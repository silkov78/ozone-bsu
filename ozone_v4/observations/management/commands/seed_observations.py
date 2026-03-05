from __future__ import annotations

import math
from datetime import timedelta

from django.core.management.base import BaseCommand
from django.db import ProgrammingError
from django.utils.timezone import now

from observations.models import Observations


def _series_value(base: float, day_idx: int, amp: float, period_days: float) -> float:
    # Deterministic "seasonality" without random.
    return base + amp * math.sin(2 * math.pi * (day_idx / period_days)) + (day_idx % 7) * 0.2


class Command(BaseCommand):
    help = "Seed test observations data (Minsk/Homel/Naroch)"

    def add_arguments(self, parser):
        parser.add_argument("--days", type=int, default=365, help="How many days back to generate")
        parser.add_argument("--clear", action="store_true", help="Delete existing observations before seeding")

    def handle(self, *args, **options):
        days: int = options["days"]
        clear: bool = options["clear"]

        if days < 0:
            raise ValueError("--days must be >= 0")

        if clear:
            try:
                deleted, _ = Observations.objects.all().delete()
                self.stdout.write(f"Deleted {deleted} rows")
            except ProgrammingError:
                # Table does not exist yet (no migrations) – just continue seeding.
                self.stdout.write("Table observations_observations does not exist yet, skipping clear.")

        start_date = (now().date() - timedelta(days=days))

        rows = []
        for i in range(days + 1):
            d = start_date + timedelta(days=i)

            # Total ozone (Dobson units) ~ 250-450 depending on season
            o3_minsk = _series_value(330, i, 35, 365)
            o3_homel = _series_value(325, i + 3, 33, 365)
            o3_naroch = _series_value(335, i + 7, 34, 365)

            # Surface ozone (ppb) ~ 10-70
            sfo3_minsk = max(5.0, _series_value(28, i, 10, 90))

            # UV index ~ 0-10
            uvi_minsk = max(0.0, _series_value(3.0, i, 2.5, 365))
            uvi_homel = max(0.0, _series_value(3.1, i + 2, 2.4, 365))
            uvi_naroch = max(0.0, _series_value(2.9, i + 5, 2.6, 365))

            # Max UV index should be >= mean-ish
            uvi_max_minsk = max(uvi_minsk, uvi_minsk + 1.2 + (i % 5) * 0.15)
            uvi_max_homel = max(uvi_homel, uvi_homel + 1.2 + ((i + 1) % 5) * 0.15)
            uvi_max_naroch = max(uvi_naroch, uvi_naroch + 1.2 + ((i + 2) % 5) * 0.15)

            rows.append(
                Observations(
                    date=d,
                    total_ozone_minsk=round(o3_minsk, 2),
                    total_uvi_minsk=round(uvi_minsk, 2),
                    max_uvi_minsk=round(uvi_max_minsk, 2),
                    surface_ozone_minsk=round(sfo3_minsk, 2),
                    total_ozone_homel=round(o3_homel, 2),
                    total_uvi_homel=round(uvi_homel, 2),
                    max_uvi_homel=round(uvi_max_homel, 2),
                    total_ozone_naroch=round(o3_naroch, 2),
                    total_uvi_naroch=round(uvi_naroch, 2),
                    max_uvi_naroch=round(uvi_max_naroch, 2),
                )
            )

        created = 0
        for obj in rows:
            _, was_created = Observations.objects.update_or_create(
                date=obj.date,
                defaults={
                    "total_ozone_minsk": obj.total_ozone_minsk,
                    "total_uvi_minsk": obj.total_uvi_minsk,
                    "max_uvi_minsk": obj.max_uvi_minsk,
                    "surface_ozone_minsk": obj.surface_ozone_minsk,
                    "total_ozone_homel": obj.total_ozone_homel,
                    "total_uvi_homel": obj.total_uvi_homel,
                    "max_uvi_homel": obj.max_uvi_homel,
                    "total_ozone_naroch": obj.total_ozone_naroch,
                    "total_uvi_naroch": obj.total_uvi_naroch,
                    "max_uvi_naroch": obj.max_uvi_naroch,
                },
            )
            if was_created:
                created += 1

        self.stdout.write(self.style.SUCCESS(f"Seeded {len(rows)} days (created: {created}, updated: {len(rows) - created})"))

