from django.contrib import admin

from django_seo.models import SEOVersion, LegalBusiness
from accounts.sites import custom_admin_site


# @admin.register(SEOVersion)
class SEOConfigurationAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'created_on']
    date_hierarchy = 'created_on'
    readonly_fields = ['version']
    search_fields = ['author', 'company_name']
    actions = ['duplicate_container']

    def duplicate_container(self, request, queryset):
        pass


class LegalBusinessAdmin(admin.ModelAdmin):
    list_display = ['legal_name', 'created_on']
    date_hierarchy = 'created_on'
    readonly_fields = ['version']
    search_fields = ['legal_name']
    actions = ['duplicate_container']

    fieldsets = [
        ['General', {'fields': ['legal_name']}],
        ['Contact', {'fields': ['general_email',
                                'customer_service_email', 'telephone', 'address_line', 'locality', 'region', 'postal_code', 'country']}],
        ['Visuals', {'fields': ['logo']}],
        ['Socials', {'fields': ['linkedin', 'facebook',
                                'twitter', 'instagram', 'youtube', 'tiktok']}]
    ]

    def duplicate_container(self, request, queryset):
        pass


custom_admin_site.register(SEOVersion, SEOConfigurationAdmin)
custom_admin_site.register(LegalBusiness, LegalBusinessAdmin)
