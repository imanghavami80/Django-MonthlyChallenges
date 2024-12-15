from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string
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
    months = list(monthly_challenges.keys())

    return render(request, 'challenges/index.html', {'months': months})


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, 'challenges/challenge.html', {
            'month': month,
            'text': challenge_text,
        })
    except KeyError:
        response_data = render_to_string('404.html')
        return HttpResponseNotFound(response_data)


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        response_data = render_to_string('404.html')
        return HttpResponseNotFound(response_data)

    redirect_path = reverse('month_challenge', args=[months[month - 1]])
    return HttpResponseRedirect(redirect_path)
