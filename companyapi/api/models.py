from django.db import models

# Create your models here.
class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    about = models.TextField()
    type = models.CharField(max_length=100, choices = (('IT','IT'),('Non IT', 'Non It'),('Mobile Phone', 'Mobile Phone')))
    add_data = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    about = models.TextField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='employees')
    position = models.CharField(max_length=100,choices=(('Manager', 'Manager'),('Developer', 'Developer'),('Tester', 'Tester')))

    def __str__(self):
        return self.name