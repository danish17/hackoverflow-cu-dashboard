from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Event
from .forms import EventForm

# Create your views here.
def app(request):
    events_list = Event.objects.order_by('date')
    context = {'events_list': events_list}
    return render(request, "dashboard.html", context)

def reserve(request, id):
    inst = get_object_or_404(Event, pk=id)
    user = request.user
    if user.is_authenticated:
        if user in inst.reserved.all():
            inst.reserved.remove(user)
            print(inst.reserved.all())
        else:
            inst.reserved.add(user)
            print(inst.reserved.all())
    else:
        print("Not logged in!")

    return redirect('app')

def addevent(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('app')
    else:
        form = EventForm() 
    return render(request, 'addevent.html', {'form' : form}) 
    
    