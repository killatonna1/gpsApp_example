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

class Dialog_limit(MDBoxLayout):
    name_text = StringProperty()

class ClipboardKid(MDBoxLayout):
    name_text = StringProperty()
    
class DialogLimitSpectators(MDBoxLayout):
    name_text = StringProperty()
    
class ISpectateDialog(MDBoxLayout):
    name_of_spectator = StringProperty()
    id_of_spectator = StringProperty()
    
class Content(MDBoxLayout):
    name_text = StringProperty()

class AppDialogs:
    
    def copy_unique_id_to_clipboard_dialog(self, id):
        try:
            
            Clipboard.copy(id)
            print(f'id: {id} скопирован')
            self.dialog = MDDialog(
                title=f"ID скопирован. Отправьте этот ID человеку для отслеживания",
                type="custom",
                content_cls=ClipboardKid(),
                buttons=[MDFlatButton(text="Понятно", on_release=self.kid_dismiss_dialog)])
                            
            self.dialog.open()
        except Exception as e:
            print(f'error link with copy_id(). Error: {e}')

    def open_limit_popup(self):
            try:
                self.dialog = MDDialog(
                    title="Максимум 5 человек",
                            content_cls=Dialog_limit(),
                            buttons=[
                                MDFlatButton(
                                    text="Понятно",
                                    on_release=self.dismiss_limit_dialog)])
            
                self.dialog.open()
            
                
            except Exception as e:
                print(f'Error link with open_limit_popup: Error is: {e}')
                
    def create_i_spectate_person(self, instance):
        try:
            self.dialog = MDDialog(
                title="Добавление нового человека:",
                type="custom",
                content_cls=ISpectateDialog(),
                buttons=[
                    MDFlatButton(
                        text="Отмена",
                        on_release=self.i_spectate_dimiss_dialog, 
                        
                    ),
                    MDFlatButton(
                        text="Добавить",
                        on_release=self.save_data_and_dimiss_i_spectate,
                        ),
                    ],
                )
            self.dialog.open()

        except Exception as e:
            print(f'error link with def create_person: Error {e}')

    def open_limit_popup_spectator(self):
        
        
        self.dialog = MDDialog(
            title="Максимум 3 человека",
                    content_cls=DialogLimitSpectators(),
                    buttons=[
                        MDFlatButton(
                            text="Понятно",
                            on_release=self.dismiss_limit_dialog_spectator)])
        try:    
            self.dialog.open()
        
            
        except Exception as e:
            print(f'Error link with open_limit_popup: Error is: {e}')
            

    def dismiss_dialog(self, *args):
        try:
            
            self.dialog.dismiss()
        except Exception as e:
            print(f'error link with def dismiss_dialog: Error {e}')

    def i_spectate_dimiss_dialog(self, *args):
        self.dialog.dismiss()

    def kid_dismiss_dialog(self, *args):
        
        self.dialog.dismiss()
        


    def dismiss_limit_dialog(self, *args):
        try:
            
            self.dialog.dismiss()
        except Exception as e:
            print(f'error link with def dismiss_limit_dialog: Error {e}')

    def dismiss_limit_dialog_spectator(self, *args):
        try:
            
            self.dialog.dismiss()
        except Exception as e:
            print(f'error link with def dismiss_limit_dialog: Error {e}')

    def save_data_and_dismiss(self, *args):
        try:
            text = self.dialog.content_cls.ids.id_textfield.text 
            

            
            self.add_id_and_name_to_txt()
            
            self.refresh_all_widgets_kids()
            self.dialog.dismiss()
            

            
        except Exception as e:
            print(f'error link with def dismiss_dialog: Error {e}')
            
    def create_i_spectate_person(self, instance):
        try:
            self.dialog = MDDialog(
                title="Добавление нового человека:",
                type="custom",
                content_cls=ISpectateDialog(),
                buttons=[
                    MDFlatButton(
                        text="Отмена",
                        on_release=self.i_spectate_dimiss_dialog, 
                        
                    ),
                    MDFlatButton(
                        text="Добавить",
                        on_release=self.save_data_and_dimiss_i_spectate,
                        ),
                    ],
                )
            self.dialog.open()

        except Exception as e:
            print(f'error link with def create_person: Error {e}')

    

    def create_person(self, instance):
        try:
            if not os.path.exists(f"{self.recive_app_storage_path()}/my_id.txt"):
                with open(f"{self.recive_app_storage_path()}/my_id.txt", 'w', encoding='utf-8') as file:
                    line = file.read()
            else:
                with open(f"{self.recive_app_storage_path()}/my_id.txt", 'r', encoding='utf-8') as file:
                    line = file.readlines()
                    print(f'numbers lines = {len(line)}')
                    if len(line) < 5:
                        self.dialog = MDDialog(
                            title="Добавление человека:",
                            type="custom",
                            content_cls=Content(),
                            buttons=[
                                MDFlatButton(
                                    text="Отмена",
                                    on_release=self.dismiss_dialog, 
                                    
                                ),
                                MDFlatButton(
                                    text="Добавить",
                                    on_release=self.save_data_and_dismiss)])
                        self.dialog.open()
                            
                    else:
                        self.open_limit_popup()
                        
                    
        except Exception as e:
            print(f'error link with def create_person: Error {e}')
            
app_dialogs = AppDialogs()