from django.contrib.auth.models import User
from django.db import models
from django.core.urlresolvers import reverse


class ListCustomer(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return "List: {}".format(self.name)

class Customer(models.Model):
    name = models.CharField(max_length=100)
    fname = models.CharField(max_length=100)
    review = models.TextField(blank=True, null=True)
    reviewed_by = models.ForeignKey(User, blank=True, null=True, related_name = "reviews")
    is_favourite = models.BooleanField(default=False)
    companies = models.ManyToManyField("Company",related_name = "Company")
    list = models.ForeignKey(ListCustomer, related_name = "customers")


    def __str__(self):
        return "{} by {}".format(self.name,self.list_companies())

    def list_companies(self):
        return ", ".join([Company.name for Company in self.companies.all()])

    def save(self, *args, **kwargs):
        super(Customer, self).save(*args, **kwargs)


class Company(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return "Company: {}".format(self.name)

    def get_absolute_url(self):
        return reverse('company-detail', kwargs={'pk', self.pk})