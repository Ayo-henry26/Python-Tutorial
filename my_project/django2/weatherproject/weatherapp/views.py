import os
from dotenv import load_dotenv

from django.shortcuts import render
from django.contrib import messages
import requests
import datetime

load_dotenv()

# Create your views here.
def home(request):
    
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'ilorin'
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=2488016460c463badee1ffa11b347764"
    PARAMS = {'units':'metric'}
    
    API_KEY = os.getenv('GOOGLE_API_KEY')
    SEARCH_ENGINE_ID = os.getenv('SEARCH_ENGINE_ID')
    
    query = city + "1920x1080"
    page = 1
    start = (page - 1) * 10 + 1
    searchType = 'image'
    city_url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}&searchType={searchType}&imgSize=xlarge"
    
    data = requests.get(city_url).json()
    count = 1
    search_items = data.get("items")
    if search_items and len(search_items) > 0:
        image_url = search_items['link']
    else:
        image_url = "https://images.pexels.com/photos/3008509/pexels-photo-3008509.jpeg?auto=compress&cs=tinysrgb&w=1600"

    try:
        data = requests.get(url, PARAMS).json()
        
        description = data['weather'][0]['description']
        icon = data['weather'][0]['icon']
        temp = data['main']['temp']
        
        day = datetime.datetime.today()
    
        
        return render(request, 'weatherapp/index.html', {'city': city, 'description': description, 'icon': icon, 'temp': temp, 'day': day, 'exception_occurred':False, 'image_url': image_url})
    
    except:
        exception_occurred = True
        messages.error(request, 'Entered data is not available to API')
        day = datetime.datetime.today()
        
        return render(request, 'weatherapp/index.html', {'city': city, 'description': 'clear sky', 'icon': '01d'  ,'temp':25, 'day': day, 'exception_occurred': exception_occurred})