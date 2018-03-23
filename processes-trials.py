
def getInfo():
        """ get input for processes """
        # Need to decide if processes will be searched or pids will be given from user.
        # If it will return list of pids or key to filter
        pass


def pidsList(searchArg):
        """ Returns a list with the pids"""
        # below I filter for ssh processes but this shall be an entry from user getInfo:
        import subprocess
        a = searchArg
        _awkParam = "/" + a + "/ {print $2}"
        _ps1 = subprocess.Popen(["ps","-ef"],stdout=subprocess.PIPE)
        _ps2 = subprocess.Popen(["awk",_awkParam],stdin=_ps1.stdout,stdout=subprocess.PIPE)
        ps = _ps2.stdout.read().split('\n')[:-1]
        return pss
	
	
def loguser(searchArg):
	import subprocess
	a = searchArg
	_awkParam = " -F \":\" \'/" + a + "/ {print $1 \" \" $6}\'"
	_p1 = subprocess.Popen (["cat","/etc/passwd"],stdout=subprocess.PIPE)
	_p2 = subprocess.Popen (["awk",_awkParam],stdin=_p1.stdout,stdout=subprocess.PIPE)
	pout = _p2.stdout.read()
	print (pout)
	
#Converting string to dictionary
string = "abc=123,xyz=456"
dict(x.split('=') for x in string.split(','))

#In cases when when there is delimiter at the end of the string:
string = "abc: 123\nxyz: 456\n"
print (string)
dict(i.split(':') for i in string.split('\n')[:-1])

def gatherData(pids):
	import subprocess
	str1 = 'Name|VmSize|VmRSS'
	str2 = '/proc/' + pids + '/status'
	p1 = subprocess.Popen(["grep","-E",str1,str2],stdout=subprocess.PIPE)
	outstr = p1.stdout.read()
	outdic = dict(i.split(':\t') for i in outstr.split('\n')[:-1])
	return outdic

	

