from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse

# Create your views here.

monthly_challenges = {
    "january": "Learn Bubble Sort!",
    "february": "Learn Insertion Sort!",
    "march": "Learn Selection Sort!",
    "april": "Learn Binary Search!",
    "may": "Learn Quick Sort!",
    "june": "Learn Merge Sort!",
    "july": "Learn DFS(Depth First Search)!",
    "august": "Learn BFS(Breadth First Search)!",
    "september": "Learn Django!",
    "october": "Learn Data Structure!",
    "november": "Learn TCP/IP!",
    "december": None,
}

def index(request):
    month_list = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "month_list": month_list
    })

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])

    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]

        # render() acts as "render_to_string() + HttpResponse()"
        return render(request, "challenges/challenge.html", {
            # Send data to frontend as "context".
            # Capitalize month in frontend with filter "...|title" to avoid string formatting in backend.
            "month_name": month,
            "text": challenge_text,
        })
    except:
        # To render the 404.html page on a 404 error, set DEBUG=False in settings.py.
        # When raised, Http404() will automatically display "ankard/templates/404.html".
        raise Http404()
