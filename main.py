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

from app.unique_id import app_unique_id
from app.screens.i_spectate_screen import app_i_spectate_screen
from app.dialogs import app_dialogs
from app.gps import app_gps
from app.permissions import app_permissions




    





class DialogBackgroundPermission(MDBoxLayout):
    name_text = StringProperty()



class MapScreen(Screen):
    nav_drawer = ObjectProperty()
    
class MySpectatorsScreen(Screen):
    nav_drawer = ObjectProperty()

class DonateScreen(Screen):
    nav_drawer = ObjectProperty()

class MI(MDBoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()

class MyApp(MDApp):

    

    nav_drawer = ObjectProperty()
    screen_manager = ObjectProperty()
    latitude = NumericProperty()
    longitude = NumericProperty()

    def recive_my_unique_id(self):
        return app_unique_id.recive_my_unique_id()
    
    def copy_unique_id_to_clipboard(self):
        return app_unique_id.copy_unique_id_to_clipboard()
    
    def background_permission_popup(self):
        return app_permissions.background_permission_popup()
    
    def open_snackbar_sucsess_copy(self):
        return app_permissions.open_snackbar_sucsess_copy()
        
    def refresh_all_buttons_map(self):
        return app_i_spectate_screen.refresh_all_buttons_map()

    def on_start(self):
        app_permissions.start_service()
        print('фоновый сервис начал работу')


    def button_add_spectators_funcs(self):
        # self.refresh_all_widgets_spectators()
        app_permissions.background_permission_popup()
        app_i_spectate_screen.button_adding_i_spectate()


    def build(self):
        app_unique_id.write_id_to_txt()
        self.theme_cls.primary_palette='Blue'
        self.theme_cls.theme_style='Dark'
        app_i_spectate_screen.button_adding_person()
        app_i_spectate_screen.button_adding_i_spectate()
        # self.add_all_kids()
        # self.add_all_spectators()
        app_i_spectate_screen.refresh_i_spectate_lister()
        # self.load_person_button()
        app_i_spectate_screen.add_button_to_list()
        app_unique_id.add_unique_id_to_menu()
        app_permissions.request_android_permissions()
        app_unique_id.copyin_unique_id_to_internal_storage()
        

    def on_stop(self):
        pass
    

    def on_pause(self):
        try:    
            self.is_paused = True
            return True
        except:
            print("Error link with 'def on_pause(self):'")

    def on_resume(self):
        pass
        
if __name__ == '__main__':
    MyApp().run()
