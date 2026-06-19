from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader
 
def etheria(request):
    return render(request, r"C:\Users\imaha\OneDrive\Documents\Python\Django\my_personal_website\etheria\templates\etheria\homepage.html")
def firstpage(request):
    return render(request,r"C:\Users\imaha\OneDrive\Documents\Python\Django\my_personal_website\etheria\templates\etheria\firstpage.html")