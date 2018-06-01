from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, Context
from .forms import formulario
from .strings_example import StringsExamples
import requests
from bs4 import BeautifulSoup


# Create your views here.
def contador(request):
    if request.method == 'POST':
        form = formulario(request.POST)
        if form.is_valid():
            pagina = form.cleaned_data['pagina']
            conector = requests.get(pagina)
            statusCode = conector.status_code

            if statusCode == 200:
                htmlText = conector.text
                html = BeautifulSoup(htmlText, "html.parser")
                entradas = html.find_all('p')
                mensaje = ""
                for entrada in entradas:
                    mensaje = mensaje + " " + entrada.getText()

                resultado = StringsExamples.count_words(mensaje)
                form = formulario()
                return render(request, 'contador.html', {'mensaje': resultado, 'form': form})
            else:
                print("Status code" + statusCode)
    else:
        form = formulario()
    return render(request, 'contador.html', {'form': form})