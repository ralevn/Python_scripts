def findsubstr (string, substring):
    findpos = []
    for i in xrange(len(string)):
        if string.find(substring,i,len(string)) != -1:
            findpos.append(string.find(substring,i,len(string)))
    hits = len(set(findpos))
    print hits

string='ABCDCDCDC'
substring='CDC'
findsubstr (string, substring)
