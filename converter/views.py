from django.shortcuts import render
from .utils import numConverter
from .forms import NumForm

def index(request):
    response = {}
    if request.method == 'POST':
        form = NumForm(request.POST)
        if form.is_valid():
            num = int(form['num'].value())
            print(type(num))
            response = {
                'input': num,
                'status': 'ok',
                'value': numConverter(num)
            }
    form = NumForm()
    return render(request, 'index.html', {'form': form, 'response': response})
