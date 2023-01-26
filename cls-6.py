#------------------------------------------------
"""download for git
   1) google---git-scm.com
   2)64-bit for window setup
   3) nxt-nxt-nxt done"""



"""--------------------------------------------------------
new--repoistory name---public--
code(green)
-----HTTPS-- copy link----python files--click on CMD---
1)git init---enter
----git folder(hidden folder)
2)(copied link)--git remote add origin <repo link>
3)git add
 4)git commit -m "message"---"message"--my first  Commit or initial commit
5)git push origin master(red--yellow)colours"""
#------------------------------------------------------------------
from abc import ABC,abstractmethod

class Area(ABC):
    @abstractmethod
    def calculate_area(self):
        pass
    @abstractmethod
    def calculate_area(self):
        pass
class Square(Area):
    def calculate_area(self):
        print("square in calculate_area")
    def calculate_circle_area(self):

        pass
#it is an abstraction method we must have to do define it if we don't need it
    #if not writeen gives error
class circle(Area):
    def calculate_area(self):
        print("circle in calculate_area ")
    def calculate_circle_area(self):
        print("circle in calculate_circle_area")
obj = Square()
obj.calculate_area()
obj.calculate_circle_area()
obj1 = circle()
obj1.calculate_area()
obj1.calculate_circle_area()
#----------------------------------------
#from abc import ABC
#class Area(ABC):
 #   def calculate_area(self):
  #      print("calculate_area")
       # pass
#class Square(Area):
  #  pass
#class Rectangle(Area):
 #   pass
#obj=Square()
#obj.calculate_area()
#----------------------------------------------------------------
#from abc import ABC
#class Area(ABC):
 #   def calculate_area(self):
  #      print("calculate_area")
       # pass
#class Square(Area):
 #   pass
#class Rectangle(Area):
 #   pass
#obj=Square()
#obj.calculate_area()
          #--------- o/p:vth pass ntng
        #--------------o/p:vthout passs about print statement
#---------------------------------------------------------------------
#class dog:
 #   def d(self):
  #      print("barking")
#class cat(dog):
 #   def d(self):
  #      print("Meow-Meow")
#obj=cat()
#obj.d()
#--------------------------------------------------
#same method name in diff class OVERRIDING

#class A:
 #   def m1(self):
  #      print("in class-A")
#class B(A):
 #   def m1(self):
  #      print("in class-B")
#obj=B()
#obj.m1()

#-------------------------------------------
#def m1(a,b,c):
 #   print(a+b+c)
#m1(1,2,3)
#------------------------------------------------
#OVERLOADING
#def m1(a,b,c=0):
 #   print(a+b)
#def m1(a,b,c):
 #   print(a*b*c)
#print(m1(10,20,30))
#print(m1(10,20,30))
#-------------------------------------
#from translate import Translator

#obj=Translator(from_lang="english",to_lang="hindi")
#new_name=obj.translate("geethika")
#print(new_name)

