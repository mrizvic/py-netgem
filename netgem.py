#!/usr/bin/env python

import urllib
import urllib2
import time
import zlib
import os


class Netgem(object):
	'''
	Manipulate with NETGEM STB over IPv4
	'''

	def __init__(self,ip,delay=0.1,timeout=5):
		'''
		delay	- pause (in seconds) between HTTP requests
		timeout - sets timeout (in seconds) waiting for HTTP response
		'''
		self.url = '{3}{0}:{1}/{2}'.format(ip,'5678',zlib.decompress('x\x9c+J\xcd\xcd/I\xd5K\xce\xcf+)\xca\xcf\x01\x00*\xb6\x05\xbc'),zlib.decompress('x\x9c\xcb())\xb0\xd2\xd7\x07\x00\n\xd6\x02Y'))
		self.delay = delay
		self.timeout = timeout
		self.verbose = False
		self.tca = 'x\x9c\xb3IL.\xc9\xcc\xcfS\xc8K\xccM\xb5U\x02\x00&,\x04\xdb'
		self.udb = 'x\x9c\xb3\xd1OL.\xc9\xcc\xcf\xb3\x03\x00\x0e\xe5\x03('


	def __Request(self,url,values):
		headers={zlib.decompress('x\x9cs\xce\xcf+I\xcd+\xd1-\xa9,H\x05\x00\x1e\x98\x04\xcb'):zlib.decompress('x\x9cK,(\xc8\xc9LN,\xc9\xcc\xcf\xd3\xaf\xc8\xcd\x01\x001\x11\x06\x15'),zlib.decompress('x\x9c\x0b-N-\xd2uLO\xcd+\x01\x00\x14\x1b\x03\xbc'):zlib.decompress('x\x9cs,HL\xceH\xd5\xf5())p\xce\xc9L\xcd+\xd1\x0f\xf5s\x0cs\xf4\xf4qt\xf2qU\xd0\xc8J,KT0\xd43\xd1\x04\x00\x17\x9d\x0c\x88')}

		try:
			body = values
			time.sleep(self.delay)

			request = urllib2.Request(url,body,headers=headers)
			response = urllib2.urlopen(request,timeout=self.timeout)

			buffer = response.read()
			return buffer
		except Exception as e:
			raise(e)

	def connect(self):

		'''
		Prepare STB for communication
		'''

		url = self.url

		notconnected=True

		while(notconnected):
			try:
				print 'connecting... ',
				result = self.__Request(url,zlib.decompress('x\x9c\xb3IL.\xc9\xcc\xcfS\xc8K\xccM\xb5UJ\xce\xcf\xcbKM.Q\xb2\xb3\xd1\x87\x88\xdb\x01\x00\xbb\xf4\x0bL'))
			except Exception as e:
				print 'failed: ',e
			else:
				print 'success'
				notconnected=False
				# return result

	def get_volume(self):

		'''
		Read current volume setting
		'''

		values=zlib.decompress('x\x9c\xb3IL.\xc9\xcc\xcfS\xc8K\xccM\xb5UJO-\x89/\xcb\xcf)\xcdMU\xb2\xb3\xd1\x87H\xd9\x01\x00\xe4G\x0c\x99')

		url=self.url
		return self.__Request(url,values)

	def set_volume(self,volume=0):

		'''
		Set current volume (0..100)
		'''

		values=zlib.decompress(self.tca) + zlib.decompress('x\x9c+N-\x89/\xcb\xcf)\xcdMU\xb2\x03\x00 \x95\x04\xa4') + '{}'.format(volume) + zlib.decompress(self.udb)

		url=self.url
		return self.__Request(url,values)

	def volume_up(self):

		'''
		Volume up
		'''

		values=zlib.decompress('x\x9c\xb3IL.\xc9\xcc\xcfS\xc8K\xccM\xb5U*N\xcdK\x89\xcfN\xadT\xb2+\xcb\xcf)\xcdM\x8d/-\xb0\xd1\x87\xa8\xb0\x03\x00K\xd0\x0f\x90')

		url=self.url
		return self.__Request(url,values)

	def volume_down(self):

		'''
		Volume down
		'''

		values=zlib.decompress('x\x9c\xb3IL.\xc9\xcc\xcfS\xc8K\xccM\xb5U*N\xcdK\x89\xcfN\xadT\xb2+\xcb\xcf)\xcdM\x8dO\xc9/\xcf\xb3\xd1\x87\xa8\xb1\x03\x00m"\x10c')

		url=self.url
		return self.__Request(url,values)

	def send_key(self,key='OK'):

		'''

		Sends a key to the box. List of supported keys:
		* on_off
		* deep_sleep
		* channel_up
		* channel_down
		* volume_up
		* volume_down
		* prev
		* next
		* rec
		* play_pause
		* up
		* down
		* left
		* right
		* ok
		* back
		* narobase
		* fullscreen
		* delete
		* favorite
		* mute
		* red
		* green
		* yellow
		* blue
		* menu
		* 0, 1, 2, ..., 9
		'''

		values=zlib.decompress('x\x9c\xb3IL.\xc9\xcc\xcfS\xc8K\xccM\xb5U*N\xcdK\x89\xcfN\xadT\xb2\x03\x00l\xc3\x08\x8d')+key+zlib.decompress('x\x9c\xb3\xd1OL.\xc9\xcc\xcf\xb3\x03\x00\x0e\xe5\x03(')

		url=self.url
		return self.__Request(url,values)

	def zap(self,channel='11'):

		'''
		Zap to channel
		'''

		values=zlib.decompress(self.tca) + zlib.decompress('x\x9c\xabJ,P\xb2\x03\x00\x05\xbd\x01\xac') + '{}'.format(channel) + zlib.decompress(self.udb)

		url=self.url
		return self.__Request(url,values)

	def get_current_channel_id(self):

		'''
		Get currently active channel
		'''

		values=zlib.decompress(self.tca) + zlib.decompress('x\x9cKO-\x89O.-*J\xcd\x03\xd2\x19\x89yy\xa99\xf1\x99)Jv\x00{0\tg') + zlib.decompress(self.udb)

		url=self.url
		return self.__Request(url,values)

	def get_channel_list(self):

		'''
		Get channel list
		'''

		values=zlib.decompress('x\x9c\xb3IL.\xc9\xcc\xcfS\xc8K\xccM\xb5UJO-\x89O\xceH\xcc\xcbK\xcd\x89\xcf\xc9,.Q\xb2\xb3\xd1\x87(\xb0\x03\x00;\x88\x0e\xf5')

		url=self.url
		return self.__Request(url,values)

	def send_text(self, text):

		alphabet={
			'.':'11',
			'@':'12',
			'/':'13',
			'1':'14',
			'a':'21',
			'b':'22',
			'c':'23',
			'2':'24',
			'd':'31',
			'e':'32',
			'f':'33',
			'3':'34',
			'g':'41',
			'h':'42',
			'i':'43',
			'4':'44',
			'j':'51',
			'k':'52',
			'l':'53',
			'5':'54',
			'm':'61',
			'n':'62',
			'o':'63',
			'6':'64',
			'p':'71',
			'q':'72',
			'r':'73',
			's':'74',
			'7':'75',
			't':'81',
			'u':'82',
			'v':'83',
			'8':'84',
			'w':'91',
			'x':'92',
			'y':'93',
			'z':'94',
			'9':'95',
			' ':'01',
			'0':'02'
		}

		for letter in text:
			x=alphabet[letter]
			sendkey = x[0]
			sendtimes = int(x[1])
			if 'oldkey' in locals() and oldkey == sendkey:
				time.sleep(2)
			for i in xrange(sendtimes):
				self.send_key(sendkey)
			oldkey=sendkey


def main():
	stbip = os.environ.get('STB_IP')
	if stbip is None:
		raise ValueError('please set STB_IP environment variable')

	# pause 150ms between requests
	n=Netgem(ip=stbip,delay=0.15)

	# this blocking until connected
	n.connect()

	n.zap(239)
	# wait for STB to load content and settle down
	time.sleep(9)

	# go to search
	for x in range(4):
		n.send_key('down')

	# press OK
	n.send_key('ok')
	time.sleep(1)

	# search for your favourite movie :-)
	n.send_text('terminator')
	time.sleep(4)

	# volume showoff
	for x in xrange(30):
		n.volume_down()
	
	for x in xrange(30):
		n.volume_up()

	print n.get_volume()

if __name__=='__main__':
	main()
