import itertools
numlst = [80, 80, 56 ,80, 67, 80, 67, 90, 80, 56, 80,67,67]
keys = []
groups = []

for k,n in itertools.groupby(sorted(numlst)):  ## importnat to be sorted
    keys.append(k)
    groups.append(list(n))                       ##  be sure to make list of the subiterator because returns (key, sub-iterator)

def prtlst(lst):
    for i in lst:
        print i,
    print


###########################
#  count of each element: #
###########################
def count_per_group (groups):
        return (len(i) for i in groups)
prtlst(keys)
prtlst(groups)
prtlst(count_per_group(groups))

###############################
# represent count of elemens: #
###############################
def repr_coe(keys,countPG):
    zippedVals = dict(zip(keys,countPG))
    return zippedVals

prtlst(repr_coe(keys,count_per_group(groups)).items())



