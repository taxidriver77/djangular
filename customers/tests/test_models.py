from django.test import TestCase
from customers.models import Customer,ListCustomer
from customers.factories import CompanyFactory

# Create your tests here.

class CustomerTest(TestCase):
	def setUp(self):
		self.company1 = CompanyFactory(name="Company 1")
		self.company2 = CompanyFactory(name="Company 2")

		aList = ListCustomer(name="test")
		aList.save()
		self.customer = Customer(name="MyCustomer", list = aList)
		self.customer.save()
		self.customer.companies.add(self.company1.pk, self.company2.pk)

	def tearDown(self):
		self.company1.delete()
		self.company2.delete()
		self.customer.delete()

	def test_can_list_companies(self):
		self.assertEqual("Company 1, Company 2", self.customer.list_companies())

	def test_string_method(self):
		self.assertEqual("MyCustomer by Company 1, Company 2", self.customer.__str__())

	def test_custom_save_method(self):
		#self.assertIsNone(self.customer.date_reviewed)
		self.customer.review = "My review"
		self.customer.save()
		#self.assertIsNotNone(self.customer.date_reviewed)