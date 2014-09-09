__author__ = 'mpetyx'

from django.shortcuts import redirect

def home(request):
    """ Home Page """
    return redirect('/api/doc/')