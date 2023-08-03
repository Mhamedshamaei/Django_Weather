from django.shortcuts import render, redirect
import requests
from .forms import *


def main(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data['name']
            return redirect('weather:get_weather', data)
        else:
            print(form.errors)
    all_city = City.objects.all()
    context = {'all_city': all_city}
    return render(request, 'weather/main.html', context)


def get_weather(request, slug):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=4769dd9ede3991407e58d6a7e2a28fea'
    city = slug
    city_weather = requests.get(
        url.format(city)).json()
    if city_weather['cod'] == '404':
        return redirect('weather:main')
    weather = {
        'city': city,
        'temperature': city_weather['main']['temp'],
        'min': city_weather['main']['temp_min'],
        'max': city_weather['main']['temp_max'],
        'humidity': city_weather['main']['humidity'],
        'wind': city_weather['wind']['speed'],
        'pressure': city_weather['main']['pressure'],
        'description': city_weather['weather'][0]['description'],
        'icon': city_weather['weather'][0]['icon']
    }
    context = {'weather': weather, 'x': city_weather}
    return render(request, 'weather/get_weather.html', context)
