from django.shortcuts import render
import requests
import folium

def index(request):
    return render(request, 'index.html')

def get_country(request):
    if request.method == 'POST':
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        
        api_url = f"https://api.bigdatacloud.net/data/reverse-geocode-client?latitude={latitude}&longitude={longitude}&localityLanguage=en"
        response = requests.get(api_url)
        data = response.json()
        country_name = data.get('countryName', 'Unknown location')
        
        # Fetching country coordinates for mapping
        country_lat = data.get('latitude')
        country_lon = data.get('longitude')
        
        # Generate map with Folium
        country_map = folium.Map(location=[country_lat, country_lon], zoom_start=3)
        folium.Marker([country_lat, country_lon], popup=country_name).add_to(country_map)
        
        # Convert Folium map to HTML
        country_map_html = country_map._repr_html_()
        
        return render(request, 'result.html', {'country_name': country_name, 'country_map': country_map_html})
    
    return render(request, 'index.html')