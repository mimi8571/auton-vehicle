#!/usr/bin/env python

import numpy as np
import time
import random
import sys

# controller module
class PID_steer():
	def __init__(self, reference, sys_feedback):
		Kp = 0.05
		Ki = 0.01
		Kd = 0.02
		self._P = 0.1
		self._I = 0.1
		self._D = 0.1
		self.ref = reference
		self.error = self.ref - sys_feedback # from system feedback
		self.error_now = self.error
		self.error_prev = 0;
		self.time_now = int(round(time.time() * 1000))
		self.time_prev = self.time_now
		self.controllerOutput()

	def controllerOutput(self, deltaError = 0, deltaTime = 0):
		deltaError = self.error_prev - self.error_now
		deltaTime = self.time_now - self.time_prev
		
		self._P = self.Kp * self.error_now
		self._I += self.error * deltaTime

		if deltaError > 0:
			self._D += self.Kd * deltaError / deltaTime
		else:
			self._D = 0
		print('P,I,D: ', self._P, self._I, self._D)

		self.error_prev += self.error_now
		self.time_prev = self.time_now
		controller = self._P + self._I + self._D

		return controller

if __name__ == "__main__":
	ideal_steer = 90
	while True: #system on
		steer = raw_input(); # get input angle
		feedback = 1;
		pd = PID_steer(steer, ideal_steer)
		print('Final Out: ', pd.controllerOutput())




