from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from watersupply.forms import quater1_watersupplyForm
from watersupply.models import quater1_watersupply
#from django.db import IntegrityError

from.models import quater1_watersupply
def showquater1(request):
    return render(request,'quater_water_supply_master.html')
#from pymongo import MongoClient

def quater1list(request):
    working_place=request.POST.get("t1")
    water_supply_place=request.POST.get("t2")
    electrical_meter_no=request.POST.get("t3")
    # x = quater1_watersupply(Working_place=working_place , Water_supply_place= water_supply_place, Electrical_meter_no = electrical_meter_no)
    #
    # x.save()
    # #update = quater1list.objects.get.all()
    # return render(request, "quater_water_supply_master.html")
    #
    from pymongo import MongoClient
    client=MongoClient('mongodb://localhost:27017')
    db= client
    posts = db.quater
    x1 ={"Working_place":working_place,"Water_supply_place":water_supply_place,"Electrical_meter_no":electrical_meter_no}
    posts.quater.insert(x1)
    return render(request, "quater_water_supply_master.html",{"msg":"details saved"})

def contact_list(request):
    contacts = watersupply.objects.all().order_by("phone_number")
    return render(request, 'contacts/contact_list.html', {'contacts': contacts})

def save_contact_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            contacts = Contact.objects.all().order_by("phone_number")
            data['html_contact_list'] = render_to_string('contacts/includes/partial_contact_list.html', {
            'contacts': contacts
        })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def contact_create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
    else:
        form = ContactForm()
    return save_contact_form(request, form, 'contacts/includes/partial_contact_create.html')

def contact_update(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
    else:
        form = ContactForm(instance=contact)
    return save_contact_form(request, form, 'contacts/includes/partial_contact_update.html')

def contact_delete(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    data = dict()
    if request.method == 'POST':
        contact.delete()
        data['form_is_valid'] = True
        contacts = Contact.objects.all()
        data['html_book_list'] = render_to_string('contacts/includes/partial_contact_list.html', {
        'contacts': contacts
    })
    else:
        context = {'contact': contact}
        data['html_form'] = render_to_string('contacts/includes/partial_contact_delete.html', context, request=request)
    return JsonResponse(data)



