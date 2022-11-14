from django.shortcuts import render

# Create your views here.

from MiApp.models import Familiares

def datos_familiares(request):

    f1 = Familiares(nombre ='Julian Moncayo', edad=23, cumpleannios='1999-06-03',parentezco="Hermano")
    f2 = Familiares(nombre ='Rosalba', edad=45, cumpleannios='1977-12-06',parentezco="Madre")
    f3 = Familiares(nombre ='Carlos Bohórquez', edad=80, cumpleannios='1970-08-15',parentezco="Tío")
    
    return render(request, 'MiApp/familia.html', {'familia':[f1,f2,f3]})