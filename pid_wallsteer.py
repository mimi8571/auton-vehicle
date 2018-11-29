#!/usr/bin/env python

import numpy as np
import time
import random

# controller module
class PID_steer():
	def __init__(self, reference, sys_feedback):
		self.Kp = 0.06
		self.Ki = 0.001
		self.Kd = 0.03
		self._P = 0.1
		self._I = 0.1
		self._D = 0.1
		self.ref = reference
		self.error = self.ref - sys_feedback 
		self.error_now = self.error
		self.error_prev = 0.
		self.time_now = time.time() * 1000;
		self.time_prev = 0.0
		self.controllerOutput()

	def controllerOutput(self):
		self.deltaError = self.error_now - self.error_prev
		self.deltaTime = self.time_now - self.time_prev
		print(self.deltaError, self.deltaTime)

		self._P = self.Kp * self.error_now
		self._I += self.error * self.deltaTime

		if self.error_now != 0:
			self._D += self.Kd * self.deltaError / self.deltaTime

		print('P,I,D: ', self._P, self._I, self._D)

		self.error_prev = self.error_now
		self.error_now += self.deltaError
		self.time_prev = self.time_now
		controller = self._P + self._I + self._D
		print(controller)

		return controller

if __name__ == "__main__":
	response = 90.
	n = 0
	while n < 6: #system on
		steer = 45.; # get input angle from robot
		if steer != 90:
			pd = PID_steer(steer, response)
			response = pd.controllerOutput()
		else:
			response = 0
		n += 1
		print('Final Out: ', response, '# Times: ', n)




