from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def pagina_protegida(request):
    return render(request, 'login/protegida.html')



def homepage(request):
    return render(request, 'login/homepage.html')

