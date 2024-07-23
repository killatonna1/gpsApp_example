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




class AppISpectateScreen:

    def read_i_spectate_txt(self):
        with open(f"{self.recive_app_storage_path()}/i_spectate.txt", 'r', encoding='utf-8') as file:
            i_spectate = file.readlines()
            return i_spectate

    def refresh_i_spectate_lister(self):
        try:
            self.root.ids.lister_i_spectate.clear_widgets()
            i_spectate_list = self.read_i_spectate_txt()
            num = 0 
            for line in i_spectate_list:
                print(line)
                  
                
                item = TwoLineAvatarIconListItem(#IconLeftWidget(icon="content-copy"),
                IconRightWidget(icon="delete", on_press=lambda instance, i=num: self.delete_widget_i_spectate(instance,i)),
                        text=str(line[15: -2]),
                        secondary_text=str(line[1: 11]))
            
                self.root.ids.lister_i_spectate.add_widget(item)
                num += 1
            self.root.ids.i_spectate_drawer.right_text = str(len(i_spectate_list))   
        except Exception as e:
            print(f'error link with refresh_i_spectate_lister. Error {e}')

    def delete_widget_i_spectate(self, instance, i):
        
        try:
            with open(f"{self.recive_app_storage_path()}/i_spectate.txt", 'r', encoding='utf-8') as file:
                i_spectate_list = file.readlines()
                del i_spectate_list[i]
            with open(f"{self.recive_app_storage_path()}/i_spectate.txt", 'w', encoding='utf-8') as write_file:
                write_file.writelines(i_spectate_list)
            self.copy_from_external_storage_to_local()
        except Exception as e:
            print(f'error link with rewritning file spectators while deleting. Error: {e}')
        self.refresh_i_spectate_lister()
        self.button_adding_i_spectate()

    def save_data_and_dimiss_i_spectate(self, *args):
        
        try:
                        
            text_name = self.dialog.content_cls.ids.name_textfield_spectator.text 
            text_id = self.dialog.content_cls.ids.id_textfield_spectator.text 
            

            if text_name and text_id:
                print(text_name, text_id)
                with open(f"{self.recive_app_storage_path()}/i_spectate.txt", 'a+') as file:
                    file.write(f"'{text_id}': '{text_name}'\n")
            
            # self.create_card_of_spectator()
            self.dialog.dismiss()
            self.copy_from_external_storage_to_local()
            self.refresh_i_spectate_lister()
        except Exception as e:
            print(f'error link with save_data_and_dimiss_i_spectate. Error: {e}')



    def button_adding_i_spectate(self): # +
        try:
            
            item = MDFloatingActionButton(icon="plus", 
                pos_hint={"center_x": .5, "center_y": .1}, 
                on_press=self.create_i_spectate_person)
            self.root.ids.my_spectators.add_widget(item)
            
        except Exception as e:
            print(f'problem with add_button. Error: {e}')
            
    def len_of_i_spectate(self):
        if os.path.exists(f"{self.recive_app_storage_path()}/i_spectate.txt"):
            with open(f"{self.recive_app_storage_path()}/i_spectate.txt", 'r', encoding='utf-8') as file:
                line = file.readlines()
                print(f'numbers lines spectator file = {len(line)}')
                return len(line)
        else:
             return 0
    
    def show_num_of_i_spectate(self):
        try:
            if self.len_of_i_spectate():
                return self.len_of_i_spectate()
            else:
                return 0
        except Exception as e:
            print(f"error link with show_num_of_i_spectate: {e}")
            
    def add_button_to_list(self):
        try:
            if not os.path.exists(f"{self.recive_app_storage_path()}/i_spectate.txt"):
                len_ids = 0
            else:
                with open(f"{self.recive_app_storage_path()}/i_spectate.txt", 'r', encoding='utf-8') as file:
                    file_data = file.readlines()
            
                for i in file_data:
                    self.unique_id_button = i[1:11]
                    self.root.ids.buttons_list.add_widget(
                OneLineListItem(text=f"Местоположение: {i[15: -2]}",
                                on_press=lambda instance, id = self.unique_id_button: self.center_on_func(id))
            )
        except Exception as e:
            print(f"error with add_button_to_list: {e}")
    
    def show_num_of_i_spectate(self):
        try:
            return self.len_of_i_spectate_list()
        except:
            return 0
    
    def copy_from_external_storage_to_local(self):
        try:
            with open(f"{self.recive_app_storage_path()}/i_spectate.txt", 'r', encoding='utf-8') as file:
                    all_spectators_list = file.readlines()
            with open("i_spectate.txt", 'w', encoding='utf-8') as file:
                    file.writelines(all_spectators_list)
        except Exception as e:
            print(f"error link with 'copy_from_external_storage_to_local': {e}")
            
    def button_adding_person(self):
        try:
            item = MDFloatingActionButton(icon="plus", 
                
            pos_hint={"center_x": .5, "center_y": .1},  
            on_press=self.create_i_spectate_person,
            
            
            )
            self.root.ids.i_spectate_screen.add_widget(item)
            
        except Exception as e:
            print(f'problem with add_button. Error: {e}')
            
    def refresh_all_widgets_kids(self):
        try:
            self.root.ids.lister.clear_widgets()
            self.root.ids.i_spectate_drawer.right_text = str(self.show_num_of_i_spectate())
        except Exception as e:
            print(f'eroor link with self.root.ids.lister.clear_widgets(). Error: {e}')
        

        try:
            self.add_all_kids()
        except Exception as e:
            print(f'error link with self.add_all_kids() while refresh widgets. Error {e}')
    

    def refresh_all_buttons_map(self):
        try:
            self.root.ids.buttons_list.clear_widgets()
        except Exception as e:
            print(f'eroor link with refresh_all_buttons_map. Error: {e}')
        


        try:
            self.add_button_to_list()
        except Exception as e:
            print(f'error link with add_button_to_list while refresh widgets. Error {e}')
            
    def delete_widget_1(self, instance, i):
        
        try:
            with open(f"{self.recive_app_storage_path()}/i_spectate.txt", 'r', encoding='utf-8') as file:
                all_spectators_list = file.readlines()
                del all_spectators_list[i]
            with open(f"{self.recive_app_storage_path()}/i_spectate.txt", 'w', encoding='utf-8') as write_file:
                write_file.writelines(all_spectators_list)
            self.copy_from_external_storage_to_local()
        except Exception as e:
            print(f'error link with rewritning file spectators while deleting. Error: {e}')
        self.refresh_all_widgets_spectators()
        if len(all_spectators_list) < 3:
            self.button_adding_i_spectate()


app_i_spectate_screen = AppISpectateScreen()