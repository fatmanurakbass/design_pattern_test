from django.shortcuts import render, HttpResponse
from .models import SopaDeneme

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.http import JsonResponse

# Create your views here.

def index(request):
    sopa = SopaDeneme.objects.filter(id=1)
    new_sopa = SopaDeneme(lab_id="111", lab_name="fn",
                            lab_last_name="fn", lab_pc="fn")

    new_sopa.sopa = sopa

    new_sopa.save()

    sopa_info = SopaDeneme.objects.filter()
    context = {
        "sopa_info": sopa_info
    }
    return render(request, "index.html", context)

def getresults(request):
    results = SopaDeneme.objects.all()
    return JsonResponse({"results": list(results.values())})