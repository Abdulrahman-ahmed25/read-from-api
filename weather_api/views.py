from django.shortcuts import render
import requests
# Create your views here.
def index(request):
    api_url = "http://api.openweathermap.org/data/2.5/weather?appid=838605860657bd88a6e3dbfb445e67fe&q="
    city = "cairo"
    url = api_url + city

    response = requests.get(url)
    content = response.json()
    context = {
        'city':city,
        'country':content['sys']['country'],
        'temp':content['main']['temp'],
        'description': content['weather'][0]['description'],
        'icon':content['weather'][0]['icon']
            }
    
    return render(request,'weather_api/view.html', context)