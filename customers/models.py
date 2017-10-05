from django.db import models


class ListCustomer(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return "List: {}".format(self.name)

class Customer(models.Model):
    name = models.CharField(max_length=100)
    fname = models.CharField(max_length=100)
    companies = models.ManyToManyField("Company",related_name = "Company")
    list = models.ForeignKey(ListCustomer, related_name = "customers")


    def __str__(self):
        return "{} by {}".format(self.name,self.list_companies())

    def list_companies(self):
        return ", ".join([Company.name for Company in self.companies.all()])


class Company(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return "Company: {}".format(self.name)