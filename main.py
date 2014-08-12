from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.properties import ListProperty
from kivy.properties import StringProperty
from kivy.uix.image import Image
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
	planetgood = False
	aliengood = False
	ufogood = False
	reportevents = False
	logevents = False
	contact = False
	moveon = False
	score = 0
	button_pressed = 0
	typelib = ['stars', 'stars', 'stars', 'planet', 'planet', 'ufo', 'alien']
	type = typelib[0]
	dark = False
	start1 = False	
	next = 'start'
	log = []
	op = 0
	day = 0
	report = ''
	event = ''
	temp = 'day1a'
	postit = False
	news = ["Trans-Humanism: Augmentation in sport rife", "The Day After Tommorow: The True story of a father and son reunited in the blizzards of New Manhattan","Google Sued:The major corporation has been sued by the human race for breach of trust", "Simpsons at 1020: starting season 1000 after 20 year haitus", "Fidel Castro Dead: Cuban Officials Announce death of leader hundreds of years after fall of the reigime"] 
	newson = True
	textboxtext = """Welcome Captain %d, you have been woken from cryosleep to control this ship.
You will receive instructions on a daily basis outlining your course of action. You have a computer terminal, and four keys.
These instructions must be followed. Any deviation will be noted, failure to comply will result in your demise. You hold the fate of your race in your hands.
Good luck Captain. \n captain%d@shipA113: Take Command, Press 1""" % (capnum, capnum)
	
			
	def flicker(self, *args):
		self.op = 0.4
		Clock.schedule_once(partial(self.opaque, 0), 0.1)
		Clock.schedule_once(partial(self.opaque, 0.6), 6)
		Clock.schedule_once(partial(self.opaque, 0), 6.1)
	def opaque(self, opacity, *args):
		self.op = opacity
	
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
	def DailyMessage(self, *args):
		replyreport = ''
		if self.report == 'planet':
			report = True
			reply = ['You followed orders. Well done. We are investigating the viability of sustaining life on the planet you found. Congratulations Captain', 'The report you filed on the recently discovered planet was unauthorised, take greater care in reading instructions from earth', 'NsjdaboINSasb nasjdo knn. AJDsij, njoni asdasd injn .......\n MESSAGE NOT DECRYPTED', 'The planet you reported does not exist. If you fail to report accurately you jeopardise the mission\'s aim to find a new planet earth.']
			if self.reportevents == True:
				replyreport = reply[0]
			else:
				replyreport = reply[random.randint(1,3)]
		else:
			report = False	
		news = ["Smart Plague: An intelligent bug takes advantage of anti-biotics, no cure found", "Smart Plague: Bug rampages through America in days.", "Plague takes 16 million lives", 'Vaccines for Plague found: Wealthy to recieve treatment first', 'First Vaccine Shipment Hijacked: A vaccine shipment to africa was hijacked, shots turning up on the black market']
		report = ["Report any sightings\nMake no contact with alien bodies\nIf you fail to follow these orders you will be repremanded.", "Report any sightings\nMake no contact with alien bodies\nIf you fail to follow these orders you will be repremanded.", "Report any sightings\nMake no contact with alien bodies\nIf you fail to follow these orders you will be repremanded.", 'You will be out of transmit distance for 3 days. Do not report sightings. Log all events. Make no contact. Follow orders.', 'You will be out of transmit distance for 2 days. Do not report sightings. Log all events. Make no contact. Follow orders.', 'You will be out of transmit distance for day. Do not report sightings. Log all events. Make no contact. Follow orders.']
		if self.day <= 3:
			self.reportevents = True
			self.logevents = False
			self.contact = False
			self.moveon = False
		elif 4 <= self.day >= 6:
			self.reportevents = False
			self.logevents = True
			self.contact = False
			self.moveon = False
				
		if report == True:
			replyrep = 'MESSAGE RECIEVED FROM EARTH\n %s' % replyreport
		else:
			replyrep = ''
		if self.newson == True:
			text = """*INCOMING TRANSMISSION*
Stardate 437707.%d, Day %d
-DAILY BROADCAST-
%s
%s
*INSTRUCTIONS*
%s
%s

""" % (self.day, self.day, news[self.day - 1], self.news.pop(random.randint(0, len(self.news)-1)), report[self.day-1], replyrep)
		elif self.newson == False:
			text = """*INCOMING TRANSMISSION*
Stardate 437707.%d, Day %d
-DAILY BROADCAST-
NEWS VOID
*INSTRUCTIONS*
%s
""" % (self.day, self.day, report(self.day - 1))
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
			self.day += 1
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
		

	def inspect(self, onoff, *args):
		tb1 = self.ids['textbox1']
		img = self.ids['centre_image']
		type = 'stars'
		lib = ['stars2', 'stars3', 'stars4', 'planet1', 'planet2', 'ufo', 'alien']
		
		if self.day < 3:
			type = 'stars'
			if self.dark == True:
				type = 'dark'
				self.dark = False
		elif self.dark == True:
			type = 'dark'
			self.dark = False
		else:
			rand = random.randint(0, len(lib) -1 )
			type = lib[rand]
			self.type = self.typelib[rand]
			
					
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
		self.dark = True
		self.next = 'newday'
		Clock.schedule_once(partial(self.inspect, True), 0.1)
		Clock.schedule_once((self.newday), 1)
		Clock.schedule_once((self.newday), 2)
		Clock.schedule_once((self.newdaystop), 5)
		Clock.schedule_once(partial(self.printout, "Booting Up", ""), 5.1)
		Clock.schedule_once(partial(self.printout, "Press any key to log in", "newline"), 7)
	def button1(self, *args):
		if self.next == 'start':
			self.printout("For a photo of your loved one press 1...", 'typewriter')
			self.next = 'start2'
			Clock.schedule_interval((self.flicker), 9)
		elif self.next == 'start2':
			centre_image = self.ids['centre_image']
			centre_image.source = "TemplatePic.png"
			self.printout("Your family will be acknowleged of your whereabouts. Press 1 to continue...", 'newline')
			self.next = 'start3'
		elif self.next == 'start3':
			self.newday()
			Clock.schedule_once((self.newdaystop), 3)
			self.DailyMessage()
			self.printout("Press Any Key To Inspect Snapshot...", 'newline')
			self.next = 'day1'
		elif self.next == 'newday':
			self.DailyMessage()
			self.next = 'day1'
			self.printout("Press Any Key To Inspect Snapshot...", 'newline')
			self.next = 'day1'
		elif self.next == 'day1':
			self.inspect( True)
			Clock.schedule_once(partial(self.inspect, False), 3)
			self.printout("Report What You Have Seen:\n1. Just Stars\n2. Planet \n3.Unidentified Object\n4.Alien Vessel", " ")
			self.next = 'day1a'
			
		elif self.next == 'day1a':
			self.printout("Just Stars:\nAny Key: Move On", "newline")
			self.next = 'jump'
		elif self.next == 'jump':
			self.jump()
			
		elif self.next == 'planet':
			self.printout('Sending signals...', 'newline')
			self.event = 'Sent signals to planet'
			if self.contact == False:
				self.planetgood = True
				self.score += 1
			else:
				self.planetgood = False
				self.score -= 1
			if self.day < 4:
				self.printout('No reply recieved, logging event', 'newline')
				self.log.append('day ' + 'self.day' + ': ' + self.event + ' None recieved') 
				self.printout('Press any key to jump...', 'newline')
				self.next = 'jump'
			else:
				int = random.randint(1, 5)
				if int == 1:
					self.printout('Incoming Transmission...', 'newline')
				else:
					self.printout('No reply recieved, logging event', 'newline')
					self.log.append('day ' + 'self.day' + ': ' + self.event + ' None recieved')
					self.printout('Press any key to jump...', 'newline')
					self.next = 'jump'	
		elif self.next == 'ufo':
			if self.contact == False:
				self.ufogood = True
				self.score += 1
			else:
				self.ufogood = False
				self.score -= 1
			self.printout('Sending signals...', 'newline')
			self.event = 'Sent signals to planet'
			if self.day < 4:
				self.printout('No reply recieved, logging event', 'newline')
				
				self.log.append('day ' + 'self.day' + ': ' + self.event + ' None recieved') 
				self.printout('Press any key to jump...', 'newline')
				self.next = 'jump'	
			
			else:
				int = random.randint(1, 5)
				if int == 1:
					self.printout('Incoming Transmission...', 'newline')
				else:
					self.printout('No reply recieved, logging event', 'newline')
					self.log.append('day ' + 'self.day' + ': ' + self.event + ' None recieved')
					self.printout('Press any key to jump...', 'newline')
					self.next = 'jump'	
		elif self.next == 'alien':
			if self.contact == False:
				self.aliengood = True
				self.score += 1
			else:
				self.aliengood = False
				self.score -= 1
			self.printout('Sending signals...', 'newline')
			self.event = 'Sent signals to planet'
			if self.day < 4:
				self.printout('No reply recieved, logging event', 'newline')
				self.log.append('day ' + 'self.day' + ': ' + self.event + ' None recieved') 
				self.printout('Press any key to jump...', 'newline')
				self.next = 'jump'	
			else:
				int = random.randint(1, 5)
				if int == 1:
					self.printout('Incoming Transmission...', 'newline')
				else:
					self.printout('No reply recieved, logging event', 'newline')
					self.log.append('day ' + 'self.day' + ': ' + self.event + ' None recieved')
					self.printout('Press any key to jump...', 'newline')
					self.next = 'jump'				
		else:
			pass
	def button2(self, *args):
		if self.next == 'day1':
			self.inspect( True)
			Clock.schedule_once(partial(self.inspect, False), 3)
			self.printout("Report What You Have Seen:\n1. Just Stars\n2. Planet \n3.Unidentified Object\n4.Alien Vessel", " ")
			self.next = 'day1a'
		elif self.next == 'day1a':
			self.event = 'Planet Sighted'
			self.next = 'planet'
			print(self.next)
			self.printout("Planet Sighted, Choose Course Of Action:\n1.Send Contact Signals\n2.Move On\n3.Report\n4.Log Event", "newline")
			
		elif self.next == 'jump':
			self.jump()
			self.next = 'newday'
			Clock.schedule_once(self.button4, 6)
		elif self.next == 'planet':
			self.printout('Press any key to jump...', 'newline')
			self.next = 'jump'
		elif self.next == 'ufo':
			self.printout('Press any key to jump...', 'newline')
			self.next = 'jump'
		elif self.next == 'alien':
			self.printout('Press any key to jump...', 'newline')
			self.next = 'jump'
		elif self.next == 'newday':
			self.DailyMessage()
			self.next = 'day1'
			self.printout("Press Any Key To Inspect Snapshot...", 'newline')
			self.next = 'day1'
		else:
			pass	
	def button3(self, *args):
		if self.next == 'day1':
			self.inspect( True)
			Clock.schedule_once(partial(self.inspect, False), 3)
			self.printout("Report What You Have Seen:\n1. Just Stars\n2. Planet \n3.Unidentified Object\n4.Alien Vessel", " ")
			self.next = 'day1a'
		elif self.next == 'day1a':
			self.next = 'ufo'
			self.event = 'Unidentified Object Sighted'
			self.printout("Unidentified Object Sighted, Choose Course Of Action:\n1.Send Contact Signals\n2.Move On\n3.Report\n4.Log Event", "newline")
		elif self.next == 'jump':
			self.jump()
			self.next = 'newday'
			
		elif self.next == 'newday':
			self.DailyMessage()
			self.next = 'day1'
			self.printout("Press Any Key To Inspect Snapshot...", 'newline')
			self.next = 'day1'
		elif self.next == 'planet':
			if self.reportevents == True:
				self.planetgood = True
				self.score += 1
				
			else:
				self.planetgood = False
				self.score -= 1
			self.printout("Reporting event to earth. Expect response in next broadcast.", "newline")
			self.report = 'planet'
			self.printout("Press any key to move on...", 'newline')
			self.next = 'jump'			
		elif self.next == 'ufo':
			self.printout("Reporting event to earth. Expect response in next broadcast.", "newline")
			self.printout("Press any key to move on...", 'newline')
			self.next = 'alien'			
		elif self.next == 'planet':
			self.printout("Reporting event to earth. Expect response in next broadcast.", "newline")
			self.printout("Press any key to move on...", 'newline')
			self.next = 'jump'			
		else:
			pass
	def button4(self, *args):
		if self.next == 'day1':
			self.inspect( True)
			Clock.schedule_once(partial(self.inspect,  False), 3)
			self.printout("Report What You Have Seen:\n1. Just Stars\n2. Planet \n3.Unidentified Object\n4.Alien Vessel", "")
			self.next = 'day1a'
		elif self.next == 'day1a':
			self.next = 'alien'
			self.event = 'Alien Craft Sighted'
			self.printout("Alien Vessel Sighted, Choose Course Of Action:\n1.Send Contact Signals\n2.Move On\n3.Report\n4.Log Event", "newline")
		elif self.next == 'jump':
			self.jump()
			self.next = 'newday'
			Clock.schedule_once(self.button1, 6)
		elif self.next == 'planet':
			self.log.append('Day ' + str(self.day) + ': ' + self.event)
			self.printout('Event Logged: %s' % self.log[len(self.log) - 1], 'newline') 
			self.printout("Press any key to move on...", 'newline')
			self.next = 'jump'			
		elif self.next == 'ufo':
			self.log.append('Day ' + str(self.day) + ': ' + self.event)
			self.printout('Event Logged: %s' % self.log[len(self.log) - 1], 'newline') 
			self.printout("Press any key to move on...", 'newline')
			self.next = 'jump'
		elif self.next == 'alien':
			self.log.append('Day ' + str(self.day) + ': ' + self.event)
			self.printout('Event Logged: %s' % self.log[len(self.log) - 1], 'newline') 
			self.printout("Press any key to move on...", 'newline')
			self.next = 'jump'			
			
		elif self.next == 'newday':
			self.DailyMessage()
			self.printout("Press Any Key To Inspect Snapshot...", 'newline')
			self.next = 'day1'
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
	
	