import random

g = random.randint(1,10)
f = random.randint(1,10)
print("galatasaray"+str(g))
print("fenerbahce"+str(f))
if g>f:
    print("galatasaray galip")
elif g<f:
    print("fener galip")
else:
    print("berabere")