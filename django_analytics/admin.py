from django.contrib import admin
from django_analytics.models import AnalyticsVersion


class AnalyticConfigurationAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'created_on']
    date_hierarchy = 'created_on'
    readonly_fields = ['version']
    fieldsets = [
        [None, {'fields': ['version']}],
        ['Google', {'fields': ['google_analytics',
                               'google_tag_manager', 'google_ads']}],
        ['Hotjar', {'fields': ['hotjar']}],
        ['Microsoft', {'fields': ['clarity']}]
    ]
    actions = ['duplicate_container']

    def duplicate_container(self, request, queryset):
        pass


admin.site.register(AnalyticsVersion, AnalyticConfigurationAdmin)
