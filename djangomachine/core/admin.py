from django.contrib import admin
from core.models import Car, CarPart, User

admin.site.register(User)
admin.site.register(CarPart)


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    # chia to panel namayesh bede
    list_display = ("id", "car_name", "is_repair", 'is_finished')
    # form = PostForm
    list_filter = ("is_repair", "is_finished")
    list_editable = ("is_repair", "is_finished")

    actions = ['enable_is_repair', 'enable_is_finished',
               'disable_is_repair', 'disable_is_finished']

    def enable_is_finished(self, request, queryset):
        for ele in queryset:
            ele.is_finished = True
            ele.save()

    def disable_is_finished(self, request, queryset):
        for ele in queryset:
            ele.is_finished = False
            ele.save()

    def enable_is_repair(self, request, queryset):
        for ele in queryset:
            ele.is_repair = True
            ele.save()

    def disable_is_repair(self, request, queryset):
        for ele in queryset:
            ele.is_repair = False
            ele.save()
