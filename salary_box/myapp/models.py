from django.db import models

# Create your models here.
STATEMENT_CHOICE = (
    ('working', 'WORKING'),
    ('close', 'CLOSE')
)

class Company(models.Model):
    name = models.CharField(max_length=99)
    founder = models.CharField(max_length=50)
    headquator = models.CharField(max_length=99)
    fund_raise = models.CharField(max_length=50)
    working = models.CharField(max_length=7, choices=STATEMENT_CHOICE, default='working')

    def __str__(self):
        return self.name


class Employee(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    address = models.CharField(max_length=99)
    experience = models.IntegerField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='company_employee')

    def __str__(self):
        return self.first_name + self.last_name
