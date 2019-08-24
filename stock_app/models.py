# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Bond(models.Model):
    bond_id = models.AutoField(primary_key=True, blank=True, null=False)
    bond_name = models.TextField()
    shares_owned = models.IntegerField()
    purchase_price = models.FloatField()
    market_price = models.FloatField()
    purchase_date = models.TextField()
    initial_investment = models.FloatField(blank=True, null=True)
    market_value = models.FloatField(blank=True, null=True)
    profit_or_loss = models.FloatField(blank=True, null=True)
    price_difference = models.FloatField(blank=True, null=True)
    percentage_yield = models.FloatField(blank=True, null=True)
    annual_earnings_or_losses = models.FloatField(blank=True, null=True)
    investor_id = models.IntegerField()
    coupon = models.IntegerField(blank=True, null=True)
    yld = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Bond'


class Investor(models.Model):
    investor_id = models.AutoField(primary_key=True, blank=True, null=False)
    investor_name = models.TextField()
    address = models.TextField(blank=True, null=True)
    phone_number = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Investor'


class Stock(models.Model):
    stock_id = models.AutoField(primary_key=True, blank=True, null=False)
    stock_name = models.TextField()
    shares_owned = models.IntegerField()
    purchase_price = models.FloatField()
    market_price = models.FloatField()
    purchase_date = models.TextField()
    initial_investment = models.FloatField(blank=True, null=True)
    market_value = models.FloatField(blank=True, null=True)
    profit_or_loss = models.FloatField(blank=True, null=True)
    price_difference = models.FloatField(blank=True, null=True)
    percentage_yield = models.FloatField(blank=True, null=True)
    annual_earnings_or_losses = models.FloatField(blank=True, null=True)
    investor_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Stock'
