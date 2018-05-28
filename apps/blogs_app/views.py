from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
def index(request):
    return HttpResponse("this is index page")
def new(request):
    response = "<form><h1>New Form</h1><label>Name:</label><input /></form>"
    return HttpResponse(response)
def create(request):
    return HttpResponse("this is creatpage")
    return redirect("/")
def numbers(request, id):
    return HttpResponse("this is number:"+" "+'{}'.format(id))
def edit(request, id):
    return HttpResponse("edit page of number :" +" "+ '{}'.format(id))
    return redirect("/")
def delete(request, id):
    return HttpResponse("delete page of number:"+" "+'{}'.format(id))
    return redirect("/")
