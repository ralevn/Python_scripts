def profile (first, last,*countries,**sales):
    print first, last
    print countries
    print sales


profile('John','Smith','USA','UK','Germany',Mercedes=5,BMW=3,Audi=10)
