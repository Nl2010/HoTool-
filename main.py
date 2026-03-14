from kivy.app import App
from kivy.lang import Builder
import os

class HPTool(App):

    def build(self):
        return Builder.load_file("design.kv")

    def scan(self):
        os.system("python scan.py")

    def backup(self):
        os.system("python backup.py")


HPTool().run()