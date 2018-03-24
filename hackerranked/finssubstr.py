def count_substring(string, sub_string):
    hitpositions = []
    for i in xrange(len(string)):
        if string.find(sub_string,i,len(string)) != -1:
            hitpositions.append(string.find(sub_string,i,len(string)))
        hitnums = len(set(hitpositions))
    return hitnums
