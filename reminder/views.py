from django.shortcuts import render , redirect
from django.views.generic.list import ListView
from .models import reminder
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy 
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
import datetime
from datetime import datetime
from django.utils import timezone


# Create your views here.

class ReminderList(ListView):
    model = reminder
    context_object_name = 'rlist'
    template_name = 'reminder/reminder_list.html'
    

def ReminderList(request):
    current_date = timezone.now()
    lists = reminder.objects.filter(user=request.user)
    for a in lists:
        if a.status == False:
            if a.due_date <= current_date:
   
                a.status = True
                a.save()
                tempalte = render_to_string('reminder/expried.html', {'a':a})
                email = EmailMessage(
                'Expried Reminder',
                tempalte,
                settings.EMAIL_HOST_USER,
                ['djangotest05@gmail.com'],
                )
                email.fail_silently=False
                email.send()        
            
    return render(request, 'reminder/reminder_list.html', {'lists' : lists})

def delete(request,pk):
    dele=reminder.objects.get(id=pk)
    dele.delete()
    return redirect('reminder:reminder')

class ReminderDetail(DetailView):
    model = reminder
    context_object_name = 'rdetail'
    template_name = 'reminder/reminder_detail.html'
    

class ReminderCreate(CreateView):
    model = reminder
    template_name = 'reminder/reminder_form.html'
    fields ='__all__'
    
    def get_success_url(self):
        tempalte = render_to_string('reminder/mail.html')
        email = EmailMessage(
        'Set Reminder',
        tempalte,
        settings.EMAIL_HOST_USER,
        ['djangotest05@gmail.com'],
    )
        email.fail_silently=False
        email.send()
        return reverse_lazy('reminder:reminder')