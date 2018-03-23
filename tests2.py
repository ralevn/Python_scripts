import subprocess

def gatherStatus(pids):
        """ Returns dictionary with process parameters and their values"""
        pid = str(pids)
        str1 = 'Name|VmSize'
        str2 = '/proc/' + pid + '/status'
        p1 = subprocess.Popen(["grep", "-E", str1, str2], stdout=subprocess.PIPE)
        outstr = p1.stdout.read()
        output = (i.split(':\t') for i in outstr.split('\n')[:-1])
        return output


for i in gatherStatus(7971):
        print i
