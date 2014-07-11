from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.properties import ListProperty
from kivy.properties import StringProperty
from kivy.properties import NumericProperty
from kivy.properties import ObjectProperty
import time
import random

class MainGui(BoxLayout, Image):
	capnum = 113
	button_pressed = 0
	start1 = False	
	next = 'start'
	day = 1
	postit = False
	textboxtext = """Welcome Captain %d, you have been woken from cryosleep to control this ship.
		You will receive instructions on a daily basis outlining your course of action. You have a computer terminal, and four keys.
		These instructions must be followed. Any deviation will be noted, failure to comply will result in your demise. You hold the fate of your race in your hands.
		Good luck Captain. \n captain%d@shipA113: Take Command, Press 1""" % (capnum, capnum)
	def wait(self, time_lapse):
		time_start = time.time()
		time_end = (time_start + time_lapse)
 
		while time_end > time.time():
			pass
	def printout(self, thetext, type):
			tbt = self.ids['textbox1']
			thetext = " " + thetext + " " 
			if type == 'add':
				tbt.text = tbt.text + thetext
			elif type == 'newline':
				tbt.text = tbt.text + "\n captain%d@shipA113: %s" % (self.capnum, thetext)		
			else:
				tbt.text = thetext				
	def newday(self):
		but1 = self.ids['button1']
		but2 = self.ids['button2']
		but3 = self.ids['button3']
		but4 = self.ids['button4']
		img = self.ids['centre_image']
		tb = self.ids['textbox1']
		but1.background_normal = 'clear.png'
		but2.background_normal = 'clear.png'
		but3.background_normal = 'clear.png'
		but4.background_normal = 'clear.png'
		but1.background_down = 'clear.png'
		but2.background_down = 'clear.png'
		but3.background_down = 'clear.png'
		but4.background_down = 'clear.png'
		tb.foreground_color = [1, 1, 1, 0]
		but1.color = [1, 1, 1, 0]
		but2.color = [1, 1, 1, 0]
		but3.color = [1, 1, 1, 0]
		but4.color = [1, 1, 1, 0]
		img.source = 'day%d.png' % self.day
	def newdaystop(self):
		but1 = self.ids['button1']
		but2 = self.ids['button2']
		but3 = self.ids['button3']
		but4 = self.ids['button4']
		img = self.ids['centre_image']
		tb = self.ids['textbox1']
		but1.background_normal = 'buttonup.png'
		but2.background_normal = 'buttonup.png'
		but3.background_normal = 'buttonup.png'
		but4.background_normal = 'buttonup.png'
		but1.background_down = 'buttondown.png'
		but2.background_down = 'buttondown.png'
		but3.background_down = 'buttondown.png'
		but4.background_down = 'buttondown.png'
		tb.foreground_color = [0, 0, 0, 1]
		but1.color = [1, 1, 1, 1]
		but2.color = [1, 1, 1, 1]
		but3.color = [1, 1, 1, 1]
		but4.color = [1, 1, 1, 1]
		if self.postit == True:
			img.source = 'Templatepostit.png'
		else:
			img.source = 'TemplatePic.png'
		self.day += 1
		
		
	def button1(self):
		if self.next == 'start':
			self.printout("For a photo of your loved one press 1...", 'newline')
			self.next = 'start2'
		elif self.next == 'start2':
			centre_image = self.ids['centre_image']
			centre_image.source = "TemplatePic.png"
			self.printout("Your family will be acknowleged of your whereabouts. Press 1 to continue...", 'newline')
			self.next = 'start3'
		elif self.next == 'start3':
			self.newday()
			self.next = 'day1'
		elif self.next == 'day1':
			self.newdaystop()
			self
			self.next = 'day1a'
		elif self.next == 'day1a':
			pass
			
			
		else:
			self.button2()	
	def button2(self):
		if self.next == 'day1':
			self.newdaystop()
			self.printout("""*INCOMING TRANSMISSION*
			Stardate 67987, Day 1 as ca""", "")
			self.next = 'day1a'
		elif self.next == 'day1a':
			pass
			
		else:
			self.button3()	
	def button3(self):
		if self.next == 'day1':
			self.newdaystop()
			self.next = 'day1a'
		elif self.next == 'day1a':
			pass
			
			
		else:
			self.button4()	
	def button4(self):
		if self.next == 'day1':
			self.newdaystop()
			self.next = 'day1a'
		elif self.next == 'day1a':
			pass

		else:
			self.button1()	
	
	
class StartupGif(BoxLayout):
	
	def rungif(self, *args):
		gifid = self.ids['image_gif']
		button1 = self.ids['initiate_button']
		if gifid.source =='initiatestart.zip':
			button1.size = [0,0]
			MainGui.start = True
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
	
startupgif = StartupGif()
maingui = MainGui()		

if __name__ == "__main__":
	KivyStart().run()
	
	