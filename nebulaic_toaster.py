from kivy.app import App

from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.scatter import Scatter
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.properties import ListProperty
from kivy.properties import StringProperty
from kivy.properties import NumericProperty
from time import sleep


import random



class ScatterTextWidget(BoxLayout, Image):
	pass
class StartupGif(BoxLayout):
	windowidth = NumericProperty(1000)
	def rungif(self, *args):
		gifid = self.ids['image_gif']
		
		if gifid.source =='initiatestart.zip':
			KivyStart2().run()	
		else:
			gifid.source = 'initiatestart.zip'
	
class ScrollableLabel(ScrollView):
	text = StringProperty('')
class KivyStart(App):
	
	def build(self):
		return StartupGif()
		
class KivyStart2(App):
	def build(self):
		return ScatterTextWidget()

if __name__ == "__main__":
	KivyStart().run()
	