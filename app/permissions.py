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





class AppPermissions:

    def request_android_permissions(self):
        try:
            from android.permissions import request_permissions, Permission, check_permission
        
            request_permissions([Permission.ACCESS_FINE_LOCATION, Permission.ACCESS_COARSE_LOCATION, Permission.READ_EXTERNAL_STORAGE])
            
        except:
            print("Error linking with 'request_permissions' for regular access.")

    
    def background_permission_popup(self): # +
        try:
            from android.permissions import request_permissions, Permission, check_permission
            if not check_permission(Permission.ACCESS_BACKGROUND_LOCATION):
            
                self.dialog = MDDialog(title="Важно: Предоставьте разрешение GPS", text="Необходимо выбрать 'Разрешить в любом режиме'", content_cls=DialogBackgroundPermission(),buttons=[MDFlatButton(text="Разрешить", on_release=self.give_permission)])                    
                self.dialog.open()            
        except Exception as e:
            print(f'Error link with open_permission_popup: Error is: {e}')


        

    def give_permission(self, *args):
        try:
            from android.permissions import request_permissions, Permission
        
            request_permissions([Permission.ACCESS_BACKGROUND_LOCATION])
            
        except:
            print("Error linking with 'request_permissions' for background access.")
           
        self.dismiss_dialog()

    def open_snackbar_sucsess_copy(self):
        try:
            MDSnackbar(
                MDLabel(
                    text="ID скопирован",
                ),               
                y=dp(23),
                pos_hint={"center_x": 0.5},
                size_hint_x=0.6,               
            ).open()
        except Exception as e:
            print(f"error link with open_snackbar_sucsess_copy: {e}" )

    def recive_app_storage_path(self):
        try:
            from android import mActivity
            context = mActivity.getApplicationContext()
            result =  context.getExternalFilesDir(None)   # don't forget the argument
            if result:
                storage_path =  str(result.toString())
                return storage_path
        except Exception as e:
            print(e)
        
   
    @staticmethod
    def start_service():
        try:
            service = autoclass('org.test.gpsapp_mom.ServiceMyservice')
            mActivity = autoclass('org.kivy.android.PythonActivity').mActivity            
            service.start(mActivity, '')
            return service
        except:
            print("Error link with 'def start_service():'")
            
app_permissions = AppPermissions()