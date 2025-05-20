from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# Create your views here.

# def january(request):
#     return HttpResponse("Eat no meat for the entire month!")

# def february(request):
#     return HttpResponse("Walk for at least 20 minutes everyday!")

# def march(request):
#     return HttpResponse("Learn Django for at least 20 minutes everyday!")

monthly_challenges = {
    "january": "Here is january challenges!",
    "february": "Here is february challenges!",
    "march": "Here is march challenges!",
    "april": "Here is april challenges!",
    "may": "Here is may challenges!",
    "june": "Here is june challenges!",
    "july": "Here is july challenges!",
    "august": "Here is august challenges!",
    "september": "Here is september challenges!",
    "october": "Here is october challenges!",
    "november": "Here is november challenges!",
    "december": "Here is december challenges!"
}

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    redirect_month = months[month-1]
    return HttpResponseRedirect("/challenges/" + redirect_month)

def monthly_challenge(request, month):
    try:
        return HttpResponse(monthly_challenges[month])
    except:
        return HttpResponseNotFound("Month(str): " + month + " is not supported.")
