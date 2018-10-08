from django.shortcuts import render
from basicapp import forms


# Create your views here.
def index(request):
    return render(request, 'basicapp/index.html')


def form_name_view(request):
    form = forms.FormName()
    if request.method == 'POST':
        form = forms.FormName(request.POST)
        if form.is_valid():
            # Do something
            print("Favorite Website Entered Was: ")
            
    return render(request, 'basicapp/form_page.html', {'myform': form})


def web_form_view(request):
    myForm = forms.WebForm()
    return render(request, 'basic_app/web_form.html', {'web_form': myForm})
