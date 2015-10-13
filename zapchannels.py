import netgem
import time
import os

def main():
	stbip = os.environ.get('STB_IP')
	if stbip is None:
		raise ValueError('please set STB_IP environment variable')

	n=netgem.Netgem(ip=stbip)
	n.connect()

	chanlist=[1,2,3,4,6,7,100,102,104,106,109,110,111,201,206,208]

	while True:
		for chan in chanlist:
			print 'zapping to channel {0}'.format(chan)
			n.zap(chan)
			time.sleep(5)

if __name__ == '__main__':
	main()
