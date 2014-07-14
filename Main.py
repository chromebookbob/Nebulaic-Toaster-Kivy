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
from kivy.animation import Animation
from kivy.core.audio import SoundLoader
import time
import random

__version__ = '1.0'

class MainGui(BoxLayout, Image):
	capnum = 113
	black = False
	button_pressed = 0
	start1 = False	
	next = 'start'
	log = []
	day = 1
	event = ''
	postit = False
	news = ["Trans-Humanism: Augmentation in sport rife", "The Day After Tommorow: The True story of a father and son reunited in the blizzards of New Manhattan","Google Sued:The major corporation has been sued by the human race for breach of trust", "Simpsons at 1020: starting season 1000 after 20 year haitus", "Fidel Castro Dead: Cuban Officials Announce death of leader hundreds of years after fall of the reigime"] 
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
	def addletter(self, letter, *args):
		tbt = self.ids['textbox1']
		tbt.text = tbt.text + letter
	def printout(self, thetext, type, *args):
			tbt = self.ids['textbox1']
			thetext = " " + thetext + " " 
			
			if type == 'add':
				tbt.text = tbt.text + thetext
			elif type == 'newline':
				tbt.text = tbt.text + "\n captain%d@shipA113: %s" % (self.capnum, thetext)		
			elif type == 'typewriter':
				for i in range(0, len(thetext)):
					Clock.schedule_once(partial(self.addletter, thetext[i-1:i]), 0.1)
			else:
				tbt.text = thetext		
	def DailyMessage(self, news, message, *args):
		
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
	def newday(self, *args):
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
		if self.black == True:
			img.source = 'day0.png'
			self.black = False
		else:
			img.source = 'day%d.png' % self.day
	def newdaystop(self, *args):
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

	def inspect(self, type, onoff, *args):
		tb1 = self.ids['textbox1']
		img = self.ids['centre_image']
		if onoff == True:
			tb1.foreground_color = [1, 1, 1, 0]
			tb1.disabled_foreground_color = [1, 1, 1, 0]
			img.source = 'inspect%s.png' % type
		else:
			tb1.foreground_color = [0, 0, 0, 1]
			if self.postit == False:
				img.source = 'TemplatePic.png'
			else:
				img.source = 'Templatepostit.png'
	def jump(self, *args):
		self.printout("Preparing to jump, shutting down console...", "")
		self.black = True
		Clock.schedule_once(partial(self.inspect, 'dark', True), 0.1)
		Clock.schedule_once((self.newday), 1)
		Clock.schedule_once((self.newday), 2)
		Clock.schedule_once((self.newdaystop), 5)
		Clock.schedule_once(partial(self.printout, "Booting Up", ""), 5.1)
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
			self.DailyMessage("Smart Plague: An intelligent bug takes advantage of anti-biotics, no cure found", "Report any sightings\nMake no contact with alien bodies\nIf you fail to follow these orders you will be repremanded.")
			self.printout("Press Any Key To Inspect Snapshot...", 'newline')
			
			self.next = 'day1'
		elif self.next == 'day1':
			self.inspect('stars', True)
			Clock.schedule_once(partial(self.inspect, 'stars', False), 3)
			self.printout("Report What You Have Seen:\n1. Just Stars\n2. Planet \n3.Unidentified Object\n4.Alien Vessel", " ")
			self.next = 'day1a'
			
		elif self.next == 'day1a':
			self.printout("Just Stars:\nAny Key: Move On", "newline")
			self.next = 'jump'
		elif self.next == 'jump':
			self.jump()
			self.next = 'day2'
			self.button4()
		elif self.next == 'day2':
			Clock.schedule_once(partial(self.DailyMessage, "Smart Plague: Bug rampages through America in days.", "Report any sightings\nMake no contact with alien bodies\nIf you fail to follow these orders you will be repremanded."), 6)
		elif self.next == 'planet':
			printout('Sending signals...', 'newline')
			self.event = 'Sent signals to planet'
			if self.day < 4:
				printout('No reply recieved, logging event')
				self.log.append('day ' + 'self.day' + ': ' + self.event + ' None recieved') 
			else:
				int = random.randint(1, 5)
				if int == 1:
					printout('Incoming Transmission...')
				else:
					printout('No reply recieved, logging event')
					self.log.append('day ' + 'self.day' + ': ' + self.event + ' None recieved')
					printout('Press any key to jump...', 'newline')
					self.next = 'jump'	
			
		else:
			pass
	def button2(self):
		if self.next == 'day1':
			self.inspect('stars', True)
			Clock.schedule_once(partial(self.inspect, 'stars', False), 3)
			self.printout("Report What You Have Seen:\n1. Just Stars\n2. Planet \n3.Unidentified Object\n4.Alien Vessel", " ")
			self.next = 'day1a'
		elif self.next == 'day1a':
			self.printout("Planet Sighted, Choose Course Of Action:\n1.Send Contact Signals\n2.Move On\n3.Report\n4.Log Event", "newline")
			self.event = 'Planet Sighted'
			self.next == 'planet'
		elif self.next == 'jump':
			self.jump()
			self.next = 'day2'
			self.button4()
		elif self.next == 'day2':
			Clock.schedule_once(partial(self.DailyMessage, "Smart Plague: Bug rampages through America in days.", "Report any sightings\nMake no contact with alien bodies\nIf you fail to follow these orders you will be repremanded."), 6)
		elif self.next == 'planet':
			self.printout('Press any key to jump...', 'newline')
			self.next = 'jump'
			
		else:
			pass	
	def button3(self):
		if self.next == 'day1':
			self.inspect('stars', True)
			Clock.schedule_once(partial(self.inspect, 'stars', False), 3)
			self.printout("Report What You Have Seen:\n1. Just Stars\n2. Planet \n3.Unidentified Object\n4.Alien Vessel", " ")
			self.next = 'day1a'
		elif self.next == 'day1a':
			self.printout("Unidentified Object Sighted, Choose Course Of Action:\n1.Send Contact Signals\n2.Move On\n3.Report\n4.Log Event", "newline")
		elif self.next == 'jump':
			self.jump()
			self.next = 'day2'
			self.button4()
		elif self.next == 'day2':
			Clock.schedule_once(partial(self.DailyMessage, "Smart Plague: Bug rampages through America in days.", "Report any sightings\nMake no contact with alien bodies\nIf you fail to follow these orders you will be repremanded."), 6)
			
			
			
		else:
			pass
	def button4(self):
		if self.next == 'day1':
			self.inspect('stars', True)
			Clock.schedule_once(partial(self.inspect, 'stars', False), 3)
			self.printout("Report What You Have Seen:\n1. Just Stars\n2. Planet \n3.Unidentified Object\n4.Alien Vessel" "")
			self.next = 'day1a'
		elif self.next == 'day1a':
			self.printout("Alien Vessel Sighted, Choose Course Of Action:\n1.Send Contact Signals\n2.Move On\n3.Report\n4.Log Event" "newline")
		elif self.next == 'jump':
			self.jump()
			self.next = 'day2'
			self.button4()
		elif self.next == 'day2':
			Clock.schedule_once(partial(self.DailyMessage, "Smart Plague: Bug rampages through America in days.", "Report any sightings\nMake no contact with alien bodies\nIf you fail to follow these orders you will be repremanded."), 6)
		elif self.next == 'planet':
			self.log.append('day ' + 'self.day' + ': ' + self.event)
		
		else:
			pass
	
	
class StartupGif(BoxLayout):
	sound = ObjectProperty(None, allownone=True)

	def donothing(self, *args):
		pass
	def soundtrack(self, *args):
		self.sound = SoundLoader.load('soundtrack.wav')
		self.sound.loop = True
		self.sound.play()
	def rungif(self, *args):
		gifid = self.ids['image_gif']
		button1 = self.ids['initiate_button']
		gifid.source = 'initiatestart.zip'
		button1.on_press = self.start()
	def start(self, *args):
		self.soundtrack()
		gifid = self.ids['image_gif']
		button1 = self.ids['initiate_button']
		button1.size = [0,0]
		GameName().run()
	
class KivyStart(App):
	
	def build(self):
		return StartupGif()
		
class GameName(App):
	
	def build(self):
		return MainGui()

if __name__ == "__main__":
	KivyStart().run()
	
	