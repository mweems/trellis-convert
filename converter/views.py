from django.http import JsonResponse
from .utils import numConverter, validateNum

def convert(request, number):
    if validateNum(number):
        response = {
            'status': 'ok',
            'num_in_english': numConverter(int(number))
        }
    else:
        response = {
            'status': 'invalid',
            'num_in_english': 'url must be a number'
        }
    
    return JsonResponse(response)
