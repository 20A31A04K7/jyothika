#------------------------------------------------------------
from random import randint
choice=["rock","paper","scissor"]
p_score=0
c_score=0
limit=3
while p_score!=limit and c_score!=limit:
    print(f"choose among the following:", choice)
    my_ch = input("player choice:").lower()
    if my_ch not in choice:
        print("invalid input")
        continue
    sys_ch=choice[int(randint(0,2))]
    print(f"System choice:{sys_ch}")
    if my_ch == sys_ch:
        print("---------Draw---------")
    elif my_ch=="rock" and sys_ch =="scissor":
        p_score+=1
    elif my_ch=="paper" and sys_ch =="rock":
        p_score+=1
    elif my_ch=="scissor" and sys_ch =="paper":
        p_score+=1
    else:
        c_score+=1
    print(f"your score:{p_score},system score:{c_score}")

if p_score>c_score:
    print("you win the match")
else:
    print("system win the match")
#------------------------------------------------------------
#row=3
#col=3
#arr=[
 #   [1,2,3],
  #  [4,5,6],
   # [7,8,9]
#]
#new_arr=[]
#print(arr[1])
#print(arr[1][1])
#for i in range(row):
#print(arr)
 #   temp=[]
   # a=input().split('')
   # print(a)
  #  b=list(map(int,a))
#print(b)
#new_arr.append((b))
#print(new_arr)
#---------------------------------------------
#arr=[]
#arr2=[]
#row=2
#col=2
#for i in range (row):
 #   element = []
  #  for j in range(col):
   #      element.append(int(input("element")))
   # arr.append(element)
#print(arr)
#for i in range (row):
 #   element = []
  #  for j in range(col):
   #      element.append(int(input("element")))
   # arr2.append(element)
#print(arr2)
#res=arr+arr2
#print(res)
#----------------------------------------------------------------------------

#arr=[]
#row=3
#col=3
#for i in range(row):
 #   element = []
  #  for j in range(col):
   #     element.append(int(input("element")))
    #arr.append(element)
#print(arr)
#-------------------------------------------------------------------

#db=[
 #   {'abc@example.com':'abc'},
  #  {'xyz@example.com':'123'},
   # {'a123@example':'ddfdf'},
    #{'fsd@example.com':'123456'}
#]
#print(db)
#username=input()
#password=input()
#for i in db:
   # print(i.keys())
    #print(i.values())
    #print(i.items())
 #   temp= {username:password}
#if temp in db:
 #   print('found')
#else:
 #   print('not Found')

#-------------------------------------------------------------------
#d={}
#d.update({'k1':'v1'}),
#d.update({'k2':'v2'}),
#d.update({'k3':'v3'}),
#d.update({'k4':'v4'}),
#d.update({'k5':'v5'})

#print(d)
#i=l.append(d)
#r=list(i)
#print(r)
#---------------------------------------------------------------------
#l=[]
#for i in range(5):
 #   d={
    #    'key1':input(),
   #     'key2':input()
    #}
    #l.append(d)
    #print(d)
#----------------------------------------------------------------------
#l=[]
#d={}
#for i in range(2):
    #d={}
    #d.update({
   #     'key1':input(),
    #    'key2':input()
  #  })
 #   l.append(d)
#print(d)


#-------------------------------------------------------------
#d={'key1':'value1'}
#d.update({'name':'user name'})
#d.update({'branch':'ece'})
#d.update({'sec':'d'})
#for i in d:
 # print((d[i]))
 #   print(i)
  #  print(type(i))
#---------------------------------------------------------------
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

#----EXample---------------------------
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

#----WEEKS-------------------------
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
# ----ODD/EVEN-------------------
#if a%2==0:
 #   print("even ")
#else:
 #   print("odd")

#print("even")  if  (a%2==0)   else print("odd")

#STUDENT@2022

