from django.contrib import admin
from django.contrib import messages
from django.utils.translation import gettext as _


class AdvancedSearchBuilder(admin.SimpleListFilter):
    title = _('Custom Search')
    parameter_name = 'custom_search'
    template = 'filters/custom_search.html'

    def lookups(self, request, model_admin):
        """ it can be overloaded as follows
            return (('uid', 'uid'),
                    ('mail', 'mail'),
                    ('sn', 'sn'),
                    ('schacPersonalUniqueID','schacPersonalUniqueID'),
                    ('schacPersonalUniqueCode','schacPersonalUniqueCode'),
                    )
        """
        l = []
        for i in model_admin.model._meta.fields:
            l.append((i.name, i.name))
        return l

    def queryset(self, request, queryset):
        """?custom_search=filter,mail__exact,peppelinux%40thatmail.it||
        """
        if request.GET.get(self.parameter_name):
            post = dict(request.GET)[self.parameter_name][0]
            search_list = []
            search_list = post.split('||')
            for se in search_list:
                sple = se.split(',')
                se_dict = {'{}__{}'.format(sple[0], sple[2]): sple[3]}
                try:
                    queryset = getattr(queryset, sple[1])(**se_dict)
                except Exception as e:
                    messages.add_message(request, messages.ERROR,
                                         _('Search filter {} failed: {}').format(se, e))
            return queryset


    def choices(self, changelist):
        for lookup, title in self.lookup_choices:
            yield {
                'selected': self.value() == str(lookup),
                'query_string': changelist.get_query_string({self.parameter_name: lookup}),
                'display': title,
            }
