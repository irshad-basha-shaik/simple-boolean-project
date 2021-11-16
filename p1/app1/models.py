from django.db import models

# Create your models here.

from django.db import models
from django.db.models import Model


# Create your models here.

class UserModel(Model):
    username = models.CharField(max_length=100)
    fruit = models.CharField(max_length=10)
    vegetables=models.CharField(max_length=100)
    location = models.CharField(max_length=100, default='1')
    asset_no = models.CharField(max_length=100, default='1')
    emp_id = models.CharField(max_length=100, default='1')
    usage_type = models.CharField(max_length=100, default='1')
    machine_type = models.CharField(max_length=100, default='1')
    gef_id_number = models.CharField(max_length=100, default='1')
    domain_workgoup = models.CharField(max_length=100, default='1')
    make1 = models.CharField(max_length=100, default='1')
    machine_model_no = models.CharField(max_length=100, default='1')
    serial_no1 = models.CharField(max_length=100, default='1')
    hdd = models.CharField(max_length=100, default='1')
    make2 = models.CharField(max_length=100, default='1')
    model = models.CharField(max_length=100, default='1')
    serial_no2 = models.CharField(max_length=100, default='1')
    ram = models.CharField(max_length=100, default='1')
    processor_purchase_date = models.CharField(max_length=100, default='1')
    warranty_end_date = models.CharField(max_length=100, default='1')
    amc_start_date = models.CharField(max_length=100, default='1')
    amc_end_date = models.CharField(max_length=100, default='1')
    os_version = models.CharField(max_length=100, default='1')
    os = models.CharField(max_length=100, default='1')
    ms_office_version = models.CharField(max_length=100, default='1')
    oem = models.CharField(max_length=100, default='1')
    antivirus = models.CharField(max_length=100, default='1')
    autocad = models.CharField(max_length=100, default='1')
    adobe_acrobate = models.CharField(max_length=100, default='1')
    visio = models.CharField(max_length=100, default='1')
    access = models.CharField(max_length=100, default='1')
    sap = models.CharField(max_length=100, default='1')
    status = models.CharField(max_length=100, default='1')
    remarks = models.CharField(max_length=100, default='1')
    user_acceptance_date = models.CharField(max_length=100, default='1')
    user_handed_over_date = models.CharField(max_length=100, default='1')

