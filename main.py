from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, NoTransition

from libs.screens.HomePage.homepage import HomePage

Window.size = (284, 610)

kv = """

"""


class PyCook(MDApp):
    def build(self):
        self.load_all_kv_files()
        self.manager = ScreenManager(transition=NoTransition())
        self.manager.add_widget(HomePage(name="homepage"))

        return self.manager

    def load_all_kv_files(self):
        Builder.load_file("libs\\screens\\HomePage\\homepage.kv")

if __name__ == "__main__":
    PyCook().run()
