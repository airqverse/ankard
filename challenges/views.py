from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

# def january(request):
#     return HttpResponse("Eat no meat for the entire month!")

# def february(request):
#     return HttpResponse("Walk for at least 20 minutes everyday!")

# def march(request):
#     return HttpResponse("Learn Django for at least 20 minutes everyday!")

def monthly_challenge(request, month):
    challenge_text = None
    if month == "january":
        challenge_text = "Jan: Eat no meat for the entire month!"
    elif month == "february":
        challenge_text = "Feb: Walk for at least 20 minutes everyday!"
    elif month == "march":
        challenge_text = "Mar: Learn Django for at least 20 minutes everyday!"
    else:
        return HttpResponseNotFound("Month: " + month + " is not supported.")

    return HttpResponse(challenge_text)
