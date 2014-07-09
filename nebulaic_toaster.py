from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.properties import ListProperty
from kivy.properties import StringProperty
from kivy.properties import NumericProperty
from time import sleep
import random

class MainGui(BoxLayout, Image):
	textboxtext = StringProperty('')
	capnum = 113
	button_pressed = 0
	def printout(self, thetext, type):
		tbt = self.ids['textbox1']
		thetext = " " + thetext + " " 
		if type == 'add':
			tbt.text = tbt.text + thetext
		elif type == 'newline':
			tbt.text = tbt.text + "\n captain%d@shipA113: %s" % (self.capnum, thetext)
		else:
			tbt.text = thetext
	def start(self, *args):
		Story.begin()
			
	def button1press(self, *args):
		button_pressed = 1
	def button2press(self, *args):
		button_pressed = 2
	def button3press(self, *args):
		button_pressed = 3
	def button4press(self, *args):
		button_pressed = 4		
		
		
class StartupGif(BoxLayout):
	
	def rungif(self, *args):
		gifid = self.ids['image_gif']
		button1 = self.ids['initiate_button']
		if gifid.source =='initiatestart.zip':
			button1.size = [0,0]
			GameName().run()
			
		else:
			gifid.source = 'initiatestart.zip'
	def donothing(self, *args):
		pass
class KivyStart(App):
	
	def build(self):
		return StartupGif()
		
class GameName(App):
	
	def build(self):
		return MainGui()
	
		

if __name__ == "__main__":
	KivyStart().run()
	
	
class Story():
	def begin(self, *args):
		text = """ ******||||| THIS IS AN AUTOMATED MESSAGE |||||******
		
			Welcome Captain %d, you have been woken from cryosleep to control this ship.
		You will receive instructions on a daily basis outlining your course of action. You have a computer terminal, and four keys.
		These instructions must be followed. Any deviation will be noted, failure to comply will result in your demis. You hold the fate of your race in your hands.
		Good luck Captain."""
		MainGui.printout(text, 'asok')
			
	
	
	