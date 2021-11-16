from django import forms

from app1.models import UserModel

FRUIT_CHOICES= [
    ('orange', 'Oranges'),
    ('cantaloupe', 'Cantaloupes'),
    ('mango', 'Mangoes'),
    ('honeydew', 'Honeydews'),
    ]
VEG=[('tomato','Tomatos'),('onion','Onions'),('cabbage','Cabbages'),('carrate','Carrates')]

class UserForm(forms.ModelForm):
    id = forms.IntegerField(widget=forms.HiddenInput,required=False)
    username = forms.CharField(max_length=100,  widget=forms.TextInput(attrs={'class': "form-control"}))
    location = forms.CharField(max_length=100,  widget=forms.TextInput(attrs={'class': "form-control"}))
    asset_no = forms.CharField(max_length=100,  widget=forms.TextInput(attrs={'class': "form-control"}))
    emp_id = forms.CharField(max_length=100,  widget=forms.TextInput(attrs={'class': "form-control"}))
    usage_type = forms.CharField(label='What is your favorite fruit?', widget=forms.RadioSelect(choices=FRUIT_CHOICES,attrs={'class': "form-radio-input"}))
    machine_type =forms.CharField(max_length=100,  widget=forms.TextInput(attrs={'class': "form-control"}))
    gef_id_number =forms.CharField(max_length=100,  widget=forms.TextInput(attrs={'class': "form-control"}))
    domain_workgoup = forms.CharField(max_length=100,  widget=forms.TextInput(attrs={'class': "form-control"}))
    make1 =forms.CharField(max_length=100,  widget=forms.TextInput(attrs={'class': "form-control"}))
    machine_model_no =forms.CharField(max_length=100,  widget=forms.TextInput(attrs={'class': "form-control"}))
    serial_no1 =forms.CharField(max_length=100,  widget=forms.TextInput(attrs={'class': "form-control"}))
    hdd =forms.CharField(max_length=100,  widget=forms.TextInput(attrs={'class': "form-control"}))
    make2 =forms.CharField(max_length=100,  widget=forms.TextInput(attrs={'class': "form-control"}))
    model =forms.CharField(max_length=100,  widget=forms.TextInput(attrs={'class': "form-control"}))
    serial_no2 =forms.CharField(max_length=100,  widget=forms.TextInput(attrs={'class': "form-control"}))
    ram =forms.CharField(max_length=100,  widget=forms.TextInput(attrs={'class': "form-control"}))
    processor_purchase_date =forms.CharField(max_length=100,  widget=forms.TextInput(attrs={'class': "form-control"}))
    warranty_end_date =forms.CharField(max_length=100,  widget=forms.TextInput(attrs={'class': "form-control"}))
    amc_start_date =forms.CharField(max_length=100,  widget=forms.TextInput(attrs={'class': "form-control"}))
    amc_end_date =forms.CharField(max_length=100,  widget=forms.TextInput(attrs={'class': "form-control"}))
    os_version=forms.CharField(max_length=100,  widget=forms.TextInput(attrs={'class': "form-control"}))
    os= forms.CharField(max_length=100,  widget=forms.TextInput(attrs={'class': "form-control"}))
    ms_office_version=forms.CharField(max_length=100,  widget=forms.TextInput(attrs={'class': "form-control"}))
    oem=forms.CharField(max_length=100,  widget=forms.TextInput(attrs={'class': "form-control"}))
    antivirus=forms.CharField(max_length=100,  widget=forms.TextInput(attrs={'class': "form-control"}))
    autocad=forms.CharField(max_length=100,  widget=forms.TextInput(attrs={'class': "form-control"}))
    adobe_acrobate=forms.CharField(max_length=100,  widget=forms.TextInput(attrs={'class': "form-control"}))
    visio=forms.CharField(max_length=100,  widget=forms.TextInput(attrs={'class': "form-control"}))
    access=forms.CharField(max_length=100,  widget=forms.TextInput(attrs={'class': "form-control"}))
    sap=forms.CharField(max_length=100,  widget=forms.TextInput(attrs={'class': "form-control"}))
    status=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': "form-control"}))
    remarks= forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': "form-control"}))
    user_acceptance_date=forms.CharField(max_length=100,  widget=forms.TextInput(attrs={'class': "form-control"}))
    user_handed_over_date=forms.CharField(max_length=100,  widget=forms.TextInput(attrs={'class': "form-control"}))
    class Meta:
        model = UserModel
        fields = "__all__"

class Editform(forms.ModelForm):
    id = forms.IntegerField(label='Edit object with following ID')
'''
class UserForm(forms.ModelForm):
    username= forms.CharField(max_length=100)
    fruit= forms.CharField(label='What is your favorite fruit?', widget=forms.RadioSelect(choices=FRUIT_CHOICES))
    class Meta:
        model = UserModel
'''