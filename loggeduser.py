#!/bin/python2.7
def loguser(searchArg):
	import subprocess
	a = searchArg
	_awkParam = "/" + a + "/ {print $1 \" \" $6}"
	_p1 = subprocess.Popen (["cat","/etc/passwd"],stdout=subprocess.PIPE)
	_p2 = subprocess.Popen (["awk",_awkParam],stdin=_p1.stdout,stdout=subprocess.PIPE)
	pout = _p2.stdout.read()
	print (pout)

loguser('niki')
