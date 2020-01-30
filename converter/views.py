from django.shortcuts import render
from .utils import numConverter, validateNum
from .forms import NumForm

def index(request):
    response = {}
    form = NumForm()
    if request.method == 'POST':
        form = NumForm(request.POST)
        print(form.errors)
        if form.is_valid():
            response = {
                'status': 'ok',
                'value': numConverter(form['num'].value())
            }
        else:
            form = form
    return render(request, 'index.html', {'form': form, 'response': response})

def convert(request, num):
    if validateNum(num):
        response = {
            'status': 'ok',
            'value': numConverter(int(num))
        }
    else:
        response = {
            'status': 'invalid input',
            'value': 'url must contain a number'
        }
    return render(request, 'convert.html', {'response': response})
