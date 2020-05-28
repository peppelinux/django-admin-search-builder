import os

from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Identity(models.Model):
    """
    Provides registry
    """
    personal_title = models.CharField(max_length=12, blank=True, null=True)
    name = models.CharField(max_length=256, blank=False, null=False,
                            help_text=_('Name'))
    surname = models.CharField(max_length=135, blank=False, null=False)
    mail = models.EmailField()
    telephoneNumber = models.CharField(max_length=135, blank=True, null=True)
    common_name = models.CharField(max_length=256, blank=True, null=True,
                                   help_text=_('Common Name'))
    country = models.CharField(max_length=128, blank=True, null=True,
                               help_text=_('Country'))
    city = models.CharField(max_length=128, blank=True, null=True,
                            help_text=_('City'))
    tin = models.CharField(help_text=_('Tax Payer\'s Number or UniqueID'),
                                   max_length=16, blank=False, null=True)
    gender = models.CharField(max_length=3, blank=True, null=True,
                              choices=(('0', _('Not know')),
                                       ('1', _('Male')),
                                       ('2', _('Female')),
                                       ('9', _('Not specified'))))
    date_of_birth = models.DateField(blank=False, null=True)
    place_of_birth = models.CharField(max_length=128,
                                      blank=False, null=True, help_text='')
    description = models.TextField(max_length=1024, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created',]
        verbose_name_plural = _("Digital Identities")

    def __str__(self):
        return '{} {}'.format(self.name, self.surname)
