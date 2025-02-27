from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges ={
    "january":"Eat no meat in the entire month!",
    "february":"Walk for at least 20 minutes every day!",
    "march":"Learn Django at least 20 minutes every day!",
    "april":"Drink at least 3 liter of water each day!",
    "may":"Learn something new every day!",
    "june":"Practise Spanish at least 10 minutes a day!",
    "july":"Do not consume sugar for the entire month!",
    "august":"Read a book at least 10 pages in each day!",
    "september":"Do not consume milk for the entire month!",
    "october":"Wake up at 5 am every day!",
    "november":"Do not eat after 5 pm for each day!",
    "december":"Keep a journal throughout the entire month!"
}
# Create your views here.
def index(request):
    list_items=""
    months= list(monthly_challenges.keys())
    for month in months:
        capitalized_month=month.capitalize()
        month_path=reverse("month-challenge", args=[month])
        list_items+=f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
        
    
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)
    
    
def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month> len(months):
        return HttpResponseNotFound("<h1>This month is not valid!</h1>")
    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = render_to_string("challenges/challenge.html")
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")
        
