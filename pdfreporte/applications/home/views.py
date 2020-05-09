from django.shortcuts import render
from django.http import HttpResponse
#
from .models import Empleado
#
from .utils import render_to_pdf
#
from django.views.generic import View


# Create your views here.
class ListEmpleadosPdf(View):

    def get(self, request, *args, **kwargs):
        empleados = Empleado.objects.all()
        data = {
            'count': empleados.count(),
            'empleados': empleados
        }
        pdf = render_to_pdf('home/lista.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
