from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.base import EventLoop
from kivy.properties import ListProperty

from kivymd.app import MDApp
from kivymd.uix.widget import MDWidget
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import Screen
from kivymd.uix.screenmanager import ScreenManager

from fastai.vision.all import *

def is_bangla(x): 
    #print(x.parent.name)
    return x.parent.name == "bn"

learn = load_learner("export.pkl")

from plyer import filechooser

class HomeScreen(Screen):
    pass

class BoxLayoutExample(MDBoxLayout):
    pass

class Container(MDWidget):
    pass

class HelloApp(MDApp):
    selection = ListProperty([])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        EventLoop.window.bind(on_keyboard=self.hook_keyboard)

    def hook_keyboard(self, window, key, *largs):
        if key == 27 and self.root.ids.sm.current == "profile":
            self.root.ids.sm.current = "home"
        return True

    def take_picture(self):
        try:
            filechooser.open_file(on_selection=self.handle_selection)
        except NotImplementedError:
            print("Not Implemented")

    def handle_selection(self, selection):
        self.selection = selection
    
    def on_selection(self , *a, **k):
        self.get_running_app().root.ids.image1.source = str(self.selection[0])
        is_bn,_,_ = learn.predict(self.selection[0])
        print(is_bn)
        if is_bn == "True":
            self.get_running_app().root.ids.lbl_camera.text = "Bangla"
        else:
            self.get_running_app().root.ids.lbl_camera.text = "English"


    def draw_navigation(self):
        print("Navigated")

HelloApp().run()
