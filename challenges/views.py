from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
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
    "december": "Learn Linux!",
}

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href='{month_path}'>{capitalized_month}</a></li>"

    response_data = f"""
    <ul>
        {list_items}
    </ul>
    """
    return HttpResponse(response_data)

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
            # Send data to frontend as "context"
            "month_name": month.capitalize(),
            "text": challenge_text,
        })
    except:
        return HttpResponseNotFound("Month(str): " + month + " is not supported.")
