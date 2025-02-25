from django.db import models

class Machine(models.Model):
    name = models.CharField(max_length=100)
    task = models.CharField(max_length=100)
    note = models.TextField()

    def __str__(self):
        return self.name

class Report(models.Model):
    param_1 = models.DecimalField(max_digits=10, decimal_places=2)
    param_2 = models.DecimalField(max_digits=10, decimal_places=2)
    param_3 = models.DecimalField(max_digits=10, decimal_places=2)
    param_4 = models.DecimalField(max_digits=10, decimal_places=2)
    param_5 = models.DecimalField(max_digits=10, decimal_places=2)
    param_6 = models.CharField(max_length=50)
    param_7 = models.CharField(max_length=50)
    param_8 = models.CharField(max_length=50)
    param_9 = models.CharField(max_length=50)
    param_0 = models.CharField(max_length=50)
    note = models.TextField()
    machine = models.ForeignKey('Machine', on_delete=models.CASCADE)
    

class Fixvar(models.Model):
    param_1 = models.DecimalField(max_digits=10, decimal_places=2)
    param_2 = models.DecimalField(max_digits=10, decimal_places=2)
    param_3 = models.DecimalField(max_digits=10, decimal_places=2)
    param_4 = models.DecimalField(max_digits=10, decimal_places=2)
    param_5 = models.DecimalField(max_digits=10, decimal_places=2)

