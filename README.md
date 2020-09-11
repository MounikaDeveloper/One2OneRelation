# One2OneRelation
A one-to-one relationship exists when each row in one table has only
one related row in a second table. For example, a business might
decide to assign one office to exactly one employee. Thus, one
employee can have only one office. The same business might also
decide that a department can have only one manager. Thus, one
manager can manage only one department.

models.py
...........
from django.db import models
class Employee(models.Model):
 idno = models.IntegerField(primary_key=True)
 name = models.CharField(max_length=30)
class AccountInfo(models.Model):
 acno = models.IntegerField(primary_key=True)
 brach = models.CharField(max_length=30)
 ifsc = models.CharField(max_length=30)
 emp =
models.OneToOneField(Employee,on_delete=models.CASCADE)

python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser
