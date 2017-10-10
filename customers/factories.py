import factory
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from .models import Company, Customer,ListCustomer



class CompanyFactory(factory.django.DjangoModelFactory):
    '''
    Create a customer
    '''
    class Meta:
        model = Company

    name = factory.Faker('name')


class UserFactory(factory.django.DjangoModelFactory):
	"""
	Creates a standard user
	"""
	class Meta:
		model = User

	first_name = factory.Faker('first_name')
	last_name = factory.Faker('last_name')
	username = first_name
	password = make_password('test')


class CustomerFactory(factory.django.DjangoModelFactory):
	"""
	Creates a customer without a review.
	"""
	class Meta:
		model = Customer

	name = factory.Faker('word')
	fname = factory.Faker('word')

	@factory.post_generation
	def companies(self, create, extracted, **kwargs):
		if not create:
			return
		if extracted:
			for companies in extracted:
				self.companies.add(companies)


class ReviewFactory(CustomerFactory):
	"""
	Creates a book with a review.
	"""
	review = factory.Faker('text', max_nb_chars=400)
	reviewed_by = factory.SubFactory(UserFactory)

