from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

monthly_challenges = {
    "january": "Do the month #1 challenge.",
    "february": "Do the month #2 challenge.",
    "march": "Do the month #3 challenge.",
    "april": "Do the month #4 challenge.",
    "may": "Do the month #5 challenge.",
    "june": "Do the month #6 challenge.",
    "july": "Do the month #7 challenge.",
    "august": "Do the month #8 challenge.",
    "september": "Do the month #9 challenge.",
    "october": "Do the month #10 challenge.",
    "november": "Do the month #11 challenge.",
    "december": None
}


# Create your views here.

def index(request):
    list_items = ''
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse('month_challenge', args=[month])

        list_items += f'<li><a href=\"{month_path}\">{capitalized_month}</a></li>'

    response_data = f'<ul>{list_items}</ul>'
    return HttpResponse(response_data)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f'<h1>{challenge_text}</h1>'
        return HttpResponse(response_data)
    except KeyError:
        response_data = '<h1>There is no page for this url!</h1>'
        return HttpResponseNotFound(response_data)


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        response_data = '<h1>There is no page for this url!</h1>'
        return HttpResponseNotFound(response_data)

    redirect_path = reverse('month_challenge', args=[months[month - 1]])
    return HttpResponseRedirect(redirect_path)
