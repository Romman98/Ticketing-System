from django.db import models
from django.contrib.auth import get_user_model

# create a user model and call it User
User = get_user_model() # This method will return the currently active user model

# Create your models here.

class Ticket(models.Model):
    traffic_choices = [
        ('Incoming', 'Incoming'),
        ('Outgoing', 'Outgoing')    
    ]
    category_choices = [
        ('Impacted KPIs', 'Impacted KPIs'),
        ('FAS Issue', 'FAS Issue'),
        ('Call Failure', 'Call Failure')
    ]
    status_choices = [
        ('Submitted', 'Submitted'),
        ('Acknowledged','Acknowledged'),
        ('In Progress','In Progress'),
        ('Solved','Solved')
    ]
    
    ticket_ID = models.AutoField(primary_key=True)
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING,related_name='ticket')
    traffic = models.CharField(max_length=50, choices=traffic_choices)
    category = models.CharField(max_length=50, choices=category_choices)
    description = models.TextField(default='')
    status = models.CharField(max_length=50, choices=status_choices, default='submitted')
    submitted_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"TT{self.ticket_ID}"
    
class Sample(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name="samples")
    timestamp = models.DateTimeField()
    calling_number = models.IntegerField()
    called_number = models.IntegerField()
    