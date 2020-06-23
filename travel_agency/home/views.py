from django.shortcuts import render
from django.http import HttpResponse

readme = ''

# copy text from readme
with open(r'C:\Users\victo\SDA_Service-for-travel-agency\README.md', 'r') as text:
    readme += text.read()


# Create your views here.
def home(request):
    # create the home page html to be returned here
    return HttpResponse('<h1> home page </h1>')


def about(request):
    return HttpResponse('<h1>Page About</h1>'
                        f'<body> {readme} </body>')
