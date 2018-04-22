from django.db import models


class Owner(models.Model):
    email = models.CharField(max_length=50)
    name = models.CharField(max_length=30)
    pan_num = models.CharField(max_length=15)
    bank_acc_num = models.CharField(max_length=30)
    ifsc = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Tenant(models.Model):
    email = models.CharField(max_length=50)
    name = models.CharField(max_length=30)
    pan_num = models.CharField(max_length=15)
    bank_acc_num = models.CharField(max_length=30)
    ifsc = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Broker(models.Model):
    email = models.CharField(max_length=50)
    name = models.CharField(max_length=30)
    pan_num = models.CharField(max_length=15)
    bank_acc_num = models.CharField(max_length=30)
    ifsc = models.CharField(max_length=30)
    owners = models.ManyToManyField(Owner, blank=True)
    tenants = models.ManyToManyField(Tenant, blank=True)

    def __str__(self):
        return self.name
