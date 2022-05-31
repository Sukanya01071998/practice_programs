# # def fact(x):
# #  if x==0:
# #   return 1
# #  return x* fact(x-1)
# # x=int(input())
# # print(fact(x))
#
# # n=int(input())
# # d=dict()
# # for i in range(1,n+1):
# #  d[i]=i*i
# # print(d)
# # values=input()
# # l=values.split()
# # t=tuple(l)
# # print(l)
# # print(t)
# # class InputOutString(object):
# #  def init(self):
# #  self.s =""
# #  def getString(self):
# #     self.s=input()
# #  def printString(self):
# #   print(self.s.upper())
# # strObj=InputOutString()
# # strObj.getString()
# # strObj.print(String())
# # !/usr/bin/env python
# # import math
# # c=50
# # h=30
# # value=[]
# # iems=[x for x in input().split(',')]
# # for d in items:
# #    value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))
# # print(','.join(value))
# # input_str=input()
# # dimensions=[int(x) for x in input_str.split(',')]
# # rowNum=dimensions[0]
# # colNum=dimensions[1]
# # multilist=[[0 for col in range(colNum)]for row in range(rowNum)]
# # for col in range(colNum):
# #     multilist[row][col]=row*col
# #     print(multilist)
# # items=[x for x in input().split(',')]
# # items.sort()
# # print(','.join(items))
# #
# # lines=[]
# # while True:
# #     s=input()
# #     if s:
# #         lines.append(s.upper())
# #     else:
# #         break;
# #         for sentenc in linesprint(sentence)
# # s=input()
# # words=[word for word in s.split("")]
# # print("".join(sorted(list(set(words)))))
#
# # def sum_list(items):
# #  sum_numbers=0
# #  for x in items:
# #   sum_numbers+=x
# #  return sum_numbers
# # print(sum_list([1,2,-8]))
# # def multiply_list(items):
# #  tot=1
# #  for x in items:
# #   tot*=x
# #  return tot
# # print(multiply_list([1,2,-8]))
# # def max_num_in_list(list):
# #  max=list[0]
# #  for a in list:
# #   if a>max:
# #    max=a
# #  return max
# # print(max_num_in_list([1,2,-8,0]))
# # def min_num_in_list(list):
# #     min=list[0]
# #     for a in list:
# #         if a<min:
# #             min=a
# #     return min
# # print(min_num_in_list([1,2,-8,0]))
# # def match_words(words):
# #     ctr=0
# #     for word in words:
# #         if len(word)>1 and word[0]==word[-1]:
# #             ctr+=1
# #     return ctr
# # print(match_words(['abc','xyz','aba','1221']))
# # def last(n):return n[-1]
# # def sort_list_last(tuples):
# #     return sorted(tuples,key=last)
# # print(sort_list_last([(2,5),(1,2)(4,4),(2,3),(2,)])
# # a=[10,20,30,20,10,50,60,40,80,50,40]
# # dup_items=set()
# # uniq_items=[]
# # l=[]
# # if not l:
# #     print("list is empty")
# # original_list=[10,22,44,23,4]
# # new_list=list(original_list)
# # print(original_list)
# # print(new_list)
# # def long_words(n,str):
# #     word_len=[]
# #     txt=str.split(" ")
# #     for x in txt:
# #         if len(x)>n:
# #             word_len.append(x)
# #     return word_len
# # print(long_words(3,"the quick brown fox jumps over the lazy dog"))
# # color=['Red','Green','White','Black','Pink','Yellow']
# # color=[x for (i,x) in enumerate(color) if i not in (0,4,5)]#num= # print(color)
# # array=[[['1,2,3' for col in range(6)]for col in range(4)]for row in range (3)]
# # print(array)
# # num= [7,8,120,25,44,20,27]
# # num= [x for x in num if x%2!=0]
# # print(num)
# # from random import shuffle
# # color=['Red','Green','White','Black','Pink','Yellow']
# # shuffle(color)
# # print(color)
# # set= {"apple","banana","cherry","orange"}
# # set.remove("orange")
# # print(set)
# # list=[10,20,30,40,50,60,70,80,90,100]
# # print("even positions; ")
# # for i in range(1,len(list),2)
# # print(list[i])
# # def char_frequency(str1):
# #     dict={}
# #     for n in str1:
# #         keys=dict.key()
# #         if n in keys:
# #              dict[n]+=1
# #         else:
# #              dict[n]=1
# #     return dict
# # print(char_frequency("google.com"))
# # n=int(input("enter a number: "))
# # for i in range(1,11):
# #       print(n,"*",i,"=",n*i)
# # d={"name":"kelly","age":25,"salary":8000,"city":"newyork"}
# # keys={"name","salary"}
# # d1={}
# # for i in  keys:
# #     d1[i]=d[i]
# #     print(d1)
# # l=[1,2,3,4,2,3,4,5,6]
# # print((set(l)))
# # color=['red','green','white','black','pink','yellow']
# # color=[x for(i,x) in enumerate(color)if i not in (0,4,5)]
# # print(color)
# # d={1:['a','G','k','l'],2:['G','b','c',],3:['a','k','G','c']}
# # s=input()
# # count=0
# # for i in d.values():
# #     for j in i:
# #         if j==s:
# #             count+=1
# #             print(count)
# # str=("sukanya")
# # i=0
# # print("characters present at even positions:")
# # while i<len(str):
# #     print(str[i])
# #     i=i+2
# # d={'a':1,'b':2,'c':3}
# # num=int(input())
# # if num in d.values():
# #     print("given number is  exist in dictionary")
# # else:
# #     print("given number is not exist in dictionary")
# # d={'a':2,'b':3,'c':4,'d':5}
# # m_value=1
# # for i in d:
# #      m_value=m_value*d[i]
# # print("multiplication value: ",m_value)
# # def match_words(words):
# #     ctr=0
# #     for word in words:
# #         if len(word)>1 and word[0]==word[-1]:
# #             ctr+=1
# #         return ctr
# # print(match_words(['abbca','xyzx','abda','1221']))
# # a=int(input())
# # b=int(input())
# # if a*b>1000:
# #     print(a+b)
# # else:
# #     print(a*b)
# # s='123'
# # count=0
# # for x in s:
# #     count+=1
# # print("length of string is: ",count)
# # l=[1,3,5,6,2,1,3]
# # print("the list in reverse order is: ")
# # for i in reversed(l):
# #      print(i,end="")
# # n=int(input("enter the number:"))
# # result=1
# # for i in range(n,0,-1):
# #   result=result*i
# # print("factorial of ",n,"is",result)
# # l=[10,20,30,40,50,60,70,80,90,100]
# # print("values are present in even position:")
# # for i in range(1,len(l),2):
# #      print(l[i])
# # l=[12,15,32,42,55,75,122,132,150,180,200]
# # for i in range(1,len(l),1):
# #     if l[i]<=150:
# #         if l[i]%5==0:
# #             print(l[i])
# # n=1
# # while(True):
# #     print(n)
# #     n+=1
# # num=int(input("enter a number:"))
# # n=1
# # while(n<=num):
# #     print(n,end="")
# #     n=n+1
# # print("enter a string:")
# # txt=input()
# # print("enter the character to count:")
# # char=input()
# # val=txt.count(char)
# # print("occurances of given character in a string:")
# # print(val)
# # d={"class":{"student":{"name":"mike","marks":{"physics":70,"history":80}}}}
# # print(d['class']['student']['marks']['history'])
# # x=5
# # y=3
# # def recursive_multiply(x,y):
# #     if y==0:
# #         return 0
# #         return x+recursive_multiply(x,y-1)
# #     print(x*y)
# #     print(recursive_multiply(x,y))
# # b=float(input("enter a width of  number:"))
# # l=float(input("enter a length of number:"))
# # area=b*l
# # perimeter=(b+l)*2
# # print("area of the rectangle is: ",area)
# # print("perimeter of the rectangle is:",perimeter)
# # r=input("enter radius of circle:")
# # r=float(r)
# # a=3.14*r*r
# # c=2*3.14*r
# # print("Area=",a)
# # print("circumference=",c)
# # def multiplicationtable(num,i):
# #     print(num,"x",i,"=",num*i)
# #     if(i<10):
# #         multiplicationtable(num,i+1)
# # num=int(input("enter a number:"))
# # print("multiplicationtable of ",num,"is:")
# # multiplicationtable(num,1)
#
# # age=int(input("enter your age:"))
# # if age>=18:
# #     print("eligible for voting")
# # else:
# #     print("not eligible for voting")
# # def func(age):
# #     if age>=18:
# #         return"the person is eligible for voting"
# #     else:
# #         return"the person is not eligible for voting"
# # print(func(20))
# # print(func(17))
# # def  fun(n1,n2):
# #     val=n1**n2
# #     print("the power of",n1,"to",n2,"is",val)
# #     return val
# # fun(5,3)
# # def power(a,b):
# #     if b==1:
# #         return a
# #     else:
# #         return a*power(a,b-1)
# # print(power(6,2))
# # def fun(n):
# #     if n%2==0:
# #         return"given numer is even"
# #     else:
# #         return"given number is odd"
# # print(fun(2))
# # print(fun(3))
# # def perfect(n):
# #     sum=0
# #     for i in range(1,n):
# #         if n%i==0:
# #             sum+=i
# #     if sum==n:
# #         print('given number is a perfect number:')
# #     else:
# #         print('not a perfect number')
# # perfect(100)
# # def func(n):
# #     for i in range(2,n):
# #         if n%i==0:
# #             return"given number is not a prime number"
# #         else:
# #             return"given number is prime number"
# # print(func(13))
# # def max(a,b):
# #     if a>b:
# #         print(a,"is greater")
# #     elif a<b:
# #         print(b,"is greater")
# #     else:
# #         print("a=b")
# # max(5,10)
# # def fun(n):
# #     if n%3==0 and n%5==0:
# #         return"FizzBuzz"
# #     elif n%5==0:
# #         return"Buzz"
# #     elif n%3==0:
# #         return"Fizz"
# #     else:
# #         return n
# # print(fun(15))
# # print(fun(10))
# # print(fun(2))
# # print(fun(9))
# # def fun(speed):
# #     if speed<70:
# #         return"ok"
# #     elif speed>=70:
# #         points=(speed-70)//5
# #         if points>12:
# #             return"license suspended"
# #         else:
# #             return("points={}".format(points))
# # print(fun(190))
# # def showNumbers(limit):
# #     for i in range(0,limit+1):
# #         print(i,"even")if i%2==0 else print(i,"odd")
# # showNumbers(10)
# # def mult(limit):
# #     l=[]
# #     for i in range(0,limit+1):
# #         if i%3==0 or i%5==0:
# #             l.append(i)
# #     return l
# # print(mult(20))
# # def show_stars(rows):
# #     l=[]
# #     for i in range(1,rows+1):
# #         l.append("*"*i)
# #      print("\n".join(l))
# # show_stars(7)
# # def prime(limit):
# #     for i in range(2,limit):
# #        if i%2== 0:
# #            continue
# #        else:
# #           print(i)
# # prime(100)
# # def char_frequency(str1):
# #     dict={}
# #     for n in str1:
# #         keys=dict.keys()
# #         if n in keys:
# #             dict[n]+=1
# #         else:
# #             dict[n]=1
# #     return dict
# # print(char_frequency('google.com'))
# # def not_poor(str1):
# #     snot=str1.find('not')
# #     spoor=str1.find('poor')
# #     if spoor>snot and snot>0 and spoor>0:
# #         str1=str1.replace(str1[snot:(spoor+4)],'good')
# #         return str1
# #     else:
# #         return str1
# # print(not_poor('the lyric is not that poor!'))
# # print(not_poor('the lyrics is poor!'))
# # from functools import reduce
# # list1=[20,13,4,8,9]
# # add=reduce(lambda x,y:x+y,list1)
# # print("addition of all list elements is:",add)
# # def match_words(words):
# #     ctr=0
# #     for word in words:
# #         if len(word)>1 and word[0]==word[-1]:
# #             ctr+=1
# #     return ctr
# # print(match_words(['abc','xyz','aba','1221']))
# # l1=['a','b','c','d','e','a']
# # l2=[2,1,1,1,1]
# # x=dict(zip(l1,l2))
# # print(x)
# # print(x['a'])
# # my_dict={'a':100,'b':-54,'c':247}
# # result=1
# # for key in my_dict:
# #     result=result*my_dict[key]
# # print(result)
# # my_dict={'x':500,'y':5874,'z':560}
# # key_max=max(my_dict.keys(),key=(lambda k:my_dict[k]))
# # key_min=min(my_dict.keys(),key=(lambda k:my_dict[k]))
# # print('maximum value:',my_dict[key_max])
# # print('minimum value:',my_dict[key_min])
# # l=[10,93,45,6,24,37,12]
# # l1=[x*10 for x in l if x%2==0]
# # print(l1)
# # x=int(input("enter a number:"))
# # y=int(input("enter a number:"))
# # z=int(input("enter a number:"))
# # if x<y and x<z:
# #     if y<z:
# #         min,mid,max=x,y,z
# #     else:
# #         min,mid,max=x,z,y
# # elif y<x and y<z:
# #     if x<z:
# #         min,mid,max=y,x,z
# #     else:
# #         min,mid,max=y,z,x
# # else:
# #     if x<y:
# #         min,mid,max=z,x,y
# #     else:
# #         min,mid,max=z,y,x
# # print("min:",min)
# # print("mid:",mid)
# # print("max:",max)
# # x=int(input("enter a number in x:"))
# # y=int(input("enter a number in y:"))
# # l=[x,y]
# # print("the original list is:",l)
# # print("after replace the items in list", l, "is:")
# # def swappositions(l,p1,p2):
# #     get=l[p1],l[p2]
# #     l[p2],l[p1]=get
# #     return l
# # p1,p2=0,1
# # print(swappositions(l,p1-1,p2-1))
# # z=int(input("default argument in z is:"))
# # def add(a,b,z=10):
# #     sum=a+b+z
# #     return sum
# # add(10,20,z)
# # def sorted(*h):
# #     l=list(h)
# #     l.sort()
# #     print(l)
# # sorted(1,3,5,6,4,)
# # for i in range(5):
# #     for j in range(i+1):
# #         print('*',end=' ')
# #     print()
# # j=5
# # for i in range(j+1):
# #  print('*'*i)
# # n=int(input())
# # c=0
# # for i in range(1,n):
# #     if n%i==0:
# #         c+=i
# # if c==n:
# #     print("perfect number")
# # else:
# #     print("not a perfect number")
# # l=[1,2,3,4,5,6,7]
# # l.insert(4,9)
# # print(l)
# # l=[-10,5,12,-78,6,-1,-7,9]
# # positive_nos=list(filter(lambda x:x>0,l))
# # print("positive numbers are:",positive_nos)
# # l1=[2,3,4,8,9]
# # l2=list(map(lambda x:x*x*x,l1))
# # print("cube valus are:",l2)
# # from functools import reduce
# # list1=[20,13,4,8,9]
# # add=reduce(lambda x,y:x+y,list1)
# # print("addition of all list elements is:",add)
# # def fun(n,i):
# #     if i>10:
# #         return
# #     else:
# #         print(n,"*",i,"=",n*i)
# #         return fun(n,i+1)
# # fun(5,1)
# # def rect(l,w):
# #     area=l*w
# #     perimeter=2*(l+w)
# #     print(area)
# #     print(perimeter)
# #     return (area, perimeter)
# # rect(6,4)
# # l=['a','b','c','d','a']
# # d={}
# # for i in l :
# #     # rect(4,5)
# #     if i in d:
# #         d[i]+=1
# #     else:
# #         d[i]=1
# # print(d)
# # d={'a':100,'b':200,'c':300}
# # a=sorted(d.values())
# # print(a[0])
# # print(a[-1])
# # d={'a':100,'b':200,'c':300}
# # max=0
# # for i in d.values():
# #     if i >max:
# #         max=i
# # print(max)
# # min=max
# # for j in d.values():
# #     if j<min:
# #         min=j
# # print(min)
# # l=['a','b','c']
# # print(l[0],l[1])
# # from math import pi
# # r = float(input ("Input the radius of the circle : "))
# # print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))
# # str=1,2,3,4,5
# # l=list(str)
# # print(l)
# # t=tuple(l)
# # print(t)
# #  l=["white","green","yellow","black"]
# # print(l[0],l[-1])
# # fname='abc.java'
# # f_extns=fname.split('.')
# # print(f_extns[-1]
# # exam_date=(11,12,2014)
# # print("the exam date start from:%i/%i/%i"%exam_date)
# # import calendar
# # x=int(input("input the year: "))
# # y=int(input("input the month :"))
# # print(calendar.month(x,y))
# # pi = 3.1415926535897931
# # r= 6.0
# # V= 4.0/3.0*pi* r**3
# # print('The volume of the sphere is: ',V)
# # def difference(n):
# #     if n <= 17:
# #         return 17 - n
# #     else:
# #         return (n - 17) * 2
# #
# # print(difference(22))
# # print(difference(14))
# # def near_thousand(n):
# #     return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))
# # print(near_thousand(1000))
# # print(near_thousand(900))
# # print(near_thousand(800))
# # print(near_thousand(2200))
# # def ltos(s):
# #     str=" "
# #     for ele in s:
# #         str+=ele+" "
# #     return str
# # s=['geeks','for','geeks']
# # print(ltos(s))
# # def listToString(s):
# #     # initialize an empty string
# #     str1 = " "
# #
# #     # return string
# #     return (str1.join(s))
# #
# #
# # # Driver code
# # s = ['Geeks', 'for', 'Geeks']
# # print(listToString(s))
# # s=['i','want',4,'apples',18,'bananas']
# # ltos=' '.join([str(elem)for elem in s])
# # print(ltos)
#
# # Python program to convert a list
# # to string using list comprehension
#
# # s = ['I', 'want', 4, 'apples', 'and', 18, 'bananas']
# #
# # # using list comprehension
# # listToStr = ' '.join(map(str, s))
# #
# # print(listToStr)
# # def convert(s):
# #     new=" "
# #     for x in s:
# #         new+=x+" "
# #     return new
# # s = ['g', 'e', 'e', 'k', 's', 'f', 'o', 'r', 'g', 'e', 'e', 'k', 's']
# # print(convert(s))
#
# # Python3 code to demonstrate
# # split string to character list
# # using list()
#
# # initializing string
# # test_string = 'GeeksforGeeks'
# #
# # # printing the original string
# # print("The original string is : ",str(test_string))
# #
# # # using list()
# # # to split string to character list
# # res = list(test_string)
# #
# # # printing result
# # print("The splitted character's list is : ",str(res))
#
# # Python3 code to demonstrate
# # Tokenizing strings in list of strings
# # using list comprehension + split()
#
# # initializing list
# # test_list = ['Geeks for Geeks', 'is', 'best computer science portal']
# #
# # # printing original list
# # print("The original list : ",test_list)
# #
# # # using list comprehension + split()
# # # Tokenizing strings in list of strings
# # res = [sub.split() for sub in test_list]
# #
# # # print result
# # print("The list after split of strings is : ",res)
#
# # Python3 code to demonstrate
# # Tokenizing strings in list of strings
# # using map() + split()
#
# # initializing list
# # test_list = ['Geeks for Geeks', 'is', 'best computer science portal']
# #
# # # printing original list
# # print("The original list : ",test_list)
# #
# # # using map() + split()
# # # Tokenizing strings in list of strings
# # res = list(map(str.split, test_list))
# #
# # # print result
# # print("The list after split of strings is : ",res)
# # l=[]
# # for i in range(2000, 3201):
# #  if (i%7==0) and (i%5!=0):
# #   l.append(str(i))
# # print(','.join(l))
# # def fact(x):
# #  if x == 0:
# #    return 1
# #  return x * fact(x - 1)
# # x=int(input())
# # print(fact(x))
# # n=int((input())
# # d=dict()
# # for i in range(1,n+1):
# #  d[i]=i*i
# # print(d)
# # values=input()
# # l=values.split()
# # t=tuple(l)
# # print(l)
# # print(t)
# # class InputOutString(object):
# #  def init(self):
# #   self.s = ""
# #  def getString(self):
# #   self.s =input()
# #  def printString(self):
# #      print(self.s.upper())
# # strObj = InputOutString()
# # strObj.getString()
# # strObj.printString()
# # import math
# # c=50
# # h=30
# # value = []
# # items=[x for x in input().split(',')]
# # for d in items:
# #  value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))
# # print(','.join(value))
# # input_str=input()
# # dimensions=[int(x) for x in input_str.split(',')]
# # rowNum=dimensions[0]
# # colNum=dimensions[1]
# # multilist=[[0 for col in range(colNum)] for row in range(rowNum)]
# # for row in range(rowNum):
# #  for col in range(colNum):
# #      multilist[row][col]= row*col
# # print(multilist)
# # items=[x for x in input().split(',')]
# # items.sort()
# # print(','.join(items))
# # from itertools import count
# # from shlex import join
# #
# # # from Tools.demo.beer import n
# # #
# # # lines = []
# # # while True:
# # #  s=input()
# # #  if s:
# # #      lines.append(s.upper())
# # #  else:
# # #      break;
# # # for sentence in lines:
# # #     print(sentence)
# # # s=input()
# # # words = [word for word in s.split(" ")]
# # # print(" ".join(sorted(list(set(words)))))
# # # value = []
# # # items=[x for x in input().split(',')]
# # # for p in items:
# # #  intp=int(p, 2)
# # #  if not intp%5:
# # #      value.append(p)
# # # print(','.join(value))
# # # values = []
# # # for i in range(1000, 3001):
# # #  s = str(i)
# # #  if (int(s[0])%2==0)and(int(s[1])%2==0)and(int(s[2])%2==0)and(int(s[3])%2==0):
# # #      values.append(s)
# # # print(",".join(values))
# # # s=input()
# # # d={"DIGITS":0, "LETTERS":0}
# # # for c in s:
# # #  if c.isdigit():
# # #      d["DIGITS"]+=1
# # #  elif c.isalpha():
# # #      d["LETTERS"]+=1
# # #  else:
# # #      pass
# # # print("LETTERS", d["LETTERS"])
# # # print("DIGITS", d["DIGITS"])
# # # s=input()
# # # d={"UPPER CASE":0, "LOWER CASE":0}
# # # for c in s:
# # #     if c.isupper():
# # #         d["UPPER CASE"]+=1
# # #     elif c.islower():
# # #         d["LOWER CASE"]+=1
# # #     else:
# # #         pass
# # # print("UPPER CASE", d["UPPER CASE"])
# # # print("LOWER CASE", d["LOWER CASE"])
# # # a=input()
# # # n1 = int( "%s" % a )
# # # n2 = int( "%s%s" % (a,a) )
# # # n3 = int( "%s%s%s" % (a,a,a) )
# # # n4 = int( "%s%s%s%s" % (a,a,a,a) )
# # # print(n1+n2+n3+n4)
# # # values =input()
# # # numbers = [x for x in values.split(",") if int(x)%2!=0]
# # # print(",".join(numbers))
# # # s=input()
# # # if not s:
# # #   break
# # #  values=s.split(" ")
# # #  operation = values[0]
# # #  amount = int(values[1])
# # #  if operation=="D":
# # #         netAmount+=amount
# # #  elif operation=="W":
# # #         netAmount-=amount
# # #  else:
# # #     pass
# # # # print(netAmount)
# # # import re
# # # value = []
# # # items=[x for x in input().split(',')]
# # # for p in items:
# # #  if len(p)<6 or len(p)>12:
# # #   continue
# # #  else:
# # #   pass
# # #  if not re.search("[a-z]",p):
# # #   continue
# # #  elif not re.search("[0-9]",p):
# # # import re
# # # value = []
# # # items=[x for x in input().split(',')]
# # # for p in items:
# # #  if len(p)<6 or len(p)>12:
# # #      continue
# # #  else:
# # #       pass
# # #  if not re.search("[a-z]",p):
# # #       continue
# # #  elif not re.search("[0-9]",p):
# # #       continue
# # #  elif not re.search("[A-Z]",p):
# # #       continue
# # #  elif not re.search("[$#@]",p):
# # #       continue
# # #  elif re.search("\s",p):
# # #       continue
# # #  else:
# # #       pass
# # #  value.append(p)
# # # print(",".join(value))
# # # from operator import itemgetter, attrgetter
# # # l = []
# # # while True:
# # #  s = input()
# # #  if not s:
# # #   break
# # #  l.append(tuple(s.split(",")))
# # # print(sorted(l, key=itemgetter(0,1,2)))
# # # def putNumbers(n):
# # #  i = 0
# # #  while i<n:
# # #   j=i
# # #   i=i+1
# # #  if j%7==0:
# # #   yield j
# # # for i in reverse(100):
# # #  print(i)
# # # import math
# # # pos = [0,0]
# # # while True:
# # #  s =input()
# # #  if not s:
# # #   break
# # #  movement = s.split(" ")
# # #  direction = movement[0]
# # #  steps = int(movement[1])
# # #  if direction=="UP":
# # #   pos[0]+=steps
# # #  elif direction=="DOWN":
# # #   pos[0]-=steps
# # #  elif direction=="LEFT":
# # #   pos[1]-=steps
# # #  elif direction=="RIGHT":
# # #   pos[1]+=steps
# # #  else:
# # #   pass
# # # print(int(round(math.sqrt(pos[1]**2+pos[0]**2))))
# # # freq = {} # frequency of words in text
# # # line=input()
# # # for word in line.split():
# # #  freq[word] = freq.get(word,0)+1
# # # words = freq.keys()
# # # words.sort()
# # # for w in words:
# # #  print("%s:%d" % (w,freq[w]))
# # # def square(num):
# # #   return num ** 2
# # # print(square(2))
# # # print(square(3))
# # # def add(a,b):
# # #   c=a+b
# # #   return c
# # # print(add(2,5))
# # # a=10
# # # b=20
# # # a,b=b,a
# # # print(a)
# # # print(b)
# #
# # # Python program to demonstrate
# # # swapping of two variables
# #
# # # x = 10
# # # y = 50
# # #
# # # # Swapping of two variables
# # # # using arithmetic operations
# # # x = x + y
# # # y = x - y
# # # x = x - y
# # #
# # # print("Value of x:", x)
# # # print("Value of y:", y)
# #
# # # Python3 program to swap elements
# # # at given positions
# #
# # # Swap function
# # # def swapPositions(list, pos1, pos2):
# # #     list[pos1], list[pos2] = list[pos2], list[pos1]
# # #     return list
# # #
# # #
# # # # Driver function
# # # List = [23, 65, 19, 90]
# # # pos1, pos2 = 1,3
# # #
# # # print(swapPositions(List, pos1,pos2))
# # # Swap function
# # # def swapPositions(list, pos1, pos2):
# # #     # popping both the elements from list
# # #     first_ele = list.pop(pos1)
# # #     second_ele = list.pop(pos2-1)
# # #
# # #     # inserting in each others positions
# # #     list.insert(pos1, second_ele)
# # #     list.insert(pos2, first_ele)
# # #
# # #     return list
# # #
# # #
# # # # Driver function
# # # List = [23, 65, 19, 90]
# # # pos1, pos2 = 1, 3
# # #
# # # print(swapPositions(List, pos1,pos2))
# # # d={'a':1,'b':2,'c':3,'d':4,'e':5}
# # # new_d=dict([(value,key)for key,value in d.items()])
# # # print(d)
# # # print("keys:values")
# # # for i in new_d:
# # #     print(i,":",new_d[i])
# #
# # # Python3 code to demonstrate
# # # swap of key and value
# #
# # # initializing dictionary
# # # import i as i
# #
# # # old_dict = {'A': 67, 'B': 23, 'C': 45, 'D': 56, 'E': 12, 'F': 69, 'G': 67, 'H': 23}
# #
# # # new_dict = dict([(value, key) for key, value in old_dict.items()])
# #
# #
# # # Printing original dictionary
# # # print("Original dictionary is : ")
# # # print(old_dict)
# # #
# # # print()
# # #
# # # # Printing new dictionary after swapping keys and values
# # # print("Dictionary after swapping is :  ")
# # # print("keys: values")
# # # for i in new_dict:
# # #     print(i, " :  ", new_dict[i])
# # # old_dict = {'A': 67, 'B': 23, 'C': 45, 'E': 12, 'F': 69, 'G': 67, 'H': 23}
# #
# # # Printing original dictionary
# # # print("Original dictionary is : ")
# # # print(old_dict)
# # #
# # # print()
# # # new_dict = {}
# # # for key, value in old_dict.items():
# # #     if value in new_dict:
# # #         new_dict[value].append(key)
# # #     else:
# # #         new_dict[value] = [key]
# # #
# # # # Printing new dictionary after swapping
# # # # keys and values
# # # print("Dictionary after swapping is :  ")
# # # print("keys: values")
# # # for i in new_dict:
# # #     print(i, " :", new_dict[i])
# #
# # # Python3 code to demonstrate working of
# # # Ensure all keys in dictionary list
# # # Using set() + chain.from_iterable() + update()
# # # from itertools import chain
# # #
# # # # initializing list
# # # test_list = [{'gfg': 3, 'is': 7},
# # #              {'gfg': 3, 'is': 1, 'best': 5},
# # #              {'gfg': 8}]
# # #
# # # # printing original list
# # # print("The original list is : " + str(test_list))
# # #
# # # # extracting all keys
# # # all_keys = set(chain.from_iterable(test_list))
# # #
# # # # assigning None using update() if key is not found
# # # for sub in test_list:
# # #     sub.update({key: None for key in all_keys if key not in sub})
# # #
# # # # printing result
# # # print("Reformed dictionaries list : " + str(test_list))
# # # def calculateAddition(n):
# # #     return n + n
# # #
# # #
# # # numbers = (1, 2, 3, 4)
# # # result = map(calculateAddition, numbers)
# # # print(result)
# # #
# # # # converting map object to set
# # # numbersAddition = set(result)
# # # print(numbersAddition)
# # # def fib(limit):
# # #     # Initialize first two Fibonacci Numbers
# # #     a, b = 0, 1
# # #
# # #     # One by one yield next Fibonacci Number
# # #     while a < limit:
# # #         yield a
# # #         a, b = b, a + b
# # #
# # #
# # # # Create a generator object
# # # x = fib(5)
# # #
# # # # Iterating over the generator object using next
# # # print(x.next())  # In Python 3, __next__()
# # # print(x.next())
# # # print(x.next())
# # # print(x.next())
# # # print(x.next())
# # #
# # # # Iterating over the generator object using for
# # # # in loop.
# # # print("\nUsing for in loop")
# # # for i in fib(5):
# # #     print(i)
# # # def simpleGeneratorFun():
# # #     yield 1
# # #     yield 2
# # #     yield 3
# # #
# # #
# # # # x is a generator object
# # # x = simpleGeneratorFun()
# # #
# # # # Iterating over the generator object using next
# # # print(x.next())  # In Python 3, __next__()
# # # print(x.next())
# # # print(x.next())
# # # string = 'GeeksforGeeks'
# # #
# # # # lambda returns a function object
# # # print(lambda string: string)
# #
# # # python code to demonstrate working of reduce()
# #
# # # importing functools for reduce()
# # # import functools
# # #
# # # # initializing list
# # # lis = [1, 3, 5, 6, 2, ]
# # #
# # # # using reduce to compute sum of list
# # # print("The sum of the list elements is : ", end="")
# # # print(functools.reduce(lambda a, b: a + b, lis))
# # #
# # # # using reduce to compute maximum element from list
# # # print("The maximum element of the list is : ", end="")
# # # print(functools.reduce(lambda a, b: a if a > b else b, lis))
# # # print("the minimum value in the list is: ",end="")
# # # print(functools.reduce(lambda a,b:a if a<b else b,lis))
# #
# # # function that filters vowels
# # # def fun(variable):
# # #     letters = ['a', 'e', 'i', 'o', 'u']
# # #     if (variable in letters):
# # #         return True
# # #     else:
# # #         return False
# # #
# # #
# # # # sequence
# # # sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']
# # #
# # # # using filter function
# # # filtered = filter(fun, sequence)
# # #
# # # print('The filtered letters are:')
# # # for s in filtered:
# # #     print(s)
# # # import itertools
# # #
# # # for i in itertools.count(10,5):
# # #     if i == 100:
# # #         break
# # #     else:
# # #         print(i, end=" ")
# # # import itertools
# # # temp = 0
# # # for i in itertools.cycle("123"):
# # #     if temp > 7:
# # #         break
# # #     else:
# # #         print(i,end=' ')
# # #         temp = temp+1
# # # def divide(x,y):
# # #     print(x/y)
# # # def outer_div(func):
# # #     def inner(x,y):
# # #         if(x<y):
# # #             x,y=y,x
# # #             return func(x,y)
# # #         return inner
# # # divide1=outer_div(divide)
# # # divide1(2,4)
# # # def divide(x,y):
# # #     print(x/y)
# # # def outer_div(func):
# # #     def inner(x,y):
# # #         if(x<y):
# # #             x,y = y,x
# # #            return func(x,y)
# # #         return inner
# # # divide1 = outer_div(divide)
# # # divide1(2,4)
# # # class program:
# # #     def fun1(self,a,b):
# # #         self.a=a
# # #         self.b=b
# # #         print(self.a+self.b)
# # # p=program()
# # # p.fun1(2,3)
# # # s='pallavi'
# # # half=int(len(s)/2)
# # # if len(s)%2==0:
# # #     first_s=s[:half]
# # #     second_s=s[half:]
# # # else:
# # #     first_s=s[:half]
# # #     second_s=s[half+1:]
# # # if first_s==second_s:
# # #     print("string is symmetrical",s)
# # # else:
# # #     print("string is not symmetrical",s)
# # # if first_s==second_s:
# # #     print("string is palindrome",s)
# # # else:
# # #     print("string is not polyndrum",s)
# # # str='welcome to python programming'
# # # words=str.split(' ')
# # # print(words)
# # # words=words[-1::-1]
# # # print(words)
# # # output_str=' '.join(words)
# # # print(output_str)
# # # s='pallavi'
# # # s=s[::-1]
# # # print(s)
# # # str='welcome to python programming'
# # # words=str.split()
# # # print(words)
# # # words=words[-1::-1]
# # # print(words)
# # # output_str=' '.join(words)
# # # print(output_str)
# # # from datetime import date
# # #
# # #
# # # class Person:
# # #
# # #     # class constructor
# # #     def __init__(self, name, age):
# # #         self.name = name
# # #         self.age = age
# # #
# # #     @classmethod
# # #     def details(cls, name,year):
# # #         return cls(name, date.today().year - year)
# # #
# # #     @staticmethod
# # #     def check_age(age):
# # #         return age > 18
# # #
# # #
# # # # Driver's code
# # # person1 = Person('Mark', 20)
# # # person2 = Person.details('Rohan', 1992)
# # #
# # # print(person1.name, person1.age)
# # # print(person2.name, person2.age)
# # # print(Person.check_age(25))
# # # s="geeksforgeeks"
# # # print("the original string is :",s)
# # # new_s=''.join([s[i]for i in range(len(s)) if i!=2])
# # # print("the string after removal of i'th character:",new_s)
# # # def findlen(str):
# # #     count=0
# # #     for i in str:
# # #         count+=1
# # #     return count
# # # str='s u k a n y a'
# # # print(findlen(str))
# # # def printwords(s):
# # #     s = s.split(' ')
# # #     for word in s:
# # #         if len(word) % 2 == 0:
# # #             print(word)
# # # s="python is a programming language"
# # # printwords(s)
# # # str='geeksforgeeks'
# # # print("the original string is:",str)
# # # hlf_idx=(len(str))//2
# # # res=' '
# # # for idx in range(len(str)):
# # #     if idx<=hlf_idx:
# # #         res+=str[idx].upper()
# # #     else:
# # #         res+=str[idx]
# # # print("the resultant string is:",res)
# # # l=[2,3,4,5,6,7,8,9]
# # # for i in l:
# # #     print(i,":",i**2,end=",")
# # # l=[1,2,3,4,5,6,7,8,9]
# # # l2=[]
# # # for i in range(len(l)):
# # #     elem=l.pop(0)
# # #     l2.append(elem)
# # # print("list1:",l)
# # # print("list2:",l2)
# # # print(sum(l))
# # # l=[2,3,4,5,6]
# # # count=1
# # # for i in l:
# # #     count=count*i
# # # print(count)
# # # l=[2,4,3,5,7,6,9,12,45,8,85,46]
# # # l2=[]
# # # l.sort()
# # # print("the smallest number in l is:",l[0])
# # # print("the biggest number in l is:",l[-1])
# # # for i in range(len(l)):
# # #     l[0]=l[-1]
# # # l2=list(l2.append(len(l)))
# # # print(l2)
# # # list1 = [5, 7, 8, 2, 45, 24, 60, 70, 89, 34]
# # # odd_list = []
# # # even_list = []
# # #
# # # for elem in list1:
# # #     if elem%2 == 0:
# # #         even_list.append(elem)
# # #     else:
# # #         odd_list.append(elem)
# # #
# # # print("Even List:", even_list)
# # # print("Odd List:", odd_list)
# # # s='1a2c3v4b6n'
# # # c=0
# # # for i in range(len(s)):
# # #     if not i.isnumeric():
# # #        pass
# # #     else:
# # #         c+=i
# # # print(c)
# # # str="a345bce"
# # # c=0
# # # for i in range(len(str)):
# # #     if  not i.isnumeric():
# # #         c+=i
# # #     else:
# # #         pass
# # # print(c)
# # # l=[1,2,3,4,5,6,7,8,9,10]
# # # n=int(input())
# # # for i in range(n):
# # #     a=l[-1]
# # #     l.pop()
# # #     l.insert(i,a)
# # # print(l)
# # # l =[5,2,3,4,5,6,7,8,9,5]
# # # l1= []
# # # a = int(input())
# # # count= 0
# # # for i in range(a):
# # #     if a>count:
# # #         l1.append(l[-1])
# # #         l.pop()
# # #         count= count+1
# # # b = l1+l
# # # print(b)
# # # sukanya = open("file.py", "r")
# # #
# # # if sukanya:
# # #     print("file is opened successfully")
# # # res=re.findall()
# # # import numpy as np
# # # l1=[1,2,3,4,5]
# # # l2=[5,4,3,2,1]
# # # l3=l1+l2
# # # n1=np.array(l1)
# # # n2=np.array(l2)
# # # l3=n1+n2
# # # print(l3)
# # # import pandas as pd
# # # import matplotlib.pyplot as plt
# # # import pandas as pd
# # # d=pd.read_csv("C:\\Users\\sukan\\OneDrive\\Desktop\\healthcare-dataset-stroke-data.csv")
# # # df=pd.DataFrame(d)
# # # print(df)
# # # print(df.to_string())
# # # print(df.head())
# # # print(df.describe())
# # # print(df.describe().T)
# # # print(df.shape)
# # # print(df[0:20:2])
# # # print(df[["id",'gender']])w
# # # print(df.loc[[0,4]])
# # # print(df.loc[0:5])
# # # print(df.iloc[0:5])
# # # print(df.loc[45,["id","age"]])
# # # print(df.iloc[0:5])
# # # print(df.iloc[0:4,0:5])
# # # print(df.iloc[[1,2,5],:])
# # # print(df.iloc[20:4,[1,2,3,4]])
# # # i="pallavi"
# # # j=""
# # # for x in i:
# # #     if x not in j:
# # #       j=j+i
# # # print(j)
# # # l1=[1,2,3,4,5]
# # # l2=[6,7,8,9,1]
# # # l3=[4,5,6,7,8]
# # # # for i in l1:
# # # #   print(i)
# # # # for j in l2:
# # # #   print(j)
# # # for(a,b,c) in zip(l1,l2,l3):
# # #   print(a,b,c)
# # # l=[1,2,3,4,5,6]
# # # for num_index,num_value in enumerate(l):
# # #  print(num_index,num_value)
# # # result = enumerate([1,2,3])
# # # # Displayi
# # # ng result
# # # print(result)
# # # # print(list(result))
# # # l1=[1,2,3,4]
# # # l2=[6,5,4,3]
# # # l3=[]
# # # for i in range(0,len(l1)):
# # #      if l1 and l2:
# # #          l3.append(l1[i]+l2[i])
# # # print(l3)
# # # s="Missicippi"
# # # k=""
# # # for i in s:
# # #     if i not in k:
# # #         k=k+i
# # # print(k)
# # # num=56789
# # # rev=0
# # # while(num>0):
# # #     remainder=num%10
# # #     rev=rev*10+remainder
# # #     num=num//10
# # #     print("reverse of number is:",rev)
# # # l=int(input("enter a number:"))
# # # h=int(input("enter a number:"))
# # # print("the prime numers in range are:")
# # # for i in range(l,h+1):
# # #     if i>1:
# # #         for j in range(2,i):
# # #             if(i%j)==0:
# # #                 break
# # #         else:
# # #             print("prime number")
# # # lower_value = int(input("Please, Enter the Lowest Range Value: "))
# # # upper_value = int(input("Please, Enter the Upper Range Value: "))
# # #
# # # print("The Prime Numbers in the range are: ")
# # # for number in range(lower_value, upper_value + 1):
# # #     if number > 1:
# # #         for i in range(2, number):
# # #             if (number % i) == 0:
# # #                 break
# # #         else:
# # #             print(number)
# # # l=[1,2,3,4,5,6,7,8,9,10]
# # # ls=[]
# # # l3=[]
# # # # 1,3,5,7,9,10,8,6,4,2
# # # l1=[l[i] for i in range(len(l)) if i%2==0]
# # # l2=[l[i] for i in range(len(l)) if i%2!=0]
# # # l3=l2[::-1]
# # # print(l3)
# # # ls=l1+l3
# # # print(ls)
# # # s='s@oft_w!a$re #eng-ineer'
# # # s1=""
# # # for i in s:
# # #     if i.isalpha():
# # #         s1+=i
# # # print(s1)
# # # l=[1,2,3,4,5,6]
# # # l1=[6,5,4,3]
# # # l2=[]
# # # a=len(l)
# # # b=len(l1)
# # # c=a-b
# # # for i in range(c):
# # #     l1.append(0)
# # # print(l1)
# # # for i,j in zip(l,l1):
# # #     l2.append(i+j)
# # # print(l2)
# # # s='listen'
# # # s1='silent'
# # # if sorted(s)==sorted(s1):
# # #     print(True)
# # # l=[3,9,1,16,45,32,2]
# # # for i in range(len(l)-1,-1,-1):
# # #     for j in range(i):
# # #         if l[j+1]<l[j]:
# # #             l[j+1],l[j]=l[j],l[j+1]
# # # print(l)
# # # s="missicippi"
# # # s1=""
# # # d=dict()
# # # for i in s:
# # #     if i in d:
# # #         d[i]+=1
# # #     else:
# # #         d[i]=1
# # # print(d)
# # # a=list(set(list(d.values())))
# # # print(a)
# # # x=a[-2]
# # # print(x)
# # # for i,j in d.items():
# # #     if j==x:
# # #          print(i)
# # # for i,j in d.items():
# # #     if j>1:
# # #          print(i)
# # # s="missiccippppi"
# # # c=1
# # # s1=""
# # # for i in range(len(s)-1):
# # #     if s[i]==s[i+1]:
# # #         c+=1
# # #     else:
# # #         s1=s1+s[i]+str(c)
# # #         c=1
# # # print(s1)
# # # k=1
# # # for i in range(len(s)-1,-1,-1):
# # #     if s[i]==s[i-1]:
# # #         k+=1
# # #     else:
# # #         s1=s1+s[i]+str(k)
# # #         break
# # # print(s1)
# # # lower=100
# # # upper=500
# # # print("prime numbers between",lower,"and",upper,"are:")
# # # for num in range(lower,upper+1):
# # #     if num>1:
# # #         for i in range(2,num):
# # #             if num%i==0:
# # #                 break
# # #         else:
# # #             print(num)
# # # import datetime
# # # now = datetime.datetime.now()
# # # print ("Current date and time : ")
# # # print (now.strftime("%Y-%m-%d %H:%M:%S"))
# # # s="my name is sukanya"
# # # d={}
# # # for i in s:
# # #     if i in d:
# # #         d[i]+=1
# # #     else:
# # #         d[i]=1
# # # print(d)
# # # print(d.items())
# # # print(d.keys())
# # # print(d.values())
# # # s="restart"
# # # char=s[-1]
# # # s=s.replace(char,"@")
# # # s=s[:-2]+char
# # # print(s)
# # # s="sukanya"
# # # c=0
# # # for i in s:
# # #     c+=1
# # # print(c)
# # # from math import pi
# # # r=float(input("enter a radius:"))
# # # area=pi*r**2
# # # print("area:",area)
# # # a='abc'
# # # x='xyz'
# # # new_a=x[:2]+a[2:]
# # # new_x=a[:2]+x[2:]
# # # s=new_a+','+new_x
# # # print(s)
# # # s='12345'
# # # v=s.split(',')
# # # print(v)
# # # l=list(s)
# # # print(l)
# # # t=tuple(s)
# # # print(t)
# # # s='sukanya'
# # # length=len(s)
# # # if length>=3:
# # #     if s[-3:]=='ing':
# # #         s+='ly'
# # #     else:
# # #         s+='ing'
# # #     print(s)
# # # else:
# # #     print(s)
# # # filename = input("Input the Filename: ")
# # # f_extns = filename.split(".")
# # # print(f_extns)
# # # print ("The extension of the file is : ",f_extns[-1])
# # # def string_length(str1):
# # #     count = 0
# # #     for char in str1:
# # #         count += 1
# # #     return count
# # # print(string_length('w3resource.com'))
# # # s="sukanyaprabhavathi"
# # # d={}
# # # for i in s:
# # #     if i in d:
# # #         d[i]+=1
# # #     else:
# # #         d[i]=1
# # # print(d)
# # # print(d.keys())
# # # print(d.values())
# # # print(d.items())
# # # a=list(set(list(d.values())))
# # # print(a)
# # # x=a[-3]
# # # for i,j in d.items():
# # #     if j>1:
# # #         print(i,end="")
# # # def str_both_ends(str):
# # #     if len(str)<2:
# # #         return 'empty string'
# # #     return str[0:2]+str[-2:]
# # # print(str_both_ends('w3resource'))
# # # print(str_both_ends('w3'))
# # # print(str_both_ends('w'))
# # # s="s"
# # # s1=""
# # # print(s)
# # # if len(s)<2:
# # #     print("empty string")
# # # else:
# # #     s1=s[0:2]+s[-2:]
# # #     print(s1)
# # # l=[1,2,3,4,5,6,7,8,9,10]
# # # l1=[]
# # # n=8
# # # for i in range(len(l)):
# # #     if n<=i:
# # #         break
# # #     else:
# # #         l1.append(l[-1])
# # #         l.pop()
# # # print(l+l1)
# # # s="sukanyasukkus"
# # # char=s[0]
# # # s=s.replace(char,"$")
# # # s=char+s[1:]
# # # print(s)
# # # str1="sukanyasukkus"
# # # char = str1[0]
# # # str1 = str1.replace(char, '$')
# # # str1 = char + str1[1:]
# # # print(str1)
# # # l=[1,2,3,4,5,6,7,8,9,10]
# # # l1=[]
# # # n=int(input())
# # # for i in range(1,len(l)):
# # #     if n<i:
# # #         break
# # #     else:
# # #         l1.append(l[-1])
# # #         l.pop()
# # # l1.reverse()
# # # print(l1+l)
# # # a="abc"
# # # b="xyz"
# # # c=""
# # # new_a=b[:2]+a[2:]
# # # new_b=a[:2]+b[2:]
# # # c=c+new_a+" "+new_b
# # # print(c)
# # # s="sukanyaing"
# # # if len(s)>2:
# # #     if s[-3:]=="ing":
# # #         s+="ly"
# # #     else:
# # #         s+="ing"
# # # print(s)
# # # def remove_char(str, n):
# # #     first_part = str[:n]
# # #     last_part = str[n + 1:]
# # #     return first_part + last_part
# # # print(remove_char('Python', 0))
# # # print(remove_char('Python', 3))
# # # print(remove_char('Python', 5))
# # # def change_sring(str1):
# # #     return str1[-1:] + str1[1:-1]+str1[:1]
# # # print(change_sring('abcd'))
# # # print(change_sring('12345'))
# # # s="python"
# # # c=" "
# # # for i in range(len(s)):
# # #     if i%2!=0:
# # #         c+=s[i]
# # # print(c)
# # # s="the quick brown fox jumps over the lazy dog."
# # # words=s.split()
# # # d={}
# # # for word in words:
# # #     if word in d:
# # #         d[word]+=1
# # #     else:
# # #         d[word]=1
# # # print(d)
# # # print(list(d.keys()))
# # # s="Python is a Programming Language"
# # # print(s)
# # # s1=s.upper()
# # # print(s1)
# # # s2=s.lower()
# # # print(s2)
# # # s=input("enter a string:")
# # # s1=s.split(",")
# # # print(s1)
# # # s2=",".join(set(list(s1)))
# # # print(s2)
# # # s="python {word} 3.0"
# # # s=s.format(word="tutorial")
# # # print(s)
# # # s="python"
# # # s1=s[-2:]
# # # print(s1*4)
# # # str1 = 'https://www.w3resource.com/python-exercises/string'
# # # print(str1.rsplit('/', 1)[0])
# # # print(str1.rsplit('-', 1)[0])
# # # def to_convert(str1):
# # #     num_upper=0
# # #     for letter in str1[:4]:
# # #         if letter.upper()==letter:
# # #             num_upper+=1
# # #     if num_upper>=2:
# # #         return str1.upper()
# # #     return str1
# # # print(to_convert("Python"))
# # # print(to_convert("PyThon"))
# # # def lexicographi_sort(s):
# # #     return sorted(sorted(s), key=str.upper)
# # #
# # # print(lexicographi_sort('w3resource'))
# # # print(lexicographi_sort('quickbrown'))
# # # s="w3resources"
# # # print(sorted(s))
# # # x = 3.1415926
# # # y = 12.9999
# # # print("\nOriginal Number: ", x)
# # # print("Formatted Number: "+"{:.2f}".format(x));
# # # print("Original Number: ", y)
# # # print("Formatted Number: "+"{:.2f}".format(y));
# # # print()
# # # numStr = "5"
# # # print('Original String :', numStr)
# # # # Left pad the string with 0 to make it's length 4
# # # numStr = numStr.zfill(5)
# # # # print('Updated String :' , numStr)
# # # x = 3
# # # y = 123
# # # print("\nOriginal Number: ", x)
# # # print("Formatted Number(left padding, width 2): "+"{:*<2d}".format(x));
# # # print("Original Number: ", y)
# # # print("Formatted Number(left padding, width 6): "+"{:*<6d}".format(y));x
# # # str = "Geeks for Geeks"
# # #
# # # # Printing the output of ljust() method
# # # print(str.ljust(20, '0'))
# # # str1 = 'The quick brown fox jumps fox over the lazy dog.'
# # # print(str1.count("fox"))
# # # s="python"
# # # s1=s.split()
# # # s1=''.join(reversed(s))
# # # print(s1)
# # # def reverse_string_words(text):
# # #     for line in text.split( '\n'):
# # #         return(' '.join(line.split( )[::-1]))
# # # print(reverse_string_words("The quick brown fox jumps over the lazy dog."))
# # # print(reverse_string_words("Python Exercises."))
# # # s="python is a programming language"
# # # for i in s.split( '\n'):
# # #     s=" ".join(s.split( )[::-1])
# # # print(s)
# # # s="python is a programming language"
# # # char="aeiou"
# # # for i in s:
# # #     if i not in char:
# # #         s=" ".join(i)
# # #         print(s,end="")
# # # def strip_chars(str, chars):
# # #     return "".join(c for c in str if c not in chars)
# # # print(strip_chars("The quick brown fox jumps over the lazy dog.", "aeiou"))
# # # s="python"
# # # s1=s.strip("py")
# # # print(s1)
# # # s="thequickbrownoversthejumpdog."
# # # d={}
# # # for i in s:
# # #     if i in d:
# # #         d[i]+=1
# # #     else:
# # #         d[i]=1
# # # print(d)
# # # # a=list(set(list(d.items())))
# # # # print(a)
# # # for i,j in d.items():
# # #     if j<=1:
# # #         print(i)
# # # s="sukanya"
# # # for i,j in enumerate(s):
# # #     print(j,i)
# # # text="w3resources"
# # # vowels="aeiouAEIOU"
# # # c=0
# # # for i in text:
# # #     if i in vowels:
# # #         c+=1
# # # print(c)
# # # s=[]
# # # for i in text:
# # #     if i in vowels:
# # #         s+=i
# # # print(s,end="")
# # # s="S\tU\tK\tA\tN\tY\tA"
# # # x=s.expandtabs(4)
# # # print(x)
# # # s="sukanya"
# # # x=s.find("a",-1)
# # # print(x)
# # # s="sukanya"
# # # x=s.index("a")
# # # print(x)
# # # s="PRABHA"
# # # print(s.isupper())
# # # s=("sukanya","prabha")
# # # s1="&".join(s)
# # # print(s1)
# # # s="ateywouts"
# # # s1=""
# # # for x in range(0,len(s),3):
# # #     s1="".join(s[x:x+3][::-1])
# # #     print(s1,end="")
# # # s="abcdefghijadgbce"
# # # d={}
# # # for i in s:
# # #     if i in d:
# # #         d[i]+=1
# # #     else:
# # #         d[i]=1
# # # print(d)
# # # a=list(set(list(d.items())))
# # # print(a)
# # # for i,j in d.items():
# # #     if j==2:
# # # #         print(i)
# # # from itertools import product
# # # s="abc"
# # # rno=3
# # # chars=[]
# # # for i in s:
# # #     chars.append(i)
# # # print(chars)
# # # results=[]
# # # for i in product(chars,repeat=rno):
# # #     results.append(i)
# # # print(results)
# # # #
# # # s = 'srikanthsrikanth'
# # # s1 = ''
# # # for i in range(len(s)-1):
# # #     if s[i] in s1:
# # #         print(s[i+1])
# # #         break
# # #     else:
# # #         s1= s1+s[i]
# # # s="absrevsdweg"
# # # s1=" "
# # # for i in range(len(s)-1):
# # #     if s[i] in s1:
# # #         print(s[i+1])
# # #         break
# # #     else:
# # #         s1=s1+s[i]
# # # print(s1)
# # # s="absrevsdweg"
# # # s1=""
# # # for i in range(len(s)-1):
# # #     a = s.count(s[i])
# # #     if a>1:
# # #         s1= s1+s[i]
# # # print(s1[2])
# # # print(s1)
# # # s="123abc456"
# # # c=0
# # # for i in s:
# # #     if i.isdigit()==True:
# # #         z=int(i)
# # #         c=c+z
# # # print(c)
# # # s="sukku hema sukku pallavi naga pallavi veeksha"
# # # s1=s.split()
# # # print(s1)
# # # d={}
# # # for i in s1:
# # #     if i in d:
# # #         d[i]+=1
# # #     else:
# # #         d[i]=1
# # # print(d)
# # # a=list(set(list(d.keys())))
# # # print(a)
# # # x=a[1]
# # # for j in d.keys():
# # #     if j==x:
# # #         print(i)
# # # s="sukku pallavi  meghana pallavi sukku hema veeksha nandhini"
# # # s2=s.split()
# # # l=[]
# # # for i in range(len(s2)-1):
# # #     a=s2.count(s2[i])
# # #     print(a)
# # #     if a>1:
# # #         l.append(s2[i])
# # # print(l[1])
# # # print(l)
# # # def remove_spaces(str1):
# # #     str1 = str1.replace(' ' , '')
# # #     return str1
# # # print(remove_spaces("w 3 res ou r ce"))
# # # print(remove_spaces("a b c"))
# # # import numpy as np
# # # a=[[10,20],[30,40]]
# # # b=np.asarray(a,order="F")
# # # for i in np.nditer(b):
# # #     print(i)
# # # import numpy as np
# # # a=[[10,20],[30,40]]
# # # b=np.asarray(a,order="c")
# # # print(b)
# # # import numpy as np
# # # a=b"welcomes"
# # # c=np.frombuffer(a,dtype="S2")
# # # print(c)
# # # import numpy as np
# # # a=np.array([1,2,3,4,5])
# # # b=np.array([5,4,3,2,1])
# # # c=np.add(a,b)
# # # print(c)
# # # import pandas as pd
# # # s="srikanth"
# # # print(s[0:7:3])
# # # print(float(23))
# # # print(int("23.04"))
# # # print(float(10+30j))
# # # print(float("srikanth"))
# # # print(float("15"))
# # # print(complex("10","12"))
# # # print(complex(True, False))
# # # x=10,20,30,40,50
# # # b=bytearray(x)
# # # print(b)
# # # print(id(b))
# # # t=[10,20,('sukanya',0)]
# # # t.pop()
# # # b =t[-1]
# # # c = list(b)
# # # c.pop()
# # # print(t)
# # # d=tuple(c)
# # # print(t.insert(d,))
# # # def f1(a,b):
# # #     d=20
# # #     c=a+b
# # #     return c
# # #     print(c)
# # # print(f1(2,3))
# # # print(11.0/3.0)
# # # import numpy as np
# # # a = np.array([[1,2,30],[10,15,4]])
# # # b = np.array([[1,2,3],[12, 19, 29]])
# # # print("Sum of array a and b\n",a+b)
# # # print("Product of array a and b\n",a*b)
# # # print("Division of array a and b\n",a/b)
# # # import numpy as np
# # # d = np.dtype([('salary',np.float64)])
# # # print(d)
# # # import numpy as np
# # # d=np.dtype([('salary',np.float64)])
# # # arr = np.array([(10000.12,),(20000.50,)],dtype=d)
# # # print(arr['salary'])
# # # import numpy as np
# # #
# # # a = np.array([[1, 2, 3, 4], [2, 4, 5, 6], [10, 20, 39, 3]])
# # #
# # # print("\nPrinting the array:\n")
# # #
# # # print(a)
# # #
# # # print("\nPrinting the transpose of the array:\n")
# # # at = a.T
# # #
# # # print(at)
# # #
# # # print("\nIterating over the transposed array\n")
# # #
# # # for x in np.nditer(at):
# # #     print(x, end=' ')
# # #
# # # print("\nSorting the transposed array in C-style:\n")
# # #
# # # print("\nIterating over the C-style array:\n")
# # # for x in np.nditer(at, order='C'):
# # #     print(x, end=' ')
# # # l=[9,10,15,20,5,8]
# # # max=l[0]
# # # for x in l:
# # #     if x>max:
# # #         max=x
# # # print(max)
# # # def max_num_in_list( list ):
# # #     max = list[ 0 ]
# # #     for a in list:
# # #         if a > max:
# # #             max = a
# # #     return max
# # # print(max_num_in_list([5,4,6,7,3,9,10,1]))
# # # def min_num_in_list( list ):
# # #     min = list[ 0 ]
# # #     for a in list:
# # #         if a < min:
# # #             min= a
# # #     return min
# # # print(min_num_in_list([5,4,6,7,3,9,10,1]))
# # # l=['xyz','aba','abc','1221']
# # # c=" "
# # # for word in  l:
# # #     if len(word)>1 and word[0]==word[-1]:
# # #         c+=word
# # #         print(c,end=",")
# # # l=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# # # for i in l:
# # #     for j in i:
# # #         sorted()
# # # print(l)
# # # def last(n): return n[1]
# # #
# # # def sort_list_last(tuples):
# # #   return sorted(tuples, key=last,reverse=False)
# # #
# # # print(sort_list_last([(2,3, 5), (1,8, 2), (4,5, 4), (2,6, 3), (2,7, 1)]))
# # # l=[10,20,30,20,50,60,40,80,50,40]
# # # l1=[]
# # # for i in l:
# # #     if i not in l1:
# # #         l1.append(i)
# # # print(sorted(l1))
# # # l = []
# # # if not l:
# # #   print("List is empty")
# # # l=[10,20,30,40,50]
# # # l1=list(l)
# # # print(l1)
# # # t=[(1,2),(5,1),(6,0),(3,5)]
# # # for i in range(0,len(t)):
# # #     for j in range(i):
# # #         if t[j][-1]<t[j+1][-1]:
# # #             continue
# # #         else:
# # #             t[j],t[j + 1]= t[j],t[j+1]
# # # print(t)
# # # l=[1,2,3,4,5]
# # # print(l)
# # # l1=l.copy()
# # # print(l1)
# # # str="the quick brown fox jumps over the lazy dog"
# # # l1=[]
# # # l=str.split(" ")
# # # for x in l:
# # #     if len(x)>4:
# # #         l1.append(x)
# # # print(l1)
# # # print(",".join(l1))
# # # l=[1,2,3,4,5]
# # # l1=[6,7,8,9,1]
# # # for i in l:
# # #     if i in l1:
# # #         print(True)
# # #         break
# # # else:
# # #     print(None)
# # # def common_data(list1, list2):
# # #     result = False
# # #     for x in list1:
# # #         for y in list2:
# # #             if x == y:
# # #                 result = True
# # #                 return result
# # # print(common_data([1, 2, 3, 4, 5], [5, 6, 7, 8, 9]))
# # # print(common_data([1, 2, 3, 4, 5], [6, 7, 8, 9]))
# # # l=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# # # l1=[]
# # # for i,x in enumerate(l):
# # #     if i not in(0,4,5):
# # #         l1.append(x)
# # # print(l1)
# # # array=[[[]]]
# # # for i in range(6):
# # #     for j in range(4):
# # #         for k in range(3):
# # # array = [[ ['python' for col in range(6)] for col in range(4)] for row in range(3)]
# # # print(array)
# # # from random import shuffle
# # # color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# # # shuffle(color)
# # # print(color)
# # # l = []
# # # for i in range(1,31):
# # #     l.append(i**2)
# # # print(l[5:])
# # # import itertools
# # # print(list(itertools.combinations_with_replacement([1,2,3],r=3)))
# # # l1 = [1, 3, 5, 7, 9]
# # # l2=[1, 2, 4, 6, 7, 8]
# # # dl1=list(set(l1)-set(l2))
# # # dl2=list(set(l2)-set(l1))
# # # l3=dl1+dl2
# # # print(l3)
# # # l=[1,2,3,4,5,6,7,8,9]
# # # for i,x in enumerate(l):
# # #     print(i,x)
# # # s=["s","u","k","a","n","y","a"]
# # # s1="".join(s)
# # # print(s1)
# # # num =[10, 30, 4, -6]
# # # print(num.index(30))
# # # import itertools
# # # original_list = [[2,4,3],[1,5,6], [9], [7,9,0]]
# # # new_merged_list = list(itertools.chain(*original_list))
# # # print(new_merged_list)
# # # list1 = [10, 10, 0, 0, 10]
# # # list2 = [10, 10, 10, 0, 0]
# # # list3 = [1, 10, 10, 0, 0]
# # #
# # # print('Compare list1 and list2')
# # # print(' '.join(map(str, list2)) in ' '.join(map(str, list1 * 2)))
# # # print('Compare list1 and list3')
# # # print(' '.join(map(str, list3)) in ' '.join(map(str, list1 * 2)))
# # # l=[4,4,5,2,8,9,1,0,-5,-9]
# # # u_items=[]
# # # d_items=set()
# # # if len(l)<2:
# # #     print(l)
# # # if len(l)>=2:
# # #     for x in l:
# # #         if x not in d_items:
# # #             u_items.append(x)
# # #             d_items.add(x)
# # #     print(d_items)
# # #     print(u_items)
# # #     u_items.sort()
# # #     print(u_items)
# # #     print(u_items[-2])
# # # l=[10, 20, 30, 40, 20, 50, 60, 40]
# # # l1=list(sorted(set(l)))
# # # for i in l:
# # #     if i not in l1:
# # #         l1.append(i)
# # # print(l1)
# # # a=int(input("age"))
# # # if False:
# # #     print("eligible to vote")
# # # else:
# # #     print("No")
# # # l=[10,10,10,10,20,20,20,20,40,40,50,50,30]
# # # print(l)
# # # d={}
# # # for i in l:
# # #     if i in d:
# # #         d[i]+=1
# # #     else:
# # #         d[i]=1
# # # print(d)
# # # l=[10, 20, 30, 40, 40, 40, 70, 80, 99]
# # # c=0
# # # min=1
# # # max=6
# # # for i in range(len(l)):
# # #     if min<=i<=max:
# # #         c+=1
# # # print(c)
# # # lst1=[1,2,3,4,5,6]
# # # lst2=[3,2,4,]
# # # ls1 = [element for element in lst1 if element in lst2]
# # # ls2 = [element for element in lst2 if element in lst1]
# # # if ls1 == ls2:
# # #     print(True)
# # # else:
# # #     print(False)
# # # def sub_lists(l):
# # #     lists = [[]]
# # #     for i in range(len(l) + 1):
# # #         for j in range(i):
# # #             lists.append(l[j: i])
# # #     return lists
# # #     # driver code
# # # l1 = [1, 2, 3]
# # # print(sub_lists(l1))
# # # def prime_eratosthenes(n):
# # #     prime_list = []
# # #     for i in range(2, n+1):
# # #         if i not in prime_list:
# # #             print (i)
# # #             for j in range(i*i, n+1, i):
# # #                 prime_list.append(j)
# # #     print(prime_list)
# # # print(prime_eratosthenes(100));
# # # for i in range(2,100):
# # #     for j in range(2,i):
# # #         if i%j==0:
# # #             break
# # #     else:
# # #         print(i)
# # # x = 100
# # # print(format(id(x)),'x')
# # # s = 'w3resource'
# # # print(format(id(s)),'s')
# # # color1 = ["Red", "Green", "Orange", "White"]
# # # color2 = ["Black", "Green", "White", "Pink"]
# # # print(set(color1)& set(color2))
# # # x=5
# # # x&=12
# # # print(x)
# # # l=[33,15,50]
# # # x=int("".join(map(str,l)))
# # # print(x)
# # # d={}
# # # for i in range(1,21):
# # #     d[str(i)]=[]
# # # print((d))
# # # list1 = ['a','b','c','d','e','f']
# # # list2 = ['d','e','f','g','h']
# # # print('Missing values in second list: ',','.join(set(list1).difference(list2)))
# # # print('Additional values in second list: ',','.join(set(list2).difference(list1)))
# # # color = [("Black", "#000000", "rgb(0, 0, 0)"), ("Red", "#FF0000", "rgb(255, 0, 0)"),
# # #          ("Yellow", "#FFFF00", "rgb(255, 255, 0)")]
# # # var1, var2, var3 = color
# # # print(var2)
# # # print(var1)
# # # print(var3)
# # # l=[1,2,3,4,5]
# # # for i in l:
# # #     print(i,end=" ")
# # # l=[]
# # # for i in range(5):
# # #     l.append({})
# # # print(l)
# # # x = [(4, 1,5), (1, 2,3), (6, 0,7)]
# # # print(max(x, key=lambda n: (n[1])))
# # # s="Red,Green,White"
# # # l=s.split(",")
# # # print(l)
# # # l=['red', 'green', 'orange']
# # # for i in l:
# # #     print(i,end="")
# # # l1 = ["red", "orange", "green", "blue", "white"]
# # # l2 = ["black", "yellow", "green", "blue"]
# # # l3=list(set(l1).difference(l2))
# # # print(l3)
# # # l4=list(set(l2).difference(l1))
# # # print(l4)
# # # l=[3,4,0,0,0,6,2,0,6,7,6,0,0,0,9,10,7,4,4,5,3,0,0,2,9,7,1]
# # # l1=[]
# # # l2=[]
# # # for i in l:
# # #     if i==0:
# # #         l2.append(i)
# # #     else:
# # #         l1.append(i)
# # # print(l1)
# # # print(l2)
# # # l1.extend(l2)
# # # print(l1)
# # # n=12345
# # # c=0
# # # while(n>0):
# # #     c+=1
# # #     n= n//10
# # # print(c)
# # # a=7
# # # k=0
# # # for i in range(2,a//2+1):
# # #     if(a%i==0):
# # #         k=k+1
# # # if(k<=0):
# # #     print("prime mnumber")
# # # else:
# # #     print("not prime number")
# # # n=467
# # # a=list(map(int,str(n)))
# # # b=list(map(lambda x:x**3,a))
# # # if sum(b)==n:
# # #     print("Armstrong number")
# # # else:
# # #     print("not arm strong number")
# # # n=9
# # # c=0
# # # for i in range(1,n):
# # #     if n%i==0:
# # #         c+=i
# # # if n==c:
# # #     print("perfect number")
# # # else:
# # #     print("not perfect number")
# # # a=[]
# # # n=int(input("Enter number of elements:"))
# # # for i in range(1,n+1):
# # #     b=int(input("Enter element:"))
# # #     a.append(b)
# # # a.sort()
# # # print("Second largest element is:",a[-2])
# # # l=[1,2,3,4,5,6]
# # # for i in range(len(l)-1):
# # #    l[i],l[i+1]=l[i+1],l[i]
# # # print(l)
# # # l=[1,2,3,4,5,6]
# # # c=l[0]
# # # l[0]=l[-1]
# # # l[-1]=c
# # # print(l)
# # # s="sukanya"
# # # if s==s[::-1]:
# # #     print("polyndrome")
# # # else:
# # #     print("not polyndrome")
# # # string=input("Enter string:")
# # # vowels=0
# # # for i in string:
# # #     if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
# # #         vowels=vowels+1
# # # print("Number of vowels are:")
# # # print(vowels)
# # # s1=input("Enter first string:")
# # # s2=input("Enter second string:")
# # # a=list(set(s1)&set(s2))
# # # print("The common letters are:")
# # # for i in a:
# # #     print(i,end=" ")
# # # s="abcdefghi"
# # # s1="".join([s[x:x+3][::-1]for x in range(0,len(s),3)])
# # # print(s1)
# # # sum=0
# # # num=1466789
# # # temp=num
# # # while(num):
# # #     i=1
# # #     f=1
# # #     r=num%10
# # #     while(i<=r):
# # #         f=f*i
# # #         i=i+1
# # #     sum=sum+f
# # #     num=num//10
# # # if sum==temp:
# # #     print("strong number")
# # # else:
# # #     print("not strong number")
# # # t=(1,2,3,4,5)
# # # l=[]
# # # for i in t:
# # #     if i==3:
# # #         pass
# # #     else:
# # #         l.append(i)
# # # print(tuple(l))
# # # t=(1,2,3,4,5)
# # # print("this is a tuple",t)
# # # l = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
# # # l1=[]
# # # for t in l:
# # #     t1=t[:-1]+(100,)
# # #     l1.append(t1)
# # # print(l1)
# # # l = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
# # # l1=[]
# # # for t in l:
# # #     if t==():
# # #         pass
# # #     else:
# # #         l1.append(t)
# # # print(l1)
# # # s="python 3.0"
# # # t=[]
# # # for x in s:
# # #     if not x.isspace():
# # #         t.append(x)
# # # print(tuple(t))
# # # t=(2, 4, 8, 8, 3, 2, 9)
# # # l=list(t)
# # # c=1
# # # for i in l:
# # #     c*=i
# # # print(c)
# # # t=((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
# # # l=list(t)
# # # l1=[]
# # # for x in zip(*l):
# # #     s=sum(x)/len(x)
# # #     l1.append(s)
# # # print(tuple(l1))
# # # t=(('333', '33'), ('1416', '55'))
# # # l=[]
# # # for x in t:
# # #     s=int(x[0]),int(x[1])
# # #     l.append(s)
# # # print(tuple(l))
# # # t=(10,20,40,50,70)
# # # s="".join(map(str,t))
# # # print(int(s))
# # # t= (('Red', 'White', 'Blue'),('Green', 'Pink', 'Purple'),('Orange', 'Yellow', 'Lime'))
# # # l= [(1,2), (2,3,5), (3,4), (2,3,4,2)]
# # # l2=[]
# # # for i in l:
# # #     s=list(i)
# # #     l2.append(s)
# # # print(l2)
# # # num_set = set([0, 1, 3, 4, 5])
# # # print("Original set:")
# # # print(num_set)
# # # num_set.remove(3)
# # # print("\nAfter removing the first element from the said set:")
# # # print(num_set)
# # # import operator
# # # d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# # # print(sorted(d.items(),reverse=True))
# # # dic1={1:10, 2:20}
# # # dic2={3:30, 4:40}
# # # dic3={5:50,6:60}
# # # dic4 = {}
# # # for d in (dic1, dic2, dic3):
# # #     dic4.update(d)
# # # print(dic4)
# # # d1 = {'a': 100, 'b': 200}
# # # d2 = {'x': 300, 'y': 400}
# # # d = d1.copy()
# # # print(d)
# # # d.update(d2)
# # # print(d)
# # # d = {'Red': 1, 'Green': 2, 'Blue': 3}
# # # for color_key, value in d.items():
# # #      print(color_key, 'corresponds to ',value)
# # # d={'data1':100,'data2':-54,'data3':247}
# # # c=0
# # # for i in d.values():
# # #     c+=i
# # # print(c)
# # # keys = ['red', 'green', 'blue']
# # # values = ['#FF0000','#008000', '#0000FF']
# # # color_dictionary = dict(zip(keys, values))
# # # print(color_dictionary)
# # # color_dict = {'red': '#FF0000',
# # #               'green': '#008000',
# # #               'black': '#000000',
# # #               'white': '#FFFFFF'}
# # # for key in sorted(color_dict):
# # #     print(key,":",color_dict[key])
# # # d={'x':500, 'y':5874, 'z': 560}
# # # print(max(d.values()))
# # # print(min(d.values()))
# # # d={'id1':
# # #    {'name': ['Sara'],
# # #     'class': ['V'],
# # #     'subject_integration': ['english, math, science']
# # #    },
# # #  'id2':
# # #   {'name': ['David'],
# # #     'class': ['V'],
# # #     'subject_integration': ['english, math, science']
# # #    },
# # #  'id3':
# # #     {'name': ['Sara'],
# # #     'class': ['V'],
# # #     'subject_integration': ['english, math, science']
# # #    },
# # #  'id4':
# # #    {'name': ['Surya'],
# # #     'class': ['V'],
# # #     'subject_integration': ['english, math, science']
# # #    },
# # # }
# # # d1={}
# # # for i,j in d.items():
# # #     if j not in d1.values():
# # #         d1[i]=j
# # # print(d1)
# # # from collections import Counter
# # # d1 = {'a': 100, 'b': 200, 'c':300}
# # # d2 = {'a': 300, 'b': 200, 'd':400}
# # # d = Counter(d1) + Counter(d2)
# # # print(d)
# # # l=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# # # l1=[]
# # # for dic in l:
# # #     for val in dic.values():
# # #         l1.append(val)
# # # print(set(l1))
# # # import itertools
# # # d ={'1':['a','b'], '2':['c','d']}
# # # l=[]
# # # for combo in itertools.product():
# # #     for k in sorted(d.keys()):
# # #         a=''.join(combo)
# # #         l.append(a)
# # # s="w3resource"
# # # d={}
# # # for i in s:
# # #     if i in d:
# # #         d[i]+=1
# # #     else:
# # #         d[i]=1
# # # print(d)
# # # dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# # # print("key  value  count")
# # # for count, (key, value) in enumerate(dict_num.items(), 1):
# # #     print(key,'   ',value,'    ', count)
# # # s="Datascience"
# # # t=s.upper()
# # # print(t)
# # # l=[]
# # # for i in range(len(s)):
# # #     if i%2==0:
# # #         l.append(t[i])
# # #     else:
# # #         l.append(s[i])
# # # print(l)
# # # print("".join(l))
# # # s="pallavi"
# # # s2="sukanya"
# # # print(s2[:3]+s[:]+s2[3:])
# # # print(bool(""))
# # # range(10)
# # # print(range)
# # # s="this is\"symbol"
# # # print(s)
# # # x=0
# # # y=10
# # # print(x or y)
# # # print(~7)
# # # print(10<<2)
# # # print(~1)
# # # s="durga"
# # # list=[10,20,30,40]
# # # print("hello %s ..... the list elements are %s" %(s,list))
# # # n=int(input("enter a number"))
# # # sum=0
# # # i=1
# # # while i<=n:
# # #    sum=sum+i
# # #    i+=1
# # # print("the sum of first",n,"numbers is:",sum)
# # # print(4&5)
# # # name=""
# # # while name!="durga":
# # #    name=input("enter a name:")
# # # print("thanks for information")
# # # i=0
# # # while False:
# # #    i+=1
# # #    print("hello",i)
# # # n=int(input("enter a number"))
# # # for i in range(1,n+1):
# # #    for j in range(1,i+1):
# # #       print("*",end=" ")
# # #    print()
# # # n=int(input("enter a number:"))
# # # for i in range(1,n+1):
# # #    print(" "*(n-i),end="")
# # #    print("* "*i)
# # # s="durga"
# # # s=None
# # # print(s)
# # # s = 'sukanya'
# # # s1 = s[0:len(s):2]
# # # a = s1.upper()
# # # print(a)
# # # s2 = s[1:len(s):2]
# # # print(s2)
# # # s3 = ''
# # # for i in range(len(s2)):
# # #     s3 = s3+(a[i]+s2[i])
# # # print(s3)
# # # s="abbababababacdefg"
# # # sub="a"
# # # d=len(s)
# # # while True:
# # #     a=s.find(sub,d)
# # #     if a==-1:
# # #         break
# # #     print(a)
# # # s='fkhdfskhfdg'
# # # i=0
# # # while i<len(s):
# # #     if s[i]=='f':
# # #         print(i)
# # #     i+=1
# # # print("abc123".islower())
# # # s="sukanya"
# # # s1=s.split()
# # # s1="".join(reversed(s))
# # # print(s1)
# # # s1=""
# # # for i in range(len(s)):
# # #     s1=s[i]+s1
# # # print(s1)
# # # s="sukanya"
# # # i=0
# # # s1=""
# # # while i<=len(s)-1:
# # #     s1=s[i]+s1
# # #     i=i+1
# # # print(s1)
# # # s="Durga software solutions"
# # # l=s.split()
# # # l1=[]
# # # i=0
# # # while i<=len(l)-1:
# # #     l1.append(l[i][::-1])
# # #     i=i+1
# # # output=" ".join(l1)
# # # print(output)
# # # s1="ravisri"
# # # s2="tejasri"
# # # s3=""
# # # for i in range(len(s1)):
# # #     s3+=s1[i]+s2[i]
# # # print(s3)
# # # s="B4A1D3"
# # # s1=s2=s3=""
# # # for x in s:
# # #     if x.isalpha():
# # #         s1+=x
# # #     else:
# # #         s2+=x
# # # for x in sorted(s1):
# # #     s3+=x
# # # for x in sorted(s2):
# # #     s3+=x
# # # print(s3 )
# # # s="s3u2k4n6y2a5"
# # # s1=""
# # # for x in s:
# # #     if x.isalpha():
# # #         s1+=x
# # #         p=x
# # #     else:
# # #         s1+=p*(int(x)-1)
# # # print(s1)
# # # s="a4b3c4d5"
# # # k=""
# # # for i in range(len(s)):
# # #     if s[i].isalpha():
# # #       continue
# # #     else:
# # #
# # # print(k)
# # # print(chr(1000))
# # # print("float value with sign:{:+f}".format(123.456))
# # # t=(1,2,3)
# # # t1=3*t
# # # print(t1)
# # # s={1,2}
# # # s.update(range(0,10))
# # # print(s)
# # # s="google.com"
# # # d={}
# # # for i in s:
# # #     if i in d:
# # #         d[i]+=1
# # #     else:
# # #         d[i]=1
# # # print(d)
# # # s="sukanya"
# # # c=0
# # # for i in s:
# # #     c+=1
# # # print(c)
# # # s="sukanya"
# # # s1=""
# # # if len(s)<2:
# # #     print("")
# # # else:
# # #     s1=s[0:2]+s[-2:]
# # # print(s1)
# # # s={'e','d','u','c','a','t','i','o','n'}
# # # v={'a','e','i','o','u'}
# # # d=s.intersection(v)
# # # print(d)
# # # A = {'s', 'u', 'n', 'n', 'y'}
# # # B = {'b', 'u', 'n', 'n', 'y'}
# # #
# # # # result is always none.
# # # result = A.symmetric_difference_update(B)
# # # print(A-B)
# # # print(B-A)
# # # print(A^B)
# # # print(B^A)
# # # print('A = ', A)
# # # print('B = ', B)
# # # print('result = ', result)
# # # A={1,2,3,4,5}
# # # B={4,5,6,7,8}
# # # print(A.symmetric_difference_update(B))
# # # print(A.difference_update(B))
# # # class Vehicle:
# # #     def __init__(self, max_speed, mileage):
# # #         self.max_speed = max_speed
# # #         self.mileage = mileage
# # #
# # # modelX = Vehicle(240, 18)
# # # print(modelX.max_speed, modelX.mileage)
# # # class Vehicle:
# # #     pass
# # # class Vehicle:
# # #
# # #     def __init__(self, name, max_speed, mileage):
# # #         self.name = name
# # #         self.max_speed = max_speed
# # #         self.mileage = mileage
# # # class Bus(Vehicle):
# # #     pass
# # # obj=Bus("Volvo",100,18)
# # # print("Bus Details:")
# # # print(obj.name,obj.max_speed,obj.mileage)
# # # class Vehicle:
# # #     def __init__(self,name,speed,mileage):
# # #         self.name=name
# # #         self.speed=speed
# # #         self.mileage=mileage
# # #     # def seating_capacity(self,capacity):
# # #     #     self.capacity=capacity
# # #     #     print(self.name,capacity)
# # # class Bus(Vehicle):
# # #     def seating_capacity(self,capacity=50):
# # #         # super().seating_capacity(capacity=50)
# # #         print(sr)
# # #
# # # obj=Bus("Volvo",100,13)
# # # obj.seating_capacity()
# #
# # # class Test:
# # #  a=10
# # #  def __init__(self):
# # #      Test.b=20
# # #      del Test.a
# # #  def m1(self):
# # #      Test.c=30
# # #      del Test.b
# # #  @classmethod
# # #  def m2(cls):
# # #      cls.d=40
# # #      del Test.d
# # #  @staticmethod
# # #  def m3():
# # #      Test.e=50
# # #      del Test.d
# # # print(Test.__dict__)
# # # t=Test()
# # # print(Test.__dict__)
# # # t.m1()
# # # print(Test.__dict__)
# # # Test.m2()
# # # print(Test.__dict__)
# # # Test.m3()
# # # print(Test.__dict__)
# # # Test.f=60
# # # print(Test.__dict__)
# # # del Test.e
# # # print(Test.__dict__)
# # # class Test:
# # #     a=10
# # #     def m1(self):
# # #         Test.b=22
# # #         del Test.a
# # # t1=Test()
# # # print(t1.__dict__)
# # # class Test:
# # #  count=0
# # #  def __init__(self):
# # #      Test.count =Test.count+1
# # #  @classmethod
# # #  def noOfObjects(cls):
# # #      print('The number of objects created for test class:',cls.count)
# # #
# # # t1=Test()
# # # t2=Test()
# # # Test.noOfObjects()
# # # t3=Test()
# # # t4=Test()
# # # t5=Test()
# # # Test.noOfObjects()
# # # s={'s','u','n','n','y'}
# # # p={'b','u','n','n','y'}
# # # s=s.symmetric_difference(p)
# # # print(s)
# # # # s.symmetric_difference_update(p)
# # # # print(s)
# # # def decor1(func):
# # #     def inner():
# # #         x=func()
# # #         return x*x
# # #     return inner
# # # def decor(func):
# # #     def inner():
# # #         x=func()
# # #         return 2*x
# # #     return inner
# # # @decor
# # # @decor1
# # # def num():
# # #     return 10
# # # print(num())
# # # def decor1(func):
# # #  def inner(name):
# # #      print("First Decor(decor) Function Execution")
# # #      func(name)
# # #  return inner
# # #
# # # def decor(func):
# # #  def inner(name):
# # #      print("Second Decor(decor1) Execution")
# # #      func(name)
# # #  return inner
# # #
# # # @decor1
# # # @decor
# # # def wish(name):
# # #     print("Hello",name,"Good Morning")
# # #
# # # wish("Durga")
# # # f=open("C:\\Users\\sukan\\OneDrive\\Documents\\sukku.txt","w")
# # # f.write("I am very good girl")
# # # with open("C:\\Users\\sukan\\OneDrive\\Documents\\sukku.txt","a+") as f:
# # # print(f.read())
# # # f.write(" I am very lazy person")
# # # print(f.read())
# # # f.write("I came from nellore")
# # # with open("C:\\Users\\sukan\\OneDrive\\Documents\\sukku.txt","a+") as f:
# # #     f.write("durga\n")
# # #     f.write("software\n")
# # #     f.write("solutions\n")
# # #     print("is file closed:",f.closed)
# # # print("is file closed:",f.closed)
# # # f=open("C:\\Users\\sukan\\OneDrive\\Documents\\sukku.txt","r")
# # # print(f.tell())
# # # f.seek(0)
# # # print(f.read())
# # # import os,sys
# # # os.path.isfile("C:\\Users\\sukan\\OneDrive\\Documents\\sukku.txt")
# # # def sub_div(func):
# # #     def inner(a,b):
# # #         if a<b:
# # #             a,b=b,a
# # #             return func(3,4)
# # #
# # #     return inner(3,4)
# # # @sub_div
# # # def div(a,b):
# # #     print(a/b)
# # # f=open(sukku.txt,"r")
# # # lines=f.readlines()
# # # print(lines)
# # # f.close()
# # # l=['neeraja','sindhu','mounika']
# # # l2=[]
# # # for i in l:
# # #     i1=i.capitalize()
# # #     l2.append(i1)
# # # print(l2)
# # # list=[i.title()for i in l]
# # # print(list)
# # # from abc import*
# # # class CollegeAutomation(ABC):
# # #     @abstractmethod
# # #     def m1(self):
# # #         pass
# # #     @abstractmethod
# # #     def m2(self):
# # #         pass
# # #     @abstractmethod
# # #     def m3(self):
# # #         pass
# # # class AbsCls(CollegeAutomation):
# # #     def m1(self):
# # #         print('m1 method implementation')
# # #     def m2(self):
# # #         print('m2 method implementation')
# # #
# # # class ConcreteCls(AbsCls):
# # #     def m3(self):
# # #         print('m3 method implementation')
# # # c=ConcreteCls()
# # # c.m1()
# # # c.m2()
# # # c.m3()
# # # class Test:
# # #     x=10
# # #     _y=20
# # #     __z=30
# # #     def m1(self):
# # #         print(Test.x)
# # #         print(Test._y)
# # #         print(Test.__z)
# # # t=Test()
# # # t.m1()
# # # print(Test.x)
# # # print(Test._y)
# # # print(Test.__z)
# # # class Test:
# # #     def __init__(self):
# # #         self.__x=10
# # # t=Test()
# # # print(t._Test__x)
# # # import csv
# # # with open("tweak.csv","w",newline="")as f:
# # #     w=csv.writer(f)
# # #     w.writerow(["ENO","ENAME","ESAL","EADDR"])
# # #     n=int(input("enter no of employees:"))
# # #     for i in range(n):
# # #         eno=input("eno:")
# # #         ename=input("ename:")
# # #         esal=input("esal:")
# # #         eaddr=input("eaddr:")
# # #         w.writerow([eno,ename,esal,eaddr])
# # # print("total employees data created successfully")
# # # import csv
# # # f=open("tweak.csv","r")
# # # r=csv.reader(f)
# # # data=list(r)
# # # # print(data)
# # # for line in data:
# # #     for word in line:
# # #         print(word,"\t",end="")
# # #     print()
# # # import os
# # # cwd=os.getcwd()
# # # print("current working directory",cwd)
# # # import os
# # # os.mkdir("my sub/my sub2")
# # # print("my sub2  created in mysub")
# # # class Test:
# # #     def __init__(self,a):
# # #         self.a=a
# # #     def __add__(self,b):
# # #         return  self.a+b.a
# # # t=Test(200)
# # # t1=Test(300)
# # # print(t+t1)
# # from math import *
# # print(sqrt(4))
# # print(ceil(10.0))
# # print(floor(10.1))
# # print(fabs(-10.4))
# # print(fabs(10.9))
# # import math
# # help(math)
# # from random import*
# # list=["sunny","bunny","chinny","vinny","pinny"]
# # for i in range(10):
# #     print(choice(list))
# # from random import*
# # for i in range(10):
# #     print(random())
# # s="veeksha"
# # s1=""
# # for i in range(len(s)//2):
# #     s1=(s[i]+s[len(s)-1-i])+s1
# #
# # print(s1)
# # s="veeksha"
# # s1=""
# # for i in range(len(s)//2):
# #     s1=s1+(s[len(s)-i-1]+s[i])
# # if (len(s)//2)!=0:
# #     j=len(s)//2
# #     s1+=s[j]
# # print(s1)
# ##
# # d={'a':1,'b':2,'c':3,3:'c','c':'c'}
# # print(d)
# # d={values:key for key,values in d.items()}
# # print(d)
# ##
# # l=[1,2,3,4,5]
# # print(l)
# # print(type(l))
# # print(l[::-1])
# # s="a4b3c5d4"
# # k=""
# # for i in s:
# #     if i.isalpha():
# #         k+=i
# #         i1=i
# #     else:
# #         k=k+i1*(int(i)-1)
# # print(k)
# # s="3b4e6g8d"
# # k=""
# # for i in s:
# #     if i.isdigit():
# #         i1=i
# #     else:
# #         i2=i*int(i1)
# #         k+=i2
# # print(k)
# # l=[1,2,3,4,5]
# # l2=[]
# # for i in l:
# #     l2.insert(0,i)
# # print(l2)
#
# class parent(object):
#     x=1
#
# class Child1(parent):
#     pass
# class Child2(parent):
#     pass
# print (parent.x,Child1.x.Child2.x)
# Child1.x = 2
# print (parent.x,Child1.x.Child2.x)
# parent.x = 3
# print (parent.x,Child1.x.Child2.x)

# import collections
# def so(s):
#     c=collections.Counter(s)
#     for idx,ch in enumerate(s):
#         if c[ch] == 1:
#             return idx
#     return -1
# print(so('alphabet'))
# print(so('barbados'))
# print(so('crunchy'))
# import unittest
# async def logs(count,name):
#     conn=aiohttp.UnixConnector(path="/var/run/docker.sock")
#     async with aiohttp.ClientSession(connector=conn) as session:
#         async with session.get(f"http://xx/containers/{cont}/log?follow=1&stdout=1") as resp:
#             async for line in resp.content:
#                 print(name,line)
#
# s='sss aaaa'
# d=dict()
# for i in s:
#     if i not in d:
#         d[i]=1
#     else:
#         d[i]+=1
# for k,v, in d.items():
#     print(k,v, sep=":")
# s="sukanya is a good girl"
# s1=""
# l=s.split()
# l1=[]
# for i in l:
#     l1.insert(0,i)
#     print(l1)
# s1=" ".join(l1)
# print(s1)
# s="sukanya is a good girl"
# s1=s[::-1]
# print(s1)
# def solution(l):
#     max=0
#     for s in l:
#         if len(s)>max:
#             max=len(s)
#     res=[]
#     for s in l:
#         if len(s)==max:
#             res.append(s)
# #    s1=i+s1
# print(s1)

# l1=[1,2,3,4,5]   return res
# # # solution(
# # # )
# # # s='pallavi'
# # s1=" "
# # for i in s:
# x=sum(l1)
# print(x)
# l=[1,2,3,4,5]
# sum=0
# for i in l:
#     sum=sum+i
# print(sum)
# x=input("True")
# type(x)
# l1=56
# print(id(l1))
# l1=10
# print(id(l1))
# print(l1 is l1)
# s="ravii"
# s1="tejag"
# s3=""
# for i in range(len(s)):
#     s3=s3+s[i]+s1[i]
# print(s3)
# a=10
# b=20
# c=30
# t=a,b,c
# print(t)
# print(type(t))
# t=(10,20,30)
# a,b,c=t
# print(a)
# print(b)
# print(c)
# i=1
# while i<5:
#     print(i)
#     if i==3:
#         break
#     i+=1
# s="pullonly"
# s1=""
# for i in s:
#
#     if i=="l":
#          break
#     s1+=i
# print(s1)
# l=[1,2,3,4,5]
# l1=[i*3 for i in l if i==2]
# print(l1)
# d={'a':1,'b':2,'c':3}
# d1={keys:values+2 for keys,values in d.items()}
# print(d1)
# POLYNDROME:
# s="radar"
# print(s)
# s1=s[::-1]
# print(s1)
# if s==s1:
#     print("polyndrome")
# else:
#     print("not polyndrome")
# REMOVE DUPLICATES:
# s="sukanyeasrtaccce"
# s1=""
# for i in s:
#     if i not in s1:
#         s1+=i
# print(s1)
# ARMSTRONG NUMBER:
# num=int(input("enter a number:"))
# order=len(str(num))
# sum=0
# n=num
# while n>0:
#     remainder=n%10
#     sum=sum+remainder**order
#     n=n//10
# if num==sum:
#     print("armstrong number")
# else:
#     print("not armstrong number")
# CHECKING A PRIME NUMBER:
# n=int(input("enter a number:"))
# for i in range(2,(n//2)+1):
#     if n%i==0:
#         print("not prime number")
#         break
# else:
#     print("prime number")
# s="ashokvamsirajkumarvishnu"
# s1="aeiou"
# s4=""
#
# for i in s:
#     for i in s1:
#         s3=s.replace(i,'@')
#         s4+=s3
# print(s3)
# print(s4)
# t=(x**2 for x in range(1,6))
# print(type(t))
# for x in t:
#     print(x)
# n=15351
# s=0
# n1=n
# while n1>0:
#     r=n1%10
#     s=s*10+r
#     n1=n1//10
# print(s)
# if n==s:
#     print("polyndrome")
# else:
#     print("not polyndrome")
# n=5
# for i in range(n):
#     for j in range(n):
#         if j>=n-1-i:
#             print("*",end="")
#         else:
#             print("-",end="")
#     print()
# n=5
# for i in range(n):
#     for j in range(n):
#         if j<=n-1-i:
#             print("*",end="")
#         else:
#             print("-",end="")
#     print()
# n=5
# for i in range(n):
#     for j in range(n):
#         if j>=i:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()
# n=5
# for i in range(n):
#     for j in range(n):
#         if j>=n-i-1:
#             print("*",end="")
#         else:
#             print("-",end="")
#     for j in range(n):
#         if j<=i-1:
#             print("*", end="")
#     print()
import unzip as unzip

n=5
# for i in range(n):
#     for j in range(n):
#         if j>=i:
#             print("*",end="")
#         else:
#             print("-",end="")
#     for j in range(n):
#         if j<=n-1-i-1:
#             print("*", end="")
#     print()
# for i in range(n):
#     for j in range(n):
#         if i==0 or j==i:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     for j in range(n-1):
#         if i==0 or j==n-i-1-1:
#             print("*", end="")
#         else:
#             print(" ",end="")
#     print()
# for i in range(n):
#     for j in range(n):
#         if i==n-1 or j==n-i-1-1:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     for j in range(n-1):
#         if i==n-1 or j==i-1:
#             print("*", end="")
#         else:
#             print(" ",end="")
#     print()
# n=5
# for i in range(n):
#     for j in range(n):
#         if j>=n//2-i and j<=n//2+i and j>=i-n//2 and j<=n+n//2-1-i:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()
# for i in range(n):
#     for j in range(n-i-1):
#         print("-",end="")
#     for j in range(i+1):
#         print("*",end="")
#     for j in range(i):
#         print("*",end="")
#
# #     print()
# n=5
# for i in range(n):
#     for j in range(n - i - 1):
#         print("-", end="")
#     for j in range(i + 1):
#         print("*", end="")
#     for j in range(i):
#         print("*", end="")
#     for j in range(n - i - 1):
#         print("-", end="")
#     for j in range(n - i - 1-1):
#         print("-", end="")
#     for j in range(i + 1):
#         print("*", end="")
#     for j in range(i):
#         print("*", end="")
#
#     print()
# n=5
# for i in range(n-1):
#     for j in range(n - i - 1):
#         print(" ", end="")
#     for j in range(i + 1):
#         print("*", end="")
#     for j in range(i):
#         print("*", end="")
#     print()
# for i in range(n):
#     for j in range(n):
#             print("*",end="")
#     for j in range(n-1):
#         print("*",end="")
#     print()
# n=5
# for i in range(n):
#     for j in range(n-1):
#         print(" ",end="")
#     for j in range(n - i - 1):
#         print(" ", end="")
#     for j in range(i + 1):
#         print("*", end="")
#     for j in range(i):
#         print("*", end="")
#     print()
# for i in range(n):
#     for j in range(n-1):
#         print(" ",end="")
#     for j in range(n):
#             print("*",end="")
#     for j in range(n):
#         print("*",end="")
#     print()
# for i in range(n):
#     for i in range(n-1-i):
#         print("-",end="")
#     for j in range(i+1):
#         print("*",end="")
#     for j in range(n):
#         print("*",end="")
#     for j in range(n):
#         print("*",end="")
#     for j in range(i-1):
#         print("*",end="")
#     print()
# def fun(s):
#    print(s.upper())
# fun("haritha")

# def fun1(fun):
#    print(fun1)
# fun1("sukanya")
# @fun1
# def fun(s):
#    print(s.upper())
#    fun("haritha")
# rows=5
# for i in range(rows):
#    for j in range(i):
#       print(i,end="")
#    print()
# s="{[()]}"
# l=[]
# for i in s:
#    if i=="[" or i=="{" or i=="(":
#       l.append(i)
#
#    elif l[-1]+i=="[]" or l[-1]+i=="()" or l[-1]+i=="{}":
#       l.pop()
# print(l)
# l1=[1,2,3,4,5]
# l2=[6,7,8,9,10]
# l3=list(zip(l1,l2))
# print(l3)
# l4=list(zip(l3))
# l=[1,2,3,4,5,6,6,3,2,7,8,9,0]
# l1=[]
# for i in l:
#     if i not in l1:
#         l1.append(i)
# print(l1)
# l=[2,3,4,1,8,5,6,7]
# for i in range(len(l)):
#     for j in range(len(l)-1):
#         if l[j]>l[j+1]:
#             l[j],l[j + 1]=l[j+1],l[j]
# print(l)
# print(l[-1])
# print(l[-2])
# temp=l[0]
# l[0]=l[-1]
# l[-1]=temp
# print(l)
# l=[1,2,2,2,3,3,3,4,4,4,4,5,5,5,5,5]
# d={}
# for i in l:
#     if i not in d:
#         d[i]=1
#     else:
#         d[i]+=1
# print(d)
# l1=[]
# for i,j in d.items():
#     l1.append((i,j))
# print(sorted(l1))
# a=list(set(list(d.values())))
# print(a)
# x=a[-3]
# for i,j in d.items():
#     # if j==x:
#     #     print(i)
#     if j>x:
#         print(i)
# l=[1,[2,2,2],[3,3,3],[4,4],[5,5]]
# l1=[]
# def fun1(l):
#     for i in l:
#         if type(i)==list:
#             fun1(i)
#         else:
#             l1.append(i)
# fun1(l)
# print(l1)
# l = [1, 2, [3, 4, [5, 6]], 7, 8, [9, [10]]]
#
# # output list
# output = []
#
#
# # function used for removing nested
# # lists in python.
# def reemovNestings(l):
#     for i in l:
#         if type(i) == list:
#             reemovNestings(i)
#         else:
#             output.append(i)
#
#
# # Driver code
# print('The original list: ', l)
# reemovNestings(l)
# print('The list after removing nesting: ', output)
# s="python is a programming language"
# print(s)
# l=s.split()
# print(l)
# l1=[]
# for i in l:
#     l1.insert(0,i)
# print(l1)
# s1=" ".join(l1)
# print(s1)
# s1=""
# for i in s:
#     s1=i+s1
# print(s1)
# l=[1,2,3,4,5]
# l1=[]
# for i in l:
#     l1.insert(0,i)
#
# print(l1)

# matrix = []
# for i in range (5):
#     matrix.append([])
#     for j in range(5):
#         matrix[i].append(j)
# print(matrix)
#
# matrix = [[j for j in range(5) for i in range(5)]
# print(matrix
# from threading import*
# def display():
#     for i in range(1,11):
#         print("child thread")
# t=Thread(target=display)
# t.start()
# for i in range(1,11):
#     print("Main Thread")
# print(~5)



#
# def sum2(func):
#     def inner(l1,l2):
#         a=(l1+l2).append(100000)
#         print(a)
#         return func(l1,l2)
#     return inner
# @sum2
# def sum1(l1,l2):
#     print(l1+l2)
# print(sum1([1,2],[3,4]))

# def capital(f):
#     def inner(n):
#         print(n.upper())
#
#     return inner
#
# @capital
# def small(n):
#     print(n)
# small("asdfghjk")
# d={'a':1,'d':2,'c':3}
# d1=sorted(d.items(),key=lambda x:x[0])
# print(d1)
# print(dict(d1))
# for i,j in d1:
# #     print(i,j)
# import array as arr
# a = arr.array('B', ['a','b','c'])
# print(type(a))
# l1 = ['Murali',"Vamrsi",'Sai','mai']
# l2 =[]
# for i in range(1,len(l1)):
#     for j in l1[0]:
#         if j in l1[i] and j not in l2:
#             l2.append(j)
# for i in range(len(l1)):
#     for j in range(len(l2)-1):
#         if l2[j] not in l1[i]:
#             l2.remove(l2[j])
# print(l2)
# print("".join(l2))
# import copy
#
# # initializing list 1
# li1 = [1, 2, [3, 5], 4]
#
# # using copy for shallow copy
# li2 = copy.copy(li1)
# print(li1)
#
# # using deepcopy for deepcopy
# li3 = copy.deepcopy(li1)
# print(li2)
# import monk
# class A:
#     def func(self):
#         print("func() is being called")
# def monkey_f(self):
#     print("monkey_f() is being called")
#
# # replacing address of "func" with "monkey_f"
# monkey_f = monk.A.func
# obj = monk.A()
#
# # calling function "func" whose address got replaced
# # with function "monkey_f()"
# obj.func()
# l=[2,7,15,12]
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]+l[j]==9:
#             print([i,j])
# import django
# print(django.get_version())
# a=input(10)
# print(type(a))
# from sys import argv
# print(type(argv))
# l=[1,2,3,4,5]
# l1=list(map(lambda x:x**x,l))
# print(l1)
# num=int(input("enter a number:"))
# for i in range(2,num):
#     if num%i==0:
#         print(" it is not prime number")
#         break
# else:
#     print(" prime number")
# n=5
# for i in range(n):
#     for j in range(i+1):
#         print("* ",end="")
#     print()
# l=[1978,1947,77,67,79,87]
# l1=[]

# for i in l:
#     x=str(i).split("7")
#     l1.append(("".join(x)))
# print(l1)
# l2=[]
# for j in l1:
#     if j=='':
#         continue
#     else:
#         l2.append(int(j))
#
# print(l2)
# n=5
# for i in range(n):
#     for j in range(i+1):
#         print("* ",end="")
#     print()
# n=5
# for i in range(n):
#     for j in range(n):
#         print("*",end="")
#     print()
# for i in range(n):
#     for j in range(n-1-i):
#         print("*",end="")
#     print()
# n=10
# # s=0
# for i in range(2,n):
#     if n%i==0:
#         print("n.p")
#         break
# else:
#     print("prime")
       # s+=i
# if s==n:
#     print("perfect number")
# else:
#     print("not perfect number")
# def upper(func):
#     def inner(n):
#         print(n.upper())
#     return inner
# @upper
# def lower(n):
#     print(n)
# lower("sukanya")
# def fib():
#     a,b=0,1
#     while True:
#         yield a
#         a,b=b,a+b
# for i in fib():
#     if i>100:
#         break
#     print(i)
# n=int(input("enter a number:"))
# if n>1:
#     for i in range(2,n):
#         if n%i==0:
#             print("not prime number")
#             break
#     else:
#         print("prime number")
# n=2805
# s=0
# temp=n
# while temp>0:
#     r=temp%10
#     s=s*10+r
#     temp=temp//10
# print(s)
# l=[1,2,3,4,5,6]
# l1=[]
# for i in range(len(l)):
#       print(l1)
s={1,2,3,4,5,6,7,8,9,10}
t=10
for i in s:
    if t-i in s:
        print(t-i,i)
    # for j in s:
    #     if i+j==10:
    #         print(i,j)
