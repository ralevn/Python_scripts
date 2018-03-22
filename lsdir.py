def lsdir(dir):
	import os
	dircont=[obj for obj in (os.walk(dir))]
	for i in (xrange(len(dircont))):
		for j in (xrange(len(dircont[i]))):
			print dircont[i][j]
lsdir ('/home/nikira/Work')
