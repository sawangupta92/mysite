from django.shortcuts import render
from django.http import HttpResponse
import pdb
import appflux
from appflux.django.appflux_exception import AppfluxException
from mysite.main import count_beans
# Create your views here.
def index(request):
  count_beans(100)
  appflux_exception = AppfluxException()
  appflux_exception.before_notify(dafuq)
  return HttpResponse("Hello, world. You're at the polls index.")

def dafuq(self, request, exception):
  self.add_tab('test', 'hula ho')
