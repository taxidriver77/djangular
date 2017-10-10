from django.core.urlresolvers import resolve, reverse
from django.test import TestCase
from customers.factories import CompanyFactory, CustomerFactory, ReviewFactory, UserFactory
from customers.models import Customer,ListCustomer
from customers.views import list_customers, ReviewList


class TestListCustomer(TestCase):
	def test_list_customers_url(self):
		url = resolve('/customers/')
		self.assertEqual(url.func, list_customers)
		
	def test_list_customers_template(self):
		response = self.client.get(reverse(list_customers))
		self.assertTemplateUsed(response, 'customers.html')
		
	def test_list_customers_returns_customers_with_reviews(self):
		# Setup our data
		company = CompanyFactory()

		aList = ListCustomer(name="test")
		aList.save()
		customers_with_reviews = ReviewFactory.create_batch(2, companies=[company,],list=aList)
		customers_without_reviews = CustomerFactory.create_batch(4, companies=[company,],list=aList)
		
		response = self.client.get(reverse(list_customers))
		customers = list(response.context['customers'])
		
		self.assertEqual(customers_with_reviews, customers)
		self.assertNotEqual(customers_without_reviews, customers)
		

class TestReviewList(TestCase):
	def setUp(self):
		self.user = UserFactory(username="test")
		self.company = CompanyFactory()
		self.list = ListCustomer(name="test")
		self.list.save()
	
	def test_reviews_url(self):
		url = resolve('/customers/review/')
		self.assertEqual(url.func.__name__, ReviewList.__name__)
	
	def test_authentication_control(self):
		# Check unauthenticated users cannot view page
		response = self.client.get(reverse('review-customers'))
		self.assertEqual(response.status_code, 302)
		
		self.client.login(username="test", password="test")
		response = self.client.get(reverse('review-customers'))
		self.assertEqual(response.status_code, 200)
		
		# While we're here, confirm we're using correct template
		self.assertTemplateUsed(response, 'list-to-review.html')
		
	def test_review_list_returns_customers_to_review(self):
		# Setup our data
		customers_without_reviews = CustomerFactory.create_batch(2, companies=[self.company,],list=self.list)
		
		self.client.login(username="test", password="test")
		response = self.client.get(reverse('review-customers'))
		
		customers = list(response.context['customers'])
		self.assertEqual(customers, customers_without_reviews)
		
	def test_can_create_new_customer(self):
		self.client.login(username="test", password="test")
		response = self.client.post(
			reverse('review-customers'),
			data={
				'name': 'My Brand New Customer',
				'fname': 'Position',
				'companies': [self.company.pk,],
				'reviewed_by': self.user.pk,
				'list':self.list.pk,
			},
		)
		
		self.assertIsNotNone(Customer.objects.get(name="My Brand New Customer"))
