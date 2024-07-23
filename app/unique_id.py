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


  



import os
import random
from string import ascii_letters, digits


class AppUniqueId:
    
    def generate_id(self):
        try:
            all_letters = ascii_letters + digits
            my_unique_id = ''.join(random.sample(all_letters, 10))
            print(my_unique_id)
            return my_unique_id
        except Exception as e:
            print(f"Error link with 'def generate_id():' {e}")
        

    
    def len_of_i_spectate_list(self):
        if not os.path.exists(f"{self.recive_app_storage_path()}/my_id.txt"):
                len_ids = 0
        else:
            with open(f"{self.recive_app_storage_path()}/my_id.txt", 'r', encoding='utf-8') as file:
                file_data = file.readlines()
                len_ids = len(file_data)
        return len_ids
    
    def copy_unique_id_to_clipboard(self, id):
        try:
            
            Clipboard.copy(id)
            print(f'id: {id} скопирован')
            
        except Exception as e:
            print(f'error link with copy_unique_id_to_clipboard(). Error: {e}')

    def write_id_to_txt(self):
        
        try:
            if os.path.exists(f"{self.recive_app_storage_path()}/my_unique_id.txt"):
                with open(f"{self.recive_app_storage_path()}/my_unique_id.txt", "r", encoding="utf-8") as file:
                    data = file.read()
                    
                    if data == "":
                        with open(f"{self.recive_app_storage_path()}/my_unique_id.txt", "w", encoding="utf-8") as file:
                            file.write(f"{self.generate_id()}")   
            else:
                with open(f"{self.recive_app_storage_path()}/my_unique_id.txt", "w", encoding="utf-8") as file:
                    file.write(f"{self.generate_id()}") 
        except Exception as e:
            print(f"error link with write_id_to_txt: {e}")

    def recive_my_unique_id(self):
        try:
            if os.path.exists(f"{self.recive_app_storage_path()}/my_unique_id.txt"):
                with open(f"{self.recive_app_storage_path()}/my_unique_id.txt", encoding="utf-8") as f:
                    my_unique_id = f.read()
                    return my_unique_id
            else:
                with open(f"{self.recive_app_storage_path()}/my_unique_id.txt", "w", encoding="utf-8") as file:
                    return "No data"        
        except Exception as e:
            print(f"error link with recive_my_unique_id: {e}")            
          
    def read_internal_id(self):
        with open(f"my_unique_id.txt", "r", encoding="utf-8") as file:
            internal_id = file.read()
            return internal_id
        
    def read_external_id(self):
        with open(f"{self.recive_app_storage_path()}/my_unique_id.txt", "r", encoding="utf-8") as file:
            external_id = file.read()
            return external_id

    def add_unique_id_to_menu(self):
        try:
            with open(f"{self.recive_app_storage_path()}/my_unique_id.txt", "r", encoding="utf-8") as file_to_read:
                read_external = file_to_read.read()
                self.root.ids.unique_id_to_copy.right_text = str(read_external)
        except Exception as e:
            print(f"error link with add_unique_id_to_menu: {e}")


    def copyin_unique_id_to_external_storage(self):
        try:
            while self.read_external_id() == "" or not os.path.exists(f"{self.recive_app_storage_path()}/my_unique_id.txt"):
                with open(f"my_unique_id.txt", "r", encoding="utf-8") as file:
                    internal_id = file.read()
                with open(f"{self.recive_app_storage_path()}/my_unique_id.txt", "w", encoding="utf-8") as file_to_write:
                    file_to_write.write(internal_id)
                with open(f"{self.recive_app_storage_path()}/my_unique_id.txt", "r", encoding="utf-8") as file_to_read:
                    read_external = file_to_read.read()
                    self.root.ids.unique_id_to_copy.right_text = str(read_external)
        except Exception as e:
            print(f"error link with copyin_unique_id_to_external_storage: {e}")

    def copyin_unique_id_to_internal_storage(self):
        try:
            while self.read_internal_id() == "" or not os.path.exists("my_unique_id.txt"):
                with open(f"{self.recive_app_storage_path()}/my_unique_id.txt", "r", encoding="utf-8") as file:
                    external_id = file.read()
                with open("my_unique_id.txt", "w", encoding="utf-8") as file_to_write:
                    file_to_write.write(external_id)
               
                    
        except Exception as e:
            print(f"error link with copyin_unique_id_to_external_storage: {e}")
            
    def add_id_and_name_to_txt(self):

        try:
            if not os.path.exists(f'{self.recive_app_storage_path()}/my_id.txt'):
                
                with open(f"{self.recive_app_storage_path()}/my_id.txt", 'w', encoding='utf-8') as new_file:
                    pass
                self.my_uniq_id = self.generate_id()
                text = self.dialog.content_cls.ids.id_textfield.text
                with open(f"{self.recive_app_storage_path()}/my_id.txt", 'a', encoding='utf-8') as write_file:
                    write_file.write(f'"{self.my_uniq_id}": "{text}"\n')
            else:  
                with open(f"{self.recive_app_storage_path()}/my_id.txt", 'r', encoding='utf-8') as file:
                    file_data = file.readlines()
                    print(len(file_data), type(file_data))
            

                    if len(file_data) < 5:
                        self.my_uniq_id = self.generate_id()
                        text = self.dialog.content_cls.ids.id_textfield.text
                        with open(f"{self.recive_app_storage_path()}/my_id.txt", 'a', encoding='utf-8') as write_file:
                            write_file.write(f'"{self.my_uniq_id}": "{text}"\n')
                    
        except Exception as e:
            print(f'error link with def create_id (ferst part): Error {e}')
    
app_unique_id = AppUniqueId()