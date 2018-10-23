#!/usr/bin/env python

import numpy as np
import time
import random

# controller module
class PID_steer():
	def __init__(self, reference, sys_feedback):
		self.Kp = 0.05
		self.Ki = 0.01
		self.Kd = 0.02
		self._P = 0.1
		self._I = 0.1
		self._D = 0.1
		self.ref = reference
		self.error = self.ref - sys_feedback 
		self.error_now = self.error
		self.error_prev = 0.
		self.time_now = int(round(time.time() * 1000));
		self.time_prev = self.time_now
		self.controllerOutput()

	def controllerOutput(self, deltaError = 0, deltaTime = 0):
		deltaError = self.error_now - self.error_prev
		deltaTime = self.time_now - self.time_prev
		print(deltaError, deltaTime)

		self._P = self.Kp * self.error_now
		self._I += self.error * deltaTime

		if self.error_now > 0:
			self._D += self.Kd * deltaError / deltaTime
		else:
			self._D = 0

		print('P,I,D: ', self._P, self._I, self._D)

		self.error_now += deltaError
		self.time_prev = self.time_now
		controller = self._P + self._I + self._D
		print(controller)

		return controller

if __name__ == "__main__":
	response = 90
	while True: #system on
		steer = 45; # get input angle
		pd = PID_steer(steer, response)
		response = pd.controllerOutput()
		print('Final Out: ', response)




