from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from django.views.generic import View, DetailView
from .models import Customer,Company
from .forms import ReviewForm

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


def review_customers(request):
    """
    List all of the customers that we want to review.
    """
    customers = Customer.objects.filter().prefetch_related('companies')

    context = {
        'customers': customers,
    }

    return render(request, "list-to-review.html", context)


def review_customer(request, pk):
    """
    Review an individual customer
    """
    customer = get_object_or_404(Customer, pk=pk)

    if request.method =='POST':
        # Process our form
        form = ReviewForm(request.POST)

        if form.is_valid():
            customer.is_favourite = form.cleaned_data['is_favourite']
            customer.review = form.cleaned_data['review']
            customer.save()

            return redirect('review-customers')
    else:
        form = ReviewForm


    context = {
        'customer': customer,
        'form':form,
    }

    return render(request, "review-customer.html", context)
