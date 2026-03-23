from django.shortcuts import render
from django.contrib import messages
import requests
import datetime


# Create your views here.
def home(request):
    
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'ilorin'
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=2488016460c463badee1ffa11b347764"
    PARAMS = {'units':'metric'}
    
    API_KEY = 'AIzaSyC679-kFjcc6riBGvvWMja4lR81ACRvvM0'
    SEARCH_ENGINE_ID = '3655bc726adfe4282'
    
    query = city + "1920x1080"
    page = 1
    start = (page - 1) * 10 + 1
    searchType = 'image'
    city_url = f"https://www.googleapis.com/customsearch/v1?q={query}&cx={SEARCH_ENGINE_ID}&key={API_KEY}&searchType={searchType}&start={start}&imgSize=xlarge"
    data = requests.get(city_url).json()
    count = 1
    search_items = data.get("items")
    image_url = search_items[1]['link']
    
    
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
        
        return render(request, 'weatherapp/index.html', {'city': 'ilorin', 'description': 'clear sky', 'icon': icon  ,'temp':temp, 'day': day, 'exception_occurred': exception_occurred})