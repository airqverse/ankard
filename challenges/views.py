from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

page_title = "Monthly Challenge"

monthly_challenges = {
    "january": "Here is January's challenge!",
    "february": "Here is February's challenge!",
    "march": "Here is March's challenge!",
    "april": "Here is April's challenge!",
    "may": "Here is May's challenge!",
    "june": "Here is June's challenge!",
    "july": "Here is July's challenge!",
    "august": "Here is August's challenge!",
    "september": "Here is September's challenge!",
    "october": "Here is October's challenge!",
    "november": "Here is November's challenge!",
    "december": "Here is December's challenge!",
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
        monthly_title = month.capitalize() + "'s Challenge"
        # render() acts as "render_to_string() + HttpResponse()"
        return render(request, "challenges/challenge.html", {
            # Send data to frontend as "context"
            "page_title": page_title,
            "monthly_title": monthly_title,
            "text": challenge_text,
        })
    except:
        return HttpResponseNotFound("Month(str): " + month + " is not supported.")
