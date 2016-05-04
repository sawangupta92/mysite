from django.shortcuts import render
from django.http import HttpResponse
import pdb
import appflux
from mysite.celery import app
from mysite.tasks import add
from appflux.django.appflux_exception import AppfluxException
# from mysite.main import count_beans
# Create your views here.
def index(request):
  # count_beans(100)
  # app.debug_task
  # mysite.tasks.add()
  # print add.name
  # add.apply_async((1,2))
  appflux_exception = AppfluxException()
  # appflux_exception.before_notify(dafuq)
  return HttpRespons("Hello, world. You're at the polls index.")

# def dafuq(self, request):
  # self.add_tab('test', 'hula ho')
