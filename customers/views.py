from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.views.generic import View, DetailView
from django.views.generic.edit import CreateView
from .models import Customer,Company
from .forms import ReviewForm,CustomerForm

# Create your views here.
def list_customers(request):
    '''
        List the customers
    '''
    customers = Customer.objects.exclude(review__isnull=True).prefetch_related('companies')
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



class ReviewList(View):
    """
    List all of the customers that we want to review.
    """
    def get(self,request):
        customers = Customer.objects.filter(review__isnull=True).prefetch_related('companies')

        context = {
            'customers': customers,
            'form' : CustomerForm
        }

        return render(request, "list-to-review.html", context)


    def post(self,request):
        form = CustomerForm(request.POST)
        customers = Customer.objects.filter(review__isnull=True).prefetch_related('companies')

        if form.is_valid():
            form.save()
            return redirect('review-customers')

        context = {
            'form':form,
             'customers': customers,
        }

        return render(request, "list-to-review.html", context)


class CreateCompany(CreateView):
    model =  Company
    fields = ['name',]
    template_name= 'create-company.html'

    def get_success_url(self):
        return reverse('review-customers')


@login_required
def review_customers(request):
    """
    List all of the customers that we want to review.
    """
    customers = Customer.objects.filter(review__isnull=True).prefetch_related('companies')

    context = {
        'customers': customers,
    }

    return render(request, "list-to-review.html", context)


@login_required
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
            customer.reviewed_by = request.user
            customer.save()

            return redirect('review-customers')
    else:
        form = ReviewForm


    context = {
        'customer': customer,
        'form':form,
    }

    return render(request, "review-customer.html", context)
