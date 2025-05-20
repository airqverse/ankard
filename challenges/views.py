from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

# def january(request):
#     return HttpResponse("Eat no meat for the entire month!")

# def february(request):
#     return HttpResponse("Walk for at least 20 minutes everyday!")

# def march(request):
#     return HttpResponse("Learn Django for at least 20 minutes everyday!")

def monthly_challenge_by_number(request, month):
    challenge_text = None
    if month == 1:
        challenge_text = 1
    elif month == 2:
        challenge_text = 2
    elif month == 3:
        challenge_text = 3
    else:
        return HttpResponseNotFound("Month(int): " + str(month) + " is not supported.")

    return HttpResponse(challenge_text)

def monthly_challenge(request, month):
    challenge_text = None
    if month == "january":
        challenge_text = "Jan: Eat no meat for the entire month!"
    elif month == "february":
        challenge_text = "Feb: Walk for at least 20 minutes everyday!"
    elif month == "march":
        challenge_text = "Mar: Learn Django for at least 20 minutes everyday!"
    else:
        return HttpResponseNotFound("Month(str): " + month + " is not supported.")

    return HttpResponse(challenge_text)
