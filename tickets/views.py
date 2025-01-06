from django.shortcuts import render, redirect, get_object_or_404

from .models import Ticket, Sample
from .forms import TicketForm, SampleForm
from django.views.generic import ListView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
class TicketView(ListView):
    model = Ticket

def create_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            # Save the ticket with the logged-in user as the owner
            ticket = form.save(commit=False)
            ticket.owner = request.user
            ticket.save()
            
            # Store the ticket ID in the session
            request.session['ticket_id'] = ticket.ticket_ID

            # Redirect to the sample form page
            return redirect('add_sample')
    else:
        form = TicketForm()
    
    return render(request, 'tickets/ticket_form.html', {'form': form})

def add_sample(request):
    # Retrieve the ticket ID from the session
    ticket_id = request.session.get('ticket_id')
    if not ticket_id:
        # Handle the case where no ticket ID is found in the session
        return redirect('create_ticket')
    
    # Get the ticket instance
    ticket = Ticket.objects.get(ticket_ID=ticket_id)
    
    if request.method == 'POST':
         form = SampleForm(request.POST)
         if form.is_valid():
            sample = form.save(commit=False)
            sample.ticket = ticket # Associate the sample with the ticket
            calling_number = form.cleaned_data['calling_number']
            called_number = form.cleaned_data['called_number']  # The inputted B numbe
            date = form.cleaned_data['timestamp']
            print(date)
            cdr_validate(str(calling_number),str(called_number))
            sample.save()
            
            # Optionally, clear the ticket ID from the session if no longer needed
            # del request.session['ticket_id']
            
            return redirect('add_sample')
    else:
        form = SampleForm()

    return render(request, 'tickets/sample_form.html', {'form': form, 'ticket': ticket})

def submit_samples(request):
    ticket_id = request.session.get('ticket_id')
    
    if not ticket_id:
        return redirect('create_ticket')
    
    # Clear the ticket ID from the session if you want to end the process
    del request.session['ticket_id']

    # Redirect to a confirmation or success page
    return redirect('view_tickets')

@login_required
def viewTickets(request):
    tickets = Ticket.objects.filter(owner=request.user)
    
    return render(request, 'tickets/viewtickets.html', {'tickets':tickets})

def ticket_detail(request, ticket_id):
    ticket = get_object_or_404(Ticket, ticket_ID=ticket_id, owner=request.user)
    samples = ticket.samples.all()
    
    return render(request, 'tickets/ticket_detail.html', {'ticket':ticket, 'samples':samples})

def ticket_delete(request, ticket_id):
    ticket = get_object_or_404(Ticket, ticket_ID=ticket_id, owner=request.user)
    ticket.delete()
    
    return redirect('view_tickets')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('view_tickets')
    else:
        form = UserCreationForm()
            
    return render(request, 'userauth/signup.html', {'form': form})

def cdr_validate(date,anumber,bnumber,cdrname):
    cdrs = []
    with open(cdrname,'r') as file:
        data = file.readlines()
        for line in data:
            if anumber in line and bnumber in line and date in line:
                cdrs.append(line)

    return cdrs

def process_cdrs(cdrs_list):
    for cdr in cdrs_list:
        cdr = cdr.split(",")
        if cdr[0] == 'START':
            date=cdr[5]
            time=cdr[6]
            calling_number=cdr[14]
            called_number=cdr[15]
            incoming_trunk=cdr[28]
            outgoing_trunk=cdr[96]
        elif cdr[0] == 'ATTEMPT':
            date=cdr[5]
            time=cdr[6]
            calling_number=cdr[16]
            called_number=cdr[17]
            incoming_trunk=cdr[30]
            outgoing_trunk=cdr[100]
        elif cdr[0] == 'STOP':
            date=cdr[10]
            time=cdr[11]
            calling_number=cdr[19]
            called_number=cdr[20]
            incoming_trunk=cdr[32]
            outgoing_trunk=cdr[110]
        
        output = {
            'date' : date,
            'time' : time,
            'calling number' : calling_number,
            'called_number' : called_number,
            'incoming_trunk' : incoming_trunk,
            'outgoing_trunk' : outgoing_trunk
        }
        
        return output