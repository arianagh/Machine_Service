from django.contrib import admin
from core.models import Car, CarPart, User

admin.site.register(User)
# admin.site.register(Car)
admin.site.register(CarPart)


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("id", "car_name", "is_repair", 'is_finished')  # chia to panel namayesh bede
    # form = PostForm
    list_filter = ("is_repair", "is_finished")
    list_editable = ("is_repair", "is_finished")

    actions = ['enable_is_repair', 'enable_is_finished', 'disable_is_repair', 'disable_is_finished']

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

    def get_queryset(self, request):  # vase ine ke har useri fght post haye khodsho betone bbine
        if request.user.is_superuser:  # vase super user hamaro neshun bede
            return super().get_queryset(request)
        return super().get_queryset(request).filter(user=request.user).all()


# lsi khodroha
# filter roye finished ha masalan by repaired
# list editable
# custom action gorohi betone is finished haro false ya true kne va bar aksva baraye is repaired
# vagahti is finished true shod byd repaired ham true beshe

