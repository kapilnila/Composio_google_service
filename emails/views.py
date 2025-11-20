from django.shortcuts import render
from .composio_clients import fetch_gmail_messages
from django.http import JsonResponse
from .models import Email
from django.views.decorators.csrf import csrf_exempt


def email_list(request):
    emails = Email.objects.all().order_by('-received_at').values()
    return JsonResponse(list(emails), safe=False)

def email_list_template(request):
    from .models import Email
    emails = Email.objects.all().order_by('-received_at')
    return render(request, "emails/list.html", {"emails": emails})
  
# Create your views here.
def sync_gmail(request):
    from .composio_clients import fetch_gmail_messages
    result = fetch_gmail_messages()
    return JsonResponse(result)
