from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, DetailView
from .models import Customer,Company


# Create your views here.
def list_customers(request):
    '''
        List the customers
    '''
    customers = Customer.objects.exclude().prefetch_related('companies')
    context = {
        'customers': customers,
    }

    #return HttpResponse("My List of customers for user logged in : "  + request.user.username)
    return render(request,"customers.html",context)



class CompaniesList(View):
    def get(self,request):
            companies = Company.objects.all();

            context = {
                'companies': companies,
            }

            return render(request,"companies.html",context)



class CustomerDetail(DetailView):
    model = Customer
    template_name = 'customer.html'


class CompanyDetail(DetailView):
    model = Company
    template_name = 'company.html'
