from django import forms
from news_app.models import Author

# This is a simple form
class NewsAddForm(forms.Form):
    title = forms.CharField(max_length=30)
    ''' Here, we can not use TextField on Forms, because it does not
    exist. So the solution to this problem is to use a widget, that then, 
    takes forms.Textarea. This acts like a TextField. '''

    body = forms.CharField(widget=forms.Textarea)
    ''' The ModelChoiceField adds a queryset. The queryset is designed to
    get the django code that allows the queryset to access the sepcific data 
    being requested. Here the queryset is Author.objects.all(), means that
    the data for all of the listed Authors are being requested. This is based
    on the model for teh Class Author.'''

    author = forms.ModelChoiceField(queryset=Author.objects.all())

# Model Form
class AuthorAddForm(forms.ModelForm):
    # Meta describes what the AuthorAddForm is, as a way to create
    # a form specific to its purpose.
    class Meta:
        # model is just relaying that we are accessing the Author class
        # on the model.
        model = Author
        # field is another way to create the form with the label, in this case
        # name. On the model, name, is taking the variable name from the model.
        fields = [
            'name'
        ]


