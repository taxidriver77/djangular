from django.core.exceptions import NON_FIELD_ERRORS
from django.test import TestCase
from customers.factories import CompanyFactory, CustomerFactory
from customers.forms import CustomerForm, ReviewForm
from customers.models import ListCustomer

class ReviewFormTest(TestCase):
	def test_no_review(self):
		form = ReviewForm(data={
			'is_favourite': False,
		})
		
		self.assertFalse(form.is_valid())
		self.assertTrue(form.has_error('review', code='required'))

	def test_review_too_short(self):
		form = ReviewForm(data={
			'is_favourite': False,
			'review': 'Too short!',
		})
		
		self.assertFalse(form.is_valid())
		self.assertTrue(form.has_error('review', code='min_length'))


class CustomerFormTest(TestCase):
	def setUp(self):
		self.company = CompanyFactory()
		self.list = ListCustomer(name="test")
		self.list.save()
		self.customer = CustomerFactory(name="MyNewCustomer", companies=[self.company,],list=self.list)
		
	def test_custom_validation_rejects_customer_that_already_exists(self):
		form = CustomerForm(data={
			'name': "MyNewCustomer",
			'companies': [self.company.pk,],
			'list': self.list.pk,
			'fname': 'position',
			'reviewed_by': None,
		})
		
		self.assertFalse(form.is_valid())
		self.assertTrue(form.has_error(NON_FIELD_ERRORS, code="customerexists"))
		
	def test_custom_validation_accepts_new_customer(self):
		new_company = CompanyFactory()
		form = CustomerForm(data={
			'name': "MyUniqueCustomer",
			'companies': [new_company.pk,],
			'list': self.list.pk,
			'fname': 'position',
			'reviewed_by': None,
		})
		
		self.assertTrue(form.is_valid())
		
		
		
