from admin_adv_search_builder.filters import AdvancedSearchBuilder
from django.contrib import admin

from . models import Identity


@admin.register(Identity)
class IdentityAdmin(admin.ModelAdmin):
    list_display  = ('name', 'surname','mail', 'created')
    search_fields = ('name', 'surname','common_name',
                     'mail', 'telephoneNumber')
    list_filter   = ( #'created',
                     AdvancedSearchBuilder,)
    readonly_fields = ('created',)
