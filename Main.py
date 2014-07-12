from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.properties import ListProperty
from kivy.properties import StringProperty
from kivy.properties import NumericProperty
from kivy.properties import ObjectProperty
from kivy.clock import Clock
from functools import partial
import time
import random

__version__ = '1.0'

class MainGui(BoxLayout, Image):
	capnum = 113
	button_pressed = 0
	start1 = False	
	next = 'start'
	day = 1
	postit = False
	news = ["Trans-Humanism: Augmentation in sport rife", "Google Sued:The major corporation has been sued by the human race for breach of trust", "Simpsons at 1020: starting season 1000 after 20 year haitus", "Fidel Castro Dead: Cuban Officials Announce death of leader hundreds of years after fall of the reigime"] 
	newson = True
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
			def addletter(self, letter, *args):
				self.tbt.text = self.tbt.text + letter
			if type == 'add':
				tbt.text = tbt.text + thetext
			elif type == 'newline':
				tbt.text = tbt.text + "\n captain%d@shipA113: %s" % (self.capnum, thetext)		
			elif type == 'typewriter':
				for i in range(0, len(thetext)):
					Clock.schedule_once(addletter, thetext[i-1, i], 0.1)
			else:
				tbt.text = thetext		
	def DailyMessage(self, news, message):
		
		if self.newson == True:
			text = """*INCOMING TRANSMISSION*
Stardate 437707.%d, Day %d
-DAILY BROADCAST-
%s
%s
*INSTRUCTIONS*
%s
""" % (self.day, self.day, news, self.news.pop(random.randint(0, len(self.news)-1)), message)
		elif self.newson == False:
			text = """*INCOMING TRANSMISSION*
Stardate 437707.%d, Day %d
-DAILY BROADCAST-
NEWS VOID
*INSTRUCTIONS*
%s
""" % (self.day, self.day, message)
		self.printout(text , "")		
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
	def newdaystop(self, huk):
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

	def inspect(self, type, onoff):
		tb1 = self.ids['textbox1']
		img = self.ids['centre_image']
		if onoff == True:
			tb1.foreground_color = [1, 1, 1, 0]
			tb1.disabled_foreground_color = [1, 1, 1, 0]
			img.source = 'inspect%s.png' % type
		else:
			tb1.foreground_color = [1, 1, 1, 1]
			if self.postit == False:
				img.source = 'TemplatePic.png'
			else:
				img.source = 'Templatepostit.png'
	def button1(self):
		if self.next == 'start':
			self.printout("For a photo of your loved one press 1...", 'typewriter')
			self.next = 'start2'
		elif self.next == 'start2':
			centre_image = self.ids['centre_image']
			centre_image.source = "TemplatePic.png"
			self.printout("Your family will be acknowleged of your whereabouts. Press 1 to continue...", 'newline')
			self.next = 'start3'
		elif self.next == 'start3':
			self.newday()
			Clock.schedule_once((self.newdaystop), 3)
		elif self.next == 'day1':
			self.newdaystop()
			self.DailyMessage("Smart Plague: An intelligent bug takes advantage of anti-biotics, no cure found", "Hello WOrld")
			self.next = 'day1a'
		elif self.next == 'day1a':
			self.inspect('planet1', True)
			
			
			
		else:
			pass
	def button2(self):
		if self.next == 'day1':
			self.newdaystop()
			self.DailyMessage("Smart Plague: An intelligent bug takes advantage of anti-biotics, no cure found", "Hello WOrld")
			self.next = 'day1a'
		elif self.next == 'day1a':
			pass
			
		else:
			pass	
	def button3(self):
		if self.next == 'day1':
			self.newdaystop()
			self.DailyMessage("Smart Plague: An intelligent bug takes advantage of anti-biotics, no cure found", "Hello WOrld")
			self.next = 'day1a'
		elif self.next == 'day1a':
			pass
			
			
		else:
			pass
	def button4(self):
		if self.next == 'day1':
			self.newdaystop()
			self.DailyMessage("Smart Plague: An intelligent bug takes advantage of anti-biotics, no cure found", "Hello WOrld")
			self.next = 'day1a'
		elif self.next == 'day1a':
			pass

		else:
			pass
	
	
class StartupGif(BoxLayout):
	
	def rungif(self, *args):
		gifid = self.ids['image_gif']
		gifid.source = 'initiatestart.zip'
		Clock.schedule_once((self.start), 2)
	def start(self, *args):
		gifid = self.ids['image_gif']
		button1 = self.ids['initiate_button']
		button1.size = [0,0]
		MainGui.start = True
		GameName().run()
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
	
	