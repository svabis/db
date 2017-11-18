# -*- coding: utf-8 -*-
from django.forms import ModelForm

from klienti.models import *

from django import forms
from django.utils.translation import ugettext_lazy


class KlientsForm(ModelForm):

    name = forms.RegexField( regex=r'^\D{3,15}$',
        error_message = (u'Obligāti jāievada Vārds'),
        widget = forms.TextInput( attrs={'class': 'form-control', 'size': 30, 'title': 'Vārds:'}))

    surname = forms.RegexField( regex=r'^\D{3,15}$',
        error_message = (u'Obligāti jāievada Uzvārds'),
        widget = forms.TextInput( attrs={'class': 'form-control', 'size': 30, 'title': 'Uzvārds:'}))

    e_mail = forms.EmailField( required=True,
         widget = forms.EmailInput( attrs={'class': 'form-control', 'title': 'e-pasts:'}))

# + 3 skaitļi skaiļi+
# + 3 skaitļi atstarpe skaitļi+
# 2 + 7 skaitļi
# 6 + 7 skaitļi
    phone = forms.RegexField( regex=r'^[+]\d{3}\d+|^[+]\d{3}\s\d+|^[2]\d{7}$|^[6]\d{7}$', max_length = 15, required=True,
         error_message = (u'Ievadiet korektu Tālruņa numuru'),
         widget = forms.TextInput( attrs={'class': 'form-control', 'size': 15, 'title': 'tālrunis'}))

#    birhtday = forms.RegexField( regex=r'^\d\d\/\d\d\/\d\d\d\d$', max_length = 10, required=True,
#         error_message = (u'Ievadiet korektu datumu.'),
#         widget = forms.TextInput( attrs={'class': 'form-control', 'size': 15, 'title': 'Dzimšanas datums:'}))

#    reg_date = forms.RegexField( regex=r'^\d\d\/\d\d\/\d\d\d\d$', max_length = 10, required=True,
#         error_message = (u'Ievadiet korektu datumu.'),
#         widget = forms.TextInput( attrs={'class': 'form-control', 'size': 15, 'title': 'Dzimšanas datums:'}))

    class Meta():
        model = Klienti
        fields = ('birthday', 'reg_date', 'card_nr', 'status', 'sex', 'notes' )

        widgets = {
            'card_nr': forms.NumberInput(attrs={'class': 'form-control'}),
            'sex': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'birthday': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'reg_date': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'style':'resize:none;'})
            }

    def __unicode__(self):
        return u'%s' % (self.name)


