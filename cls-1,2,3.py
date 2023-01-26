#dictionary
d={'key':'value'}
d.update({'name':'username'})
d.update({'branch':'cse'})
d.update({'sec':'A'})
for i in d:
    print(i)
#---------------------------------------------
d={'key':'value'}
d.update({'name':'username'})
d.update({'branch':'cse'})
d.update({'sec':'A'})
for i in d:
    print(d[i])
#--------------------------------
l=[]
for i in range(5):
    d ={
        'key1': input('enter key 1:'),
        'key2': input('enter key 2:')
    }
    l.append(d)
    print(d)
#---------------------------------------
l=[]
d={}
for i in range(2):
    d.update({
        'key1': input('enter key 1:'),
        'key2': input('enter key 2:')
    })
    l.append(d)
print(l)
#-------------------------------------
a=[1,2,3]
b=a
b[0]=100
print(a)
print(b)
#-------------------------------------------------
s1="hello world"
s2="HI THERE"
print(s1.upper())
print(s2.lower())
#----------------------------------------------------

num=5
print("the square of {} is {}".format(num,num*num))#{ }is {:.2f}
#square of NUM
#----------------------------------------------
a=int(input("enter"))
b=int(input("enter"))
try:
    print(a/b)
except:
    print("b can't be 0")
print("after error")
#-----------------------------------------------------
#l=[56,43,78,245,2478,"hello",[1,2,3,4]]
#k=78
#for i in range(len(l)):
 #   if k == l[i]:
  #      print(i)
   #     temp=True
    #    break
#if temp == False:
 #   print("ele not found")
#-----------------------------------------
#l=[x*x*x for x in range (0,10)]
#print(l)
#------------------------------------------
#l=[num for num in range(0,51) if num%2==0]
#print(l)
#-----------------------------------------
#l=[num for num in range(1,101) if num%7==0 and num%11==0]
#print(l)
#-----------------------------------------------------

#dict={}
#dict.update(
 #   {'key1':'value1'}
  #  {'key2':'value2'}
   # {'key3':'value3'}
#)
#print(dict)
#----EXample----
#a=int(input())
#if a<20 :
 #   if a%2==0:
  #      print("weird")
   # else :
    #    print("odd")
#elif a>=20 and a<30:
  #  print("normal")

#elif a>=30:
  #  if a%2!=0:
   #     print("normal")
    #else:
     #   print("weird")

#----WEEKS-----
#if a==1:
 #    print("sun")
#elif a==2:
 #   print("Mon")
#elif a==3:
 #   print("tue")
#elif a==4:
 #   print("wed")
#elif a == 5:
 #   print("Thu")
#elif a == 6:
 #   print("fri")
#elif a == 7:
 #   print("sat")
#else:
 #   print("invalid")
# ----ODD/EVEN----
#if a%2==0:
 #   print("even ")
#else:
 #   print("odd")

#print("even")  if  (a%2==0)   else print("odd")

#STUDENT@2022-----password

