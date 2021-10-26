from django.shortcuts import render, HttpResponse
import requests
import json
from covid import Covid



# Create your views here.

def index(request):
    covid = Covid()
    all_country_data = covid

    #data = covid.get_data()

    vietnam_case = covid.get_status_by_country_name("VietNam")

    #print(vietnam_case)

    vietnam_confirmed = vietnam_case['confirmed']

    #print("Confirmed", vietnam_confirmed)

    vietnam_active = vietnam_case['active']

    #print("Active", vietnam_active)

    vietnam_deaths = vietnam_case['deaths']

    #print("Deaths", vietnam_deaths)

    vietnam_recovered = vietnam_case['recovered']

    #print("Recovered", vietnam_recovered)

    # confirmed = covid.get_total_confirmed_cases()

    # recovered = covid.get_total_recovered()

    # deaths = covid.get_total_deaths()

    # active = covid.get_total_active_cases()

    #print(vietnam_case)


    context = {
        'vietnam_case': vietnam_case,
        'vietnam_confirmed': vietnam_confirmed,
        'vietnam_active': vietnam_active,
        'vietnam_deaths': vietnam_deaths,
        'vietnam_recovered': vietnam_recovered,
        'all_country_data': all_country_data,
        # 'confirmed': confirmed,
        # 'deaths': deaths,
        # 'active': active,
        # 'recovered': recovered,
    }

    return render(request, 'stats/index.html', context)
