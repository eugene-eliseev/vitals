from django.db import models
from django.urls import reverse


class Race(models.Model):
    name = models.CharField(max_length=32, primary_key=True)

    def get_absolute_url(self):
        return "/race/{}/detail".format(self.pk)


class Buyer(models.Model):
    name = models.CharField(max_length=32, primary_key=True)
    phone = models.IntegerField()

    def get_absolute_url(self):
        return "/seller/{}/detail".format(self.pk)


class Seller(models.Model):
    name = models.CharField(max_length=32, primary_key=True)
    phone = models.IntegerField()

    def get_absolute_url(self):
        return "/buyer/{}/detail".format(self.pk)


class Sex(models.Model):
    name = models.CharField(max_length=1, primary_key=True)


class People(models.Model):
    first_name = models.CharField(max_length=32)
    second_name = models.CharField(max_length=32)
    reason = models.CharField(max_length=50)
    sex = models.ForeignKey(Sex, on_delete=models.PROTECT)
    is_alive = models.BooleanField()
    health_problems = models.CharField(max_length=50, default='')
    birthday = models.DateField()
    first_payment = models.IntegerField(default=0)
    buy_price = models.IntegerField(default=0)
    sell_price = models.IntegerField(default=0)
    sell_date = models.DateField()
    seller = models.ForeignKey(Seller, on_delete=models.PROTECT)
    buyer = models.ForeignKey(Buyer, on_delete=models.PROTECT, default=None)
    race = models.ForeignKey(Race, on_delete=models.PROTECT)

    def get_absolute_url(self):
        return "/people/{}/detail".format(self.pk)


class Vital(models.Model):
    name = models.CharField(max_length=32, primary_key=True)

    def get_absolute_url(self):
        return "/vital/{}/detail".format(self.pk)


class PeopleVital(models.Model):
    vital = models.ForeignKey(Vital, on_delete=models.PROTECT)
    people = models.ForeignKey(People, on_delete=models.PROTECT)
    price = models.IntegerField()
    condition = models.IntegerField()
    buyer = models.ForeignKey(Buyer, on_delete=models.PROTECT, default=None)

    def get_absolute_url(self):
        return "/pv/{}/detail".format(self.pk)
