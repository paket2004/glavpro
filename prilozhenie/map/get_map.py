import requests
import os
from urllib.parse import quote
from PIL import Image
from io import BytesIO

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
# GOOGLE_API_KEY = "AIzaSyAL9pC1huSldjegbhv91Eqh0v1axfyMPlQ"
OUTPUT_FOLDER = "prilozhenie/map/screenshots"
ADDRESSES = ["Оренбургская область, с. Мирошкино, ул. Центральная, 27",]
ZOOM_LEVEL = 17 
IMAGE_SIZE = "1280x1280"
SHIFT_LEFT = 0.0025
SHIFT_UP = 0.001

def create_folder():
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def geocode_address(address, api_key):
    """Получение координат через Google Geocoding API"""
    encoded_address = quote(address)
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={encoded_address}&key={api_key}"
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        if data["status"] == "OK":
            location = data["results"][0]["geometry"]["location"]
            return location["lat"], location["lng"]
        else:
            print(f"Ошибка геокодирования: {data['status']} - {address}")
            return None
    except Exception as e:
        print(f"Ошибка при геокодировании {address}: {str(e)}")
        return None

def save_satellite_image(lat, lon, address, zoom=ZOOM_LEVEL, size=IMAGE_SIZE, shift_left=0, shift_up=0):
    
    shifted_lon = lon - shift_left
    shifted_lat = lat + shift_up
    """Сохранение спутникового снимка"""
    url = (
        f"https://maps.googleapis.com/maps/api/staticmap?"
        f"center={shifted_lat},{shifted_lon}"
        f"&zoom={zoom}"
        f"&size={size}"
        f"&maptype=satellite"
        f"&key={GOOGLE_API_KEY}"
    )
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        image = Image.open(BytesIO(response.content))
        image_RGB = image.convert("RGB")
        image_RGB.save("prilozhenie\map\screenshots\map_schema.jpg", format="JPEG", quality=100)
    except Exception as e:
        print(f"Ошибка при загрузке изображения для {address}: {str(e)}")
        return None

def main():
    create_folder()
    
    for address in ADDRESSES:
        print(f"\nОбработка: {address}")
        coords = geocode_address(address, GOOGLE_API_KEY)
        if coords:
            lat, lon = coords
            save_satellite_image(lat, lon, address, shift_left=SHIFT_LEFT, shift_up=SHIFT_UP)

if __name__ == "__main__":
    main()