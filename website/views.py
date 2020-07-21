from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
	return render(request, "home.html", {})

def contact(request):
	if request.method == "POST":
		message_name = request.POST["message-name"]
		message_email = request.POST["message-email"]
		message = request.POST["message"]


		send_mail(
			message_name,
			message_email,
			message,
			["kruegerjohannes03@gmail.com"],

			)
		
		return render(request, "contact.html", {})

	else:
		return render(request, "contact.html", {})

def about(request):
	return render(request, "about.html", {})

def service(request):
	return render(request, "service.html", {})

def pricing(request):
	return render(request, "pricing.html", {})

def empty(request):
	return render(request, "empty.html", {})

