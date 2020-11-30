from django import forms

class NewFeedbackForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    phone = forms.CharField(label='Phone Number', max_length=100)
    email = forms.EmailField(label='Email Address', max_length=100)
    feedback = forms.CharField(label='Feedback', max_length=1000)

class NewEnquiryForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    phone = forms.CharField(label='Phone Number', max_length=100)
    email = forms.EmailField(label='Email Address', max_length=100)
    enquiry = forms.CharField(label='Feedback', max_length=1000)
