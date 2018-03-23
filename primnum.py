def primfact(e):
   for n in range(1, e+1):
      for x in range(2, n-1):
         if n % x == 0:
            break
      else:
         print n, 
primfact(29)