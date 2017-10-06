from django.conf.urls import url
from customers.views import  (CompanyDetail,CustomerDetail,
                              list_customers,CompaniesList,review_customers,review_customer)


urlpatterns = [
    url(r'^$', list_customers, name='customers'),
    url(r'^companies/$', CompaniesList.as_view(), name='companies'),
    url(r'^companies/(?P<pk>[-\w]+)/$', CompanyDetail.as_view(), name='company-detail'),
    url(r'^customers/(?P<pk>[-\w]+)/$', CustomerDetail.as_view(), name='customer-detail'),
    url(r'^review/$', review_customers, name='review-customers'),
    url(r'^review/(?P<pk>[-\w]+)/$', review_customer, name='review-customer'),
]


