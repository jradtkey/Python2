from django.shortcuts import render, HttpResponse, redirect

def index(request):
    response = "Hello, I am your first request!"
    return HttpResponse(response)

def blogs(request):
    response = "This should be a list of blogs."
    return HttpResponse(response)

def new(request):
    response = "This is a placeholder to display a new form to create a new blog."
    return HttpResponse(response)

def create(request):
	if request.method == "POST":
        request.session['name'] = "test"  # more on session below
		print "*"*50
		return redirect("/")
	else:
		return redirect("/")

def show(request, number):
    print number
    response = "Placeholder to display blog " + number
    return HttpResponse(response)

def edit(request, number):
    print number
    response = "Placeholder to edit blog " + number
    return HttpResponse(response)

def destroy(request, number):
    print number
    response = "Placeholder to destroy blog " + number
    return HttpResponse(response)

def surveys(request):
    response = "Placeholder to display surveys."
    return HttpResponse(response)

def newSurveys(request):
    response = "Placeholder to create new surveys."
    return HttpResponse(response)

def register(request):
    response = "Placeholder for users to create a new user record."
    return HttpResponse(response)

def smelly(request):
    response = "Placeholder for users to log in"
    return HttpResponse(response)

# Create your views here.
