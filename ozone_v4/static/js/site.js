// Общие помощники нового фронта ННИЦ МО БГУ
(function () {
  const LOCALES = { ru: "ru-RU", be: "be-BY", en: "en-GB" };
  const lang = document.documentElement.lang || "ru";
  const locale = LOCALES[lang] || "ru-RU";
  const UVI = {
    ru: ["низкий", "умеренный", "высокий"],
    be: ["нізкі", "умераны", "высокі"],
    en: ["low", "moderate", "high"],
  }[lang] || ["низкий", "умеренный", "высокий"];

  // даты
  window.shortDate = s => new Date(s).toLocaleDateString(locale, { day: "numeric", month: "long" });
  window.fmtDate = s => new Date(s).toLocaleDateString(locale, { day: "numeric", month: "long", year: "numeric" });

  // уровень УФ-индекса: [css-класс, подпись]
  window.uviClass = v => v < 3 ? ["uvi-low", UVI[0]] : v < 6 ? ["uvi-mod", UVI[1]] : ["uvi-high", UVI[2]];

  // последнее непустое значение параметра в массиве наблюдений
  window.lastOf = (rows, key) => {
    for (let i = rows.length - 1; i >= 0; i--) if (rows[i][key] != null) return { date: rows[i].date, value: rows[i][key], i };
    return null;
  };

  // плавная смена раскладки (View Transitions), без анимации — если пользователь её отключил
  window.REDUCED_MOTION = matchMedia("(prefers-reduced-motion: reduce)").matches;
  window.smooth = fn => document.startViewTransition && !REDUCED_MOTION ? document.startViewTransition(fn) : fn();

  // Chart.js-плагин: линия аккуратно прорисовывается слева направо
  window.drawIn = {
    id: "drawIn",
    beforeDatasetsDraw(c) {
      if (REDUCED_MOTION) return;
      c.$t0 ??= performance.now();
      const t = Math.min(1, (performance.now() - c.$t0) / 2200), p = Math.sin(t * Math.PI / 2), a = c.chartArea;
      c.ctx.save(); c.ctx.beginPath(); c.ctx.rect(a.left - 2, a.top - 10, (a.right - a.left + 4) * p, a.bottom - a.top + 20); c.ctx.clip();
      if (t < 1) requestAnimationFrame(() => c.draw());
    },
    afterDatasetsDraw(c) { if (!REDUCED_MOTION) c.ctx.restore(); },
  };

  // шапка: тёмная поверх hero, светлая ниже; бургер-меню
  document.addEventListener("DOMContentLoaded", () => {
    const hero = document.querySelector(".hero"), hd = document.querySelector(".header");
    if (hero && hd) {
      document.body.classList.add("has-hero");
      const upd = () => hd.classList.toggle("dark", hero.getBoundingClientRect().bottom > 68);
      addEventListener("scroll", upd, { passive: true }); upd();
    }
    document.querySelector(".burger")?.addEventListener("click", () => document.getElementById("nav").classList.toggle("open"));
  });
})();
