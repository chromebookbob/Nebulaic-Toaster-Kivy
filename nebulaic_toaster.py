from kivy.app import App

from kivy.uix.label import Label
from kivy.uix.scatter import Scatter
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.properties import ListProperty
from kivy.properties import StringProperty
from time import sleep


import random
class ScatterTextWidget(BoxLayout, Image):
	somestring = 'I just want to say:'
	textboxtext = StringProperty(somestring)
	text_color = ListProperty([7, 20, 55, 1])
	
	def rancolor(self, *args):
		color = [random.random() for i in xrange(3)] + [1]
		self.text_color = color
		
	def printout(text, self, *args):
		
		self.somestring = firsttext + text
		self.textboxtext = StringProperty(self.somestring)
		
			
	def button1press():
		printout("Hello World!")
		
class StartupGif(BoxLayout, Image):
	def rungif(self, *args):
		gifid = self.ids['image_gif']
		
		if gifid.source =='initiatestart.zip':
			KivyStart2().run()	
		else:
			gifid.source = 'initiatestart.zip'
	
class KivyStart(App):
	
	def build(self):
		return StartupGif()
		
class KivyStart2(App):
	def build(self):
		return ScatterTextWidget()

if __name__ == "__main__":
	KivyStart().run()
	