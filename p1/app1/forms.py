from django import forms

from app1.models import UserModel

FRUIT_CHOICES= [
    ('orange', 'Oranges'),
    ('cantaloupe', 'Cantaloupes'),
    ('mango', 'Mangoes'),
    ('honeydew', 'Honeydews'),
    ]
VEGETABLES=[
('tomato','Tomatos'),('brinjal','Brinjals'),('potato','Potatos'),('lfinger','Lfingers')
]
class UserForm(forms.ModelForm):
    id = forms.IntegerField(widget=forms.HiddenInput)
    username = forms.CharField(max_length=100)
    fruit = forms.CharField(label='What is your favorite fruit?', widget=forms.RadioSelect(choices=FRUIT_CHOICES))
    vegetables = forms.CharField(label='Choose vegetables?', widget=forms.RadioSelect(choices=VEGETABLES))
    class Meta:
        model = UserModel
        fields = "__all__"

class Editform(forms.ModelForm):
    id = forms.IntegerField(label='Edit object with following ID')
