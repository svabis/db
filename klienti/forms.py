# -*- coding: utf-8 -*-
from django.forms import ModelForm

from klienti.models import *

from django import forms
from django.utils.translation import ugettext_lazy


class KlientsForm(ModelForm):

#    name = forms.RegexField( regex=r'^\D{3,15}$',
#        error_message = (u'Obligāti jāievada Vārds'),
#        widget = forms.TextInput( attrs={'class': 'form-control', 'size': 30, 'title': 'Vārds:'}))

#    surname = forms.RegexField( regex=r'^\D{3,15}$',
#        error_message = (u'Obligāti jāievada Uzvārds'),
#        widget = forms.TextInput( attrs={'class': 'form-control', 'size': 30, 'title': 'Uzvārds:'}))

#    e_mail = forms.EmailField( required=True,
#         widget = forms.EmailInput( attrs={'class': 'form-control', 'title': 'e-pasts:'}))

#    phone = forms.RegexField( regex=r'^[+]\d{3}\d+|^[+]\d{3}\s\d+|^[2]\d{7}$|^[6]\d{7}$', max_length = 15, required=True,
#         error_message = (u'Ievadiet korektu Tālruņa numuru'),
#         widget = forms.TextInput( attrs={'class': 'form-control', 'size': 15, 'title': 'tālrunis'}))

# + 3 skaitļi skaiļi+
# + 3 skaitļi atstarpe skaitļi+
# 2 + 7 skaitļi
# 6 + 7 skaitļi


    class Meta():
        model = Klienti
        fields = ('name', 'surname', 'e_mail', 'phone', 'birthday', 'reg_date', 'card_nr', 'status', 'sex', 'notes' )

        widgets = {
            'name': forms.TextInput( attrs={'class': 'form-control', 'size': 30}),
            'surname': forms.TextInput( attrs={'class': 'form-control', 'size': 30}),
            'e_mail': forms.EmailInput( attrs={'class': 'form-control'}),
            'phone': forms.TextInput( attrs={'class': 'form-control', 'size': 15}),

            'card_nr': forms.TextInput(attrs={'class': 'form-control'}),
            'sex': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),

# works            'birthday': forms.DateTimeInput(attrs={'class': 'form-control'}),
# nope           'birthday': forms.SelectDateWidget(attrs={'class': 'form-control'}),
            'birthday': forms.DateInput(attrs={'class': 'form-control'}),

            'reg_date': forms.DateInput(attrs={'class': 'form-control', 'readonly':'readonly'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'style':'resize:none;'})
            }

#        myform.fields['status'].widget.attrs['readonly'] = True

    def __unicode__(self):
        return u'%s' % (self.name)


