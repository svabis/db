# -*- coding: utf-8 -*-
from django.forms import ModelForm

from clients.models import *

from django import forms
from django.utils.translation import ugettext_lazy


class KlientsForm(ModelForm):

    status = forms.ModelChoiceField( queryset = Statusi.objects.all().order_by('status_order'),
         widget = forms.Select(attrs={'class': 'form-control'}))

    class Meta():
        model = Klienti
        fields = ('avatar', 'name', 'surname', 'e_mail', 'phone', 'birthday', 'reg_date', 'card_nr', 'society', 'gender', 'notes',
                  'disabled', 'disabled_until', 'student', 'student_until', 'elderly', 'status')

        widgets = {
            'avatar': forms.FileInput(),
            'name': forms.TextInput( attrs={'class': 'form-control', 'size': 30}),
            'surname': forms.TextInput( attrs={'class': 'form-control', 'size': 30}),
            'e_mail': forms.EmailInput( attrs={'class': 'form-control'}),
            'phone': forms.TextInput( attrs={'class': 'form-control', 'size': 15}),

            'card_nr': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
#            'status': forms.Select(attrs={'class': 'form-control'}),
            'society': forms.CheckboxInput(attrs={'class': 'form-control'}),

            'birthday': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'GGGG-MM-DD'}),

            'reg_date': forms.DateInput(attrs={'class': 'form-control', 'readonly':'readonly'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'style':'resize:none;'}),

            'disabled': forms.CheckboxInput(attrs={'class': 'form-control', 'onclick': 'selectOnlyThis(this.id)'}),
            'disabled_until': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'GGGG-MM-DD'}),
            'student': forms.CheckboxInput(attrs={'class': 'form-control', 'onclick': 'selectOnlyThis(this.id)'}),
            'student_until': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'GGGG-MM-DD'}),
            'elderly': forms.CheckboxInput(attrs={'class': 'form-control', 'onclick': 'selectOnlyThis(this.id)'})

            }


    def __unicode__(self):
        return u'%s' % (self.name)


