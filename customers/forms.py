from django import forms

class ReviewForm(forms.Form):
       '''
       Form for reviewing customer
       '''

       is_favorite = forms.BooleanField(
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


