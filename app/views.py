from django.shortcuts import render
from app.models import AccountDetailsModel
# Create your views here.
def showIndex(request):
    return render(request,"index.html",{"data":AccountDetailsModel.objects.all()})