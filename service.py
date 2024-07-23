

from jnius import autoclass
import os.path
import requests
from plyer import gps
import time
import os

PythonService = autoclass('org.kivy.android.PythonService')
PythonService.mService.setAutoRestartService(True)
# latitude = 0.0
# longitude = 0.0


def recive_my_unique_id():
    try:
        if os.path.exists("my_unique_id.txt"):
            with open("my_unique_id.txt", encoding="utf-8") as f:
                my_unique_id = f.read()
                print(f"Мой уникальный id: {my_unique_id}")
                return my_unique_id               
    except Exception as e:
        print(f"error link with recive_my_unique_id: {e}")  

def get_gps_data():
    def on_location(**kwargs):
        latitude = kwargs.get('lat')
        longitude = kwargs.get('lon')
        print(f'coords background service: {latitude}, {longitude}')
        process_coordinates(latitude, longitude)
    gps.configure(on_location=on_location)
    gps.start(5000, 0)  

def process_coordinates(latitude, longitude):
    try:
        id_one =  recive_my_unique_id()
        print(str(id_one))           
        data = {"id": str(id_one),"coordinates": [latitude, longitude]}
                # Sending data:
        response = requests.post('http://45.146.164.92:5000/api/data/send', json=data)
        if response.status_code == 200:
            print("Data sent successfully!")
        else:
            print('Error sending data to server')
            print("Response status code:", response.status_code)
            print("Response content:", response.content)
            print(f'Отправлены данные Spectator: {recive_my_unique_id()}')
    except Exception as e:
        print(f"Error link with process_coordinates_1:' {e}")



if __name__ == '__main__':
    while True:
        get_gps_data()
        time.sleep(3)
        print('сон 3 сек.')
            
       
    