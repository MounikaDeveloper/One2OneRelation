from django.db import models

# Create your models here.
class EmployeeModel(models.Model):
    idno=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=30)
    def __int__(self):
        return self.idno

class AccountDetailsModel(models.Model):
    accno=models.IntegerField(primary_key=True)
    branch=models.CharField(max_length=30)
    ifsc=models.CharField(max_length=30)
    emp=models.OneToOneField(EmployeeModel,on_delete=models.CASCADE)

    def __int__(self):
        return self.accno
