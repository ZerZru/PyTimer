__author__ = 'Elisey Sharov'

import time

class timer:
	def start():
		h = 0
		m = 0
		s = 0
		while True:
			s += 1
			if s >= 60:
				m += 1
				s = 0
			if m > 60:
				h += 1
				m = 0
				s = 0
			time.sleep(1)
			print('{}:{}:{}'.format(h, m, s))
