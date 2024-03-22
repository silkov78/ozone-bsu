from django.contrib import admin

from .models import (
    Worker, Education, Career, Reward, ScienceInterest, Publication
)


# admin.site.register(Education)
# admin.site.register(Career)
# admin.site.register(Reward)
# admin.site.register(ScienceInterest)
# admin.site.register(Publication)


class WorkersEducationInline(admin.TabularInline):
    model = Education
    extra = 1
    classes = ('collapse', )


class WorkersCareerInline(admin.TabularInline):
    model = Career
    extra = 1
    classes = ('collapse', )


class WorkersRewardInline(admin.TabularInline):
    model = Reward
    extra = 1
    classes = ('collapse', )


class WorkersScienceInterestInline(admin.TabularInline):
    model = ScienceInterest
    extra = 1
    classes = ('collapse', )


class WorkersPublicationInline(admin.TabularInline):
    model = Publication
    extra = 3
    classes = ('collapse', )


@admin.register(Worker)
class ProductAdmin(admin.ModelAdmin):

    inlines = [
        WorkersEducationInline,
        WorkersCareerInline,
        WorkersRewardInline,
        WorkersScienceInterestInline,
        WorkersPublicationInline
    ]

    list_display = ['last_name', 'first_name',  'academic_rank', 'ordering', ]
    readonly_fields = ('id', 'last_edit', 'time_creation')
