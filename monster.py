#!/usr/bin/python

# _   .-')                     .-') _   .-')    .-') _     ('-.  _  .-')   
#( '.( OO )_                 ( OO ) ) ( OO ). (  OO) )  _(  OO)( \( -O )  
# ,--.   ,--.).-'),-----. ,--./ ,--,' (_)---\_)/     '._(,------.,------.  
# |   `.'   |( OO'  .-.  '|   \ |  |\ /    _ | |'--...__)|  .---'|   /`. ' 
# |         |/   |  | |  ||    \|  | )\  :` `. '--.  .--'|  |    |  /  | | 
# |  |'.'|  |\_) |  |\|  ||  .     |/  '..`''.)   |  |  (|  '--. |  |_.' | 
# |  |   |  |  \ |  | |  ||  |\    |  .-._)   \   |  |   |  .--' |  .  '.' 
# |  |   |  |   `'  '-'  '|  | \   |  \       /   |  |   |  `---.|  |\  \  
# `--'   `--'     `-----' `--'  `--'   `-----'    `--'   `------'`--' '--' 
#                                                                 IN A BOX          
#
# Find more information about this project at
# https://github.com/hevnsnt/monster
# 
import pygame
import random
import RPi.GPIO as GPIO
import time
import os, sys


def gpiosetup():
  '''Setup the GPIO pins, note this is written to support 4 relays on pins 14, 15, 18, and 23 of Raspi.
  However, you do not need to have a 4 relay board. If you only want to lift lid, connect just pin 14,
  if you want two 14 & 15 and so on. '''

  GPIO.setmode(GPIO.BCM)
  pinList = [14, 15, 18, 23] # These are the connected Raspi GPIO pins
  # See https://github.com/hevnsnt/monster/blob/master/images/pi3_gpio.png for pinout
  # Edit this if your setup is different.

  # Loop through pins and set mode and state to 'HIGH' as Relays move from NC to NO when moved 'LOW' 
  for i in pinList: 
    GPIO.setup(i, GPIO.OUT) 
    GPIO.output(i, GPIO.HIGH)


def openLid():
  ''' This assumes the lid actuators are on GPIO 14, edit below to match your setup'''
  try:
    gpiosetup()
    print("")
    print("Jumping the Lid (Relay 1)")
    print("     [+] Jumping Lid")
    for i in range(60):
      GPIO.output(14, GPIO.LOW)
      time.sleep(randTime())

      GPIO.output(14, GPIO.HIGH)
      time.sleep(randTime())
  # End program cleanly with keyboard
  except KeyboardInterrupt:
    print "  Quit"

def smoke():
  ''' This assumes the smoke machine is on GPIO 15, edit below to match your setup'''
  try:
  	if nosmoke is True:
  		print("     [-] Skipping Smoke")
  	else:
	    print("")
	    print("Adding some smoke to the box:")
	    print("     [+] Fog on")
	    GPIO.output(15, GPIO.LOW)
	    time.sleep(15)
	    GPIO.output(15, GPIO.HIGH)
	    print("     [+] Fog off")
	  # End program cleanly with keyboard
  except KeyboardInterrupt:
    print "  Quit"


def monsterscream():
	smoke()
	print("     [+] Monster is ANGRY")
	pygame.mixer.music.stop()
	pygame.mixer.music.load("audio/Monster-scream.mp3")
	pygame.mixer.music.play(1)
	time.sleep(1.5)
	openLid()
	

def randTime():
  '''This function returns a random time'''
  timeDelay = random.uniform(0.01, 0.5)
  return(timeDelay)

def minwait(min):
	time.sleep(min*30)


def startmusic():
	print("     [+] Monster is sleeping")
	pygame.mixer.music.load("audio/monster-sleeping.mp3")
	pygame.mixer.music.play(-1)
	minwait(1)
	print("     [+] Waking up Monster")
  	monsterscream()
  	halloween()

def mouth(opentime):
  '''This function moves the mouth up and down'''
  GPIO.output(14, GPIO.LOW)
  time.sleep(opentime)
  GPIO.output(14, GPIO.HIGH)
  time.sleep(0.1)


def halloween():
  time.sleep(1)
  pygame.mixer.music.stop()
  pygame.mixer.music.load("audio/Happy_Halloween.mp3")
  pygame.mixer.music.play(1)
  time.sleep(2)
  print("     [+] Happy Halloween")
  mouth(.353)
  mouth(.286)
  mouth(.329)
  mouth(.351)
  mouth(.873)
  mouth(.290)
  mouth(.241)
  mouth(.291)
  mouth(.230)
  mouth(2.334)
  time.sleep(1)
  snore()
  

def snore():
  print("     [+] Monster going to sleep")
  pygame.mixer.music.stop()
  pygame.mixer.music.load("audio/SNORE003.wav")
  pygame.mixer.music.play(-1)
  minwait(2)
  startmusic()



if __name__ == "__main__": # execute only if run as a script
	try:
		os.system('cls' if os.name == 'nt' else 'clear')
		os.system("cat monster.txt") # This is the easist way I know how to do this. CHANGE MY MIND
		nosmoke = False
		if len(sys.argv) > 1: 
				if sys.argv[1] == "-s":
					print("[-] Smoke mode: [DISABLED] ")
					nosmoke = True
		else:
			print("[+] Smoke mode: [ENABLED] (Disable with -s)")
		print("[+] Adjusting RaspberryPi Audio volume to 100%\n") #Set Raspi Audio Output all the way up
		os.system("amixer sset PCM,0 200%") #Set Raspi Audio Output all the way up
		gpiosetup() #Setup the GPIO pins
		pygame.mixer.init()
		print("Everything appears correct!")
		print("\n[+] Monster in a box is online")
		startmusic()
		# End program cleanly with keyboard

	except KeyboardInterrupt: 
		GPIO.cleanup()
		print("\n[--EXIT--] Monster in a box complete")
		print("    Find more information about this project at")
		print("     [[ https://github.com/hevnsnt/monster ]]")
		print("")
