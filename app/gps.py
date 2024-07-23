import kivy
import asyncio
from kivy.app import async_runTouchApp
from kivy.uix.screenmanager import ScreenManager, Screen
import threading
import os
from kivy.metrics import dp
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.button import MDFlatButton
# import asyncio
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty
import random
from string import ascii_letters
from string import digits
from kivy_garden.mapview import MapView
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.dialog import MDDialog
from kivymd.uix.snackbar.snackbar import MDSnackbarActionButton
from kivymd.uix.snackbar.snackbar import MDSnackbar
from kivymd.uix.label import MDLabel
import requests
from kivymd.icon_definitions import md_icons
from kivy.properties import NumericProperty
from kivy.core.clipboard import Clipboard
from jnius import autoclass
from kivymd.uix.list import OneLineListItem
from kivymd.uix.list import TwoLineAvatarIconListItem
from kivymd.uix.list import IconLeftWidget
from kivymd.uix.list import IconRightWidget
from kivymd.uix.button import MDFloatingActionButton
from kivymd.uix.snackbar import Snackbar






class AppGPS:

    def center_on_func(self, id):
        u_id = id
        print(f'u_id: {u_id}')
        
        
        try:
            
            
            response = requests.get(f'http://45.146.164.92:5000/api/data/get/{u_id}')
            if response.status_code == 200:
                data = response.json()
                print("Received data:", data)
                coordinates = data.get('coordinates', None)
                if coordinates is not None:
                    latitude = float(coordinates[0])
                    longitude = float(coordinates[1])
                    self.latitude = latitude
                    self.longitude = longitude
                    
                else:
                    print('Error: Invalid coordinates data')
                
            else:
                print('Error getting data from server')
                print("Response status code:", response.status_code)
                print("Response content:", response.content)
        except Exception as e:
            print(f'Error with recive data. Error: {e}')
        
        try:
            self.root.ids.map_view.center_on(self.latitude, self.longitude).start()
            
        except Exception as e:
            print(e, 'Erroe with center_on function')
            
app_gps = AppGPS()