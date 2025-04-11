import requests
import os
from urllib.parse import quote
from PIL import Image
from io import BytesIO

# Конфигурация (ПЕРЕМЕСТИТЕ В ПЕРЕМЕННЫЕ ОКРУЖЕНИЯ!)
GOOGLE_API_KEY = "AIzaSyAL9pC1huSldjegbhv91Eqh0v1axfyMPlQ"  # Замените на свой ключ
OUTPUT_FOLDER = "prilozhenie/map/screenshots"
ADDRESSES = [
    "Оренбургская область, с. Мирошкино, ул. Центральная, 27",
    # Добавьте другие адреса по необходимости
]
ZOOM_LEVEL = 17  # 18-20 для детализации зданий
# IMAGE_SIZE = "640x640"  # Максимальный размер для бесплатного тарифа
IMAGE_SIZE = "1280x1280"  # Требуется платный тариф Google Maps Static API!
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

        # Уменьшаем изображение, чтобы сымитировать масштаб между 17 и 18
        # resized_image = image.resize((960, 960), Image.LANCZOS)
        resized_image = image.resize((960, 960), Image.LANCZOS).convert("RGB")


        safe_address = "".join(c if c.isalnum() else "_" for c in address)
        filename = f"{safe_address}_{lat}_{lon}_z{zoom}_scaled.jpg"
        filepath = os.path.join(OUTPUT_FOLDER, filename)

        resized_image.save(filepath, format="JPEG")
        print(f"Сохранено: {filepath}")
        return filepath
    except Exception as e:
        print(f"Ошибка при загрузке изображения для {address}: {str(e)}")
        return None
    # try:
    #     response = requests.get(url, timeout=10)
    #     response.raise_for_status()
        
    #     # Создаем безопасное имя файла
    #     safe_address = "".join(c if c.isalnum() else "_" for c in address)
    #     filename = f"{safe_address}_{lat}_{lon}_z{zoom}.jpg"
    #     filepath = os.path.join(OUTPUT_FOLDER, filename)
        
    #     with open(filepath, "wb") as f:
    #         f.write(response.content)
    #     print(f"Сохранено: {filepath}")
    #     return filepath
    # except Exception as e:
    #     print(f"Ошибка при загрузке изображения для {address}: {str(e)}")
    #     return None
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