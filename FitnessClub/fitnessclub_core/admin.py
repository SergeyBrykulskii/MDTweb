from django.contrib import admin
from .models import GymMembership, Gym, Schedule, GroupClass

class GroupClassInline(admin.TabularInline):
    model = GroupClass
    extra = 0


@admin.register(Gym)
class GymAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'display_group_classes']
    list_filter = ['schedule', 'gym_membership']
    inlines = [GroupClassInline]

    def display_group_classes(self, obj):
        return ", ".join([group_class.name for group_class in obj.group_classes.all()])  

    display_group_classes.short_description = 'Group Classes'


@admin.register(GymMembership)
class GymMembershipAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'cost']


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ['open_time', 'close_time', 'is_works_on_weekends']
    fields = [('open_time', 'close_time'), 'is_works_on_weekends']


@admin.register(GroupClass)
class GroupClassAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'cost', 'gym']
    list_filter = ['gym']
    fields = [('name', 'description'), 'gym']

