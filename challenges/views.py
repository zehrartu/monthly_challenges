from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.http import HttpResponseRedirect
from django.urls import reverse

monthly_challenges ={
    "january":"Eat no meat in the entire month!",
    "february":"Walk for at least 20 minutes every day!",
    "march":"Learn Django at least 20 minutes every day!",
    "april":"Eat no meat in the entire month!",
    "may":"Walk for at least 20 minutes every day!",
    "june":"Learn Django at least 20 minutes every day!",
    "july":"Eat no meat in the entire month!",
    "august":"Walk for at least 20 minutes every day!",
    "september":"Learn Django at least 20 minutes every day!",
    "october":"Eat no meat in the entire month!",
    "november":"Walk for at least 20 minutes every day!",
    "december":"Learn Django at least 20 minutes every day!"
}
# Create your views here.
def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month> len(months):
        return HttpResponseNotFound("This month is not valid!")
    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported!")
        
