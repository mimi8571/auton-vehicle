#!/usr/bin/env python

import numpy as np
import time
import random

# controller module
class PID():
	def __init__(self, reference, sys_feedback):
		Kp = 0.0
		Ki = 0.0
		Kd = 0.0
		self._P = 0.0
		self._I = 0.0
		self._D = 0.0
		self.ref = reference
		self.error = self.ref - sys_feedback # from system feedback
		self.error_now = self.error
		self.error_prev = 0
		self.time_now = int(round(time.time() * 1000))
		self.time_prev = self.time_now
		self.controllerOutput()

	def controllerOutput(self, deltaError = 0, deltaTime = 0):
		self.getKd()
		self.getKi()
		self.getKp()

		deltaError = self.error_prev - self.error_now
		deltaTime = self.time_now - self.time_prev
		#print(self.Kp, self.error_now)
		self._P = self.Kp * self.error_now
		self._I += self.error * deltaTime

		if deltaTime > 0:
			self._D = self.Kd * deltaError / deltaTime
		else:
			self._D = 0

		self.error_prev = self.error_now
		self.time_prev = self.time_now
		controller = self._P + self._I + self._D

		return controller

	def getKp(self, gain_P = 0):
		gain_P = random.randint(0,30)
		self.Kp = gain_P

	def getKi(self, gain_I = 0):
		gain_I = random.randint(0,25)
		self.Ki = gain_I

	def getKd(self, gain_D = 0):
		gain_D = random.randint(0,15)
		self.Kd = gain_D

if __name__ == "__main__":
	pd = PID(5,3)
	print 'Final Output: ',pd.controllerOutput() 
