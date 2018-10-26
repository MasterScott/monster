#!/usr/bin/python

# _   .-')                     .-') _   .-')    .-') _     ('-.  _  .-')   
#( '.( OO )_       v1.0      ( OO ) ) ( OO ). (  OO) )  _(  OO)( \( -O )  
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
import os


def gpiosetup():
  GPIO.setmode(GPIO.BCM)

  # init list with GPIO numbers
  pinList = [14, 15, 18, 23]

  # loop through pins and set mode and state to 'high'
  for i in pinList: 
    GPIO.setup(i, GPIO.OUT) 
    GPIO.output(i, GPIO.HIGH)


def openLid():
  try:
    gpiosetup()
    print("")
    print("Test One: Jumping relay one.")
    print("     [+] Up and Down")
    GPIO.output(14, GPIO.LOW)
    GPIO.output(14, GPIO.HIGH)
    time.sleep(2)
    GPIO.output(14, GPIO.LOW)
    GPIO.output(14, GPIO.HIGH)
    time.sleep(2)
    GPIO.output(14, GPIO.LOW)
    GPIO.output(14, GPIO.HIGH)
    time.sleep(2)
    print("     [+] Jumping relay one.")

    for i in range(60):
      GPIO.output(14, GPIO.LOW)
      time.sleep(randTime())

      GPIO.output(14, GPIO.HIGH)
      time.sleep(randTime())
  # End program cleanly with keyboard
  except KeyboardInterrupt:
    print "  Quit"

def smoke():
  try:
    gpiosetup()
    print("")
    print("Turning on fog machine")
    print("     [+] Fog on")
    GPIO.output(15, GPIO.LOW)
    time.sleep(15)
    GPIO.output(15, GPIO.HIGH)
    print("     [+] Fog off")
  # End program cleanly with keyboard
  except KeyboardInterrupt:
    print "  Quit"


def seckc():
	smoke()
	print("     [+] Playing Interrupt")
	pygame.mixer.music.stop()
	pygame.mixer.music.load("audio/Monster-scream.mp3")
	pygame.mixer.music.play(1)
	openLid()
	#minwait(1)
	startmusic()

def randTime():
  timeDelay = random.uniform(0.01, 0.5)
  return(timeDelay)


def getrandom():
	rand = random.randint(1,10111)
	return rand

def randt():
	i = 1
	while True:
		i = getrandom()
		if i < 230:
			print(str(i) + " is lower than 230!")
			seckc()
		else:
			time.sleep(2)

def minwait(min):
	time.sleep(min*30)


def startmusic():
	print("     [+] Playing background sound")
	pygame.mixer.music.load("audio/monster-sleeping.mp3")
	pygame.mixer.music.play(-1)
	minwait(1)
  	seckc()


if __name__ == "__main__": # execute only if run as a script
	try:
		os.system("cat monster.txt") #Set Raspi Audio Output all the way up
		print("[+] Adjusting RaspberryPi Audio volume to 100%\n")
		os.system("amixer sset PCM,0 200%") #Set Raspi Audio Output all the way up
		gpiosetup()
		pygame.mixer.init()
		print("\n[+] Starting Sound Test:")
		print("     [+] Starting Music")
		startmusic()
		# End program cleanly with keyboard

	except KeyboardInterrupt: 
		GPIO.cleanup()
		print("\n[--EXIT--] Testing complete")
		print("    Find more information about this project at")
		print("    https://github.com/hevnsnt/monster")
		print("")