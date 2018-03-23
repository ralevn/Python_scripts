class Staff:
"""  Students and Teachers form the Staff of a School   """
    annual_fee = 2000.00 ## class variable valid for all instances
    staff_num = 0

    def __init__(self, fname, lname, gender):
        self.fname = fname  ## instance variable
        self.lname = lname
        self.gender = gender
        self.email = fname + '.' + lname + '@school.com'
        Staff.staff_num += 1

    def full_info (self):  ## regular method applies on instances
        return '==> %s %s:  %s - %s' %(self.fname,self.lname,self.gender,self.email)

    def fullname (self):
        return "{} {}" .format(self.fname,self.lname)

    @classmethod       ## decorator saying a class methods (applying to whole class) follow
    def set_fee (cls,amount):
        cls.annual_fee = amount

    @staticmethod      ## decorator saying a static methods (applying to whole class but taking no parameters) follow
    def is_work_day(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
## special methods:
    def __repr__(self):
        return "{} {}: {}".format(self.fname, self.lname,self.email)
    def __str__(self):
        return '{}' " mail: " '{}'.format(self.fullname(), self.email)
    def __len__(self):
        return len(self.fullname())



class Students(Staff):
    def __init__(self, fname, lname, gender,wave,BY):
        Staff.__init__(self,fname,lname,gender)   ## initialize the parent attributes from parent init method
        self.BY = BY
        self.wave = wave

    def pers_fee(self):
            return Staff.annual_fee * (1 - self.wave)
    def stud_info (self):  ## regular method applies on instances
        return '==> %s %s:  %s - %s  - %i, fee:  %d' %(self.fname,self.lname,self.gender,self.email,self.BY,self.pers_fee())
    def __add__(self, other): ## this special method will help represnt sum of two students fees with print (stud1 + stud2)
        return self.pers_fee() + other.pers_fee()

class Teachers(Staff):
    def __init__(self, fname, lname, gender,subject):
        Staff.__init__(self,fname,lname,gender)
        self.subject = subject
    def teac_info (self):  ## regular method applies on instances
        return '==> %s %s:  %s - %s, subject:  %s' %(self.fname,self.lname,self.gender,self.email,self.subject)

stud_1 = Students('John', 'Gardner','Male',0.3,1984)
stud_2 = Students('Mary', 'Jane', 'Female',0.25,1988)
teach_1 = Teachers('Dan', 'Brown', 'Male','Conspiracy')

print stud_1.__dict__.keys()
print stud_2.__dict__.values()
print stud_2.fname, stud_2.lname,stud_2.gender,stud_2.BY,stud_2.email + "\n"

print 'Standart Annual fee:  ' , Staff.annual_fee
print(stud_1.stud_info())
print (Students.stud_info(stud_2))
print 'Staff #: ',Staff.staff_num
## Now we correct the standart annual fee
Staff.set_fee(1921.00)
print '\nNew Annual fee:  ' , Staff.annual_fee
print(stud_1.stud_info())
print (Students.stud_info(stud_2))

print (teach_1.teac_info())
import datetime
w_day = datetime.date(2017,12,8)
print 'Workday: ',Staff.is_work_day(w_day)

## Special metods to represent info in HR format
print(teach_1)
print teach_1.fullname()

print(repr(stud_1))
print(str(stud_2))

print(stud_1 + stud_2)
print(len(stud_1))
