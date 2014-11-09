#!/usr/bin/env python

class Hello:	
	def __init__(self):
		self.str = "Hello World!"
	def print_str(self):
		print self.str

def main():
	demo = Hello()
	demo.print_str()

if __name__=='__main__':
	main()
