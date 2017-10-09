from django import forms
from .models import Customer

class ReviewForm(forms.Form):
       '''
       Form for reviewing customer
       '''

       is_favourite = forms.BooleanField(
           label="Favourite ?",
           help_text = 'In you top 100 customers of all',
           required = False,
       )

       review = forms.CharField(
           widget=forms.Textarea,
           min_length=300,
           error_messages={
               'required':'Please enter your review',
               'min_length':'Please write at least 300 characters (you have written %(show_value)s',
           }
       )


class CustomerForm(forms.ModelForm):
   class Meta:
        model = Customer
        fields = ['name','companies','fname','list']


   def clean(self):
        # Super the clean method to maintain main validation and error messages
        super(CustomerForm, self).clean()

        try:
            name = self.cleaned_data.get('name')
            companies = self.cleaned_data.get('companies')
            customer = Customer.objects.get(name=name, companies=companies)

            raise forms.ValidationError(
				'The customer {} by {} already exists'.format(name, customer.list_companies()),
				code='customerexists'
            )

        except Customer.DoesNotExist:
            return self.cleaned_data


