from django.shortcuts import render
from django.db.models import Sum, F, ExpressionWrapper

from .models import PriceList

from .models import Person1
from .models import Person2

# Create your views here.

# Preisliste anzeigen

def Koop_view_price(request):

    #all_items = Person1.objects.get(id=1)
    #all_items = Person1.objects.filter(name='Hallo')

    # Alphabetisch sortieren
    all_items = PriceList.objects.order_by('name')
    return render(request, 'koop_price.html', {'all_items': all_items})


# Person 1

def Person_1_addSmart(request):
    if request.method == 'POST':
        entry = PriceList.objects.get(id = request.POST['itemNumber'])
        print('Hinzufügen (aus Preisliste):',entry)
        Person1.objects.create(name = entry.name, amount = request.POST['itemAmount'], price = entry.price)
    all_items = Person1.objects.all()
    return render(request, 'koop_1.html', {'all_items': all_items})

def Person_1_add(request):
    if request.method == 'POST':
        Person1.objects.create(name = request.POST['itemName'], amount = request.POST['itemAmount'], price = request.POST['itemPrice'])
        print('Hinzufügen (manuell)')
    all_items = Person1.objects.all()
    return render(request, 'koop_1.html', {'all_items': all_items})

def Person_1_delete(request):
    if request.method == 'POST':
        what_to_delete = Person1.objects.get(id = request.POST['itemNumber'])
        print('Lösche:',what_to_delete)
        what_to_delete.delete()
    return render(request, 'koop_1.html')

def Person_1_sum(request):
    if request.method == 'POST':
        alle_eintraege = Person1.objects.all()
        gesamte_euro_summe = 0
        for id in alle_eintraege:
            gesamte_euro_summe += id.price * id.amount
        print(gesamte_euro_summe)
    return render(request, 'koop_1.html')

# Person 2

def Person_2_add(request):
    if request.method == 'POST':
        Person2.objects.create(name = request.POST['itemName'])
    all_items = Person2.objects.all()
    return render(request, 'koop_2.html', {'all_items': all_items})
