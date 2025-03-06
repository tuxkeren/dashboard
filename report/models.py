from django.db import models

class Machine(models.Model):
    TASK = [
        ('T', 'Threading'),
        ('W', 'Welding')
    ]
    name = models.CharField(max_length=100)
    task = models.CharField(max_length=100, choices=TASK)
    note = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Report(models.Model):
    param_1 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    param_2 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    param_3 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    param_4 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    param_5 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    param_6 = models.CharField(max_length=50, null=True, blank=True)
    param_7 = models.CharField(max_length=50, null=True, blank=True)
    param_8 = models.CharField(max_length=50, null=True, blank=True)
    param_9 = models.CharField(max_length=50, null=True, blank=True)
    param_0 = models.CharField(max_length=50, null=True, blank=True)
    note = models.TextField(null=True, blank=True)
    machine = models.ForeignKey('Machine', on_delete=models.CASCADE)
    

class Fixvar(models.Model):
    param_1 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    param_2 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    param_3 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    param_4 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    param_5 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

