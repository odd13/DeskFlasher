#!/usr/bin/env python3

import time
import os

class DeskLight:
	"""A simple desklight class for pwm led strips"""

	def __init__(self):
		self.STEP = 30
		self.DELAY = 0.002
		self.pin = 0

	def dim_up_and_down(self):
		self.turn_up()
		self.turn_down()

	def turn_up(self):
		for j in range(1, 6000, self.STEP):
			cmd = "echo " + str(self.pin) + "=" + str(j) + " > /dev/servoblaster"
			os.system(cmd)
			time.sleep(self.DELAY)

	def turn_down(self):
		for j in range(6000, 1, (self.STEP*-1)):
			cmd = "echo " + str(self.pin) + "=" + str(j) + " > /dev/servoblaster"
			os.system(cmd)
			time.sleep(self.DELAY)

	def flash(self, flashes, seconds):
		for j in range(1,flashes,1):
			self.turn_on()
			time.sleep(seconds)
			self.turn_off()
			time.sleep(seconds)

	def light_power(self, p):
		cmd = "echo " + str(self.pin) + "=" + str(p) + " > /dev/servoblaster"
		os.system(cmd)

	def turn_on(self):
		self.light_power("100%")

	def turn_off(self):
		self.light_power("0")
