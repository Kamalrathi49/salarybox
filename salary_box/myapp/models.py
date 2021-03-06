from django.db import models
from django.contrib.auth.models import User
# Create your models here.
STATEMENT_CHOICE = (
    ('working', 'WORKING'),
    ('close', 'CLOSE')
)

class Company(models.Model):
    name = models.CharField(max_length=99, unique=True)
    founder = models.CharField(max_length=50)
    headquator = models.CharField(max_length=99)
    fund_raise = models.CharField(max_length=50)
    working = models.CharField(max_length=7, choices=STATEMENT_CHOICE, default='working')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')

    def __str__(self):
        return self.name

    def get_employee_count(self):
        return Employee.objects.filter(company = self).count()


class Employee(models.Model):
    # id = models.IntegerField(primary_key=True, unique=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    address = models.CharField(max_length=99)
    experience = models.IntegerField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='employee')
     
    def __str__(self):
        return self.first_name + self.last_name
