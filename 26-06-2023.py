#!/usr/bin/env python
# coding: utf-8

# # Difference between print("") & without print
# print(" ") will print the result without any colon where as " " will print value with colon -See line 1 & 2
# printing result without print statement will not give any output if used before print statement -see line 4 
# printing result without print sttement will work if used at the end or after print - see line 3

# In[1]:


print("Shree Ganeshya Namaha")


# In[2]:


"Jai Shree Ram"


# In[3]:


print("Jai Shree Shiv Maa Parvati")
"Jai Shree Hanuman ji"


# In[4]:


"Jai Shree Hanuman ji"
print("Jai Shree Shiv Maa Parvati")


# # Multiline output 
# we use """ """ to print output in multiplt line

# In[5]:


print ("""Good Morning 
Everyone, Hope you are going great
and enjoying session""")


# # How to Comments
# to comment we use # before line or start on line

# In[6]:


print("Ram is good") #using print to get the output


# In[7]:


#This is starting of multiline 
#code another way 
#of commenting in python


# In[8]:


print('I am "Umesh"')


# In[9]:


print("""I am "Umesh" """)


# # Variables in Python
# Variables are anything which stores values like a=10 here a is variable which stores the value 10

# # Condition to create varaible
# 1-Should not start from numerical value like 1,100 etc
# 2-should start with alphabates only 
# 3-not containe speical characters like @,#,^,&,*,$,% or any other character which has funtoinal value or assignement value in python
# 4-Can use Capital letter to assign the variable 

# In[1]:


# rule 1  Should not start from numerical value like 1,100 etc else will give syntaxError :cannot assign to literal
a= 100


# In[2]:


100='a'


# In[3]:


ten_10 =10


# In[4]:


print(ten_10)


# In[5]:


TEN =10


# In[6]:


TEN


# In[7]:


## Python is case sensitive so make sure you give proper name to your variables
TEN =10
ten =11
# these are two different variable to give name accordingly and its suggested to use small letters insted of capital letters


# In[8]:


# we can assign variable using _ but this is called hidden variable which will be used in programming but will not be accessible to user other than developer
_num =14


# In[9]:


print(_num)


# # 30-06-2023

# In[10]:


# Types of printing variable with Print statement 
#with + + sign

name ="RAM SINGH"
print("My name is "+name +".")


# In[11]:


# f string or formatted string
#we use f in start of statment and {}
print(f"My name is {name}.")


# In[12]:


# using .format() funtion
print("My name is{}".format(name))


# In[13]:


# using multiple f string format
age =10
print(f"My name is {name} and i am {age} years old")


# In[14]:


print ='Umesh'
print


# In[15]:


print("Ram")


# In[16]:


# we are getting the errror in above line because we have assigned the variable where print is having value as "Umesh"
# to use print again as funtion we have to use the del funtion which will delete the variable and make it funtion again
# make sure not to use Reserverd words as variable  link "https://docs.python.org/2.5/ref/keywords.html"
# lets make it again as funtion
del print


# In[17]:


print(2/2)


# In[18]:


# how to assign value to multiple variables 
a,b,c =10,20,30


# In[19]:


print(a,b,c)


# In[20]:


a=b=c =10


# In[21]:


print(a,b,c)


# In[22]:


# input funtion 
# this funtion takes value as string only and can be manipulted using type conversion keywork 


# In[35]:


# how to ask user to give input and print that output 
name =input('Enter your name: ')

if name =="umesh":
    print(name)
else:
    print("entry correct value")


# In[36]:


name =input('Enter your name')
print(type(name))


# In[37]:


#Memory assisgnment


# In[38]:


# whenever we assign value t0 variable python store it to a location that is called memory allocation
#it will assign the same memory to same value variable like if a =10 nd b =10 then the ID or memory block will be same for both variable


# In[39]:


a= 10
b=10
c=20


# In[40]:


# to check memory location we use ID funtion
print (id(a),id(b),id(c))


# In[41]:


#string take more memory compare to int
a=10
b='Ram'


# In[42]:


print(id(a),id(b))


# In[43]:


# note that memory is assigned to valur of variable not to variable, memoey address will change the if value of variable changed


# In[44]:


a=10
b='Ram'
print(id(a),id(b))


# In[45]:


a='Ram'
b=10
print(id(a),id(b))


# In[46]:


# memoery will stay on address as long as value is there value need to be deleted
del a 
del b


# In[47]:


a


# In[48]:


a='Ram'
b=10
print(id(a),id(b))


# In[49]:


#how to create email using input method 
lastname =input("Enter your last name")
firstname =input("Enter your first name")
mail ="@gmail.com"
print(f"{lastname}.{firstname}{mail}")


# In[51]:


#how to create email using input method 
lastname =input("Enter your last name")
firstname =input("Enter your first name")
print(f"{lastname}.{firstname}"+"@gmail.com")


# In[53]:


raining =True
if raining ==True:
    print("Lets stay and work from home")
else:
    print("Go to office")


# In[54]:


# Logical Operators
# not 
# and
#or


# In[55]:


start=True
print(start)


# In[56]:


start=True
print( not start)


# In[65]:


# an example of logical operators
class_started =False

if class_started:
    print("lets concentrate on class")
else:
    print("Class has not started")


# In[66]:


class_started =True

if not class_started:
    print("lets concentrate on class")
else:
    print("Class has not started")


# In[70]:


# example of AND condition
a=int(input("enter number here for a "))
b=int(input("enter number here for b "))
if a==10 and b==15:
    print("value for a & b matched")
elif a==10:
    print("its a=10") 
else:
    print("its other value for a")


# In[71]:


# example of AND condition
a=int(input("enter number here for a "))
b=int(input("enter number here for b "))
if a==10 and b==15:
    print("value for a & b matched")
elif a==10:
    print("its a=10") 
else:
    print("its other value for a")


# In[73]:


# example of AND condition
a=int(input("enter number here for a "))
b=int(input("enter number here for b "))
if a==10 and b==15:
    print("value for a & b matched")
elif a==10:
    print("its a=10") 
else:
    print("its other value for a & b")


# In[77]:


# use bool operator in printstatement to show clear result 
marks =80
required =36

if marks >=required:
    print(f"total marks got : {marks}")
    print(f"marks required : {required}")
    print(f"You have got : {marks} marks and required marks were: {required} and you are Pass")
else:
    print("Fail")


# In[78]:


# Equality Operators
A =1
B=1
A==B


# In[79]:


A =1
B=1
A is B


# In[81]:


print(id(A),id(B))


# In[82]:


a=['Ram','Shyam']
b=['Ram','Shyam']


# In[87]:


a is b 


# In[85]:


# why we are getting different result where as we have same value in list
# lets check 
print(id(a),id(b))
# thes both having different memory location because as per python list value can be changed anytime so it have assigned different memeory locatin wich is making them different even having same value


# In[88]:


# in Python there is difference in is and is not vs == and != 
#1-is and is not check the memory location of variable value and give result 
# but == and != check the value or variable not the memory location and used mostly lets see in example
a=['Ram','Shyam']
b=['Ram','Shyam']
a is b # this will check if both variable value stored as same location or not if location is same it will give True else False


# In[50]:


a=['Ram','Shyam']
b=['Ram','Shyam']
a==b # this will check the value of variable not the memoery and will give True as values are same


# # Check membership in a list
# ## What is list

# In[2]:


# we use in funtion to check if any value is present in list or not 
a=['Ram','Shyam']
"shyam" in a # note this is case sensitive and we got false as Shyam is there but not shyam


# In[3]:


# we can use this with if else to create new or append the list

if "Umesh" in a:
    print("Yes")
else:
    print("No Umesh is not present, adding him to list")
    a= a+"Umesh"  # we will get the error is we run this because a is list and str can't be concatenated, we have make it list 
    print(a)


# In[6]:


a=['Ram','Shyam']


# In[7]:


if "Umesh" in a:
    print("Yes")
else:
    print("No Umesh is not present, adding him to list")
    a= a+["Umesh"]
    print(a)


# In[9]:


n =int(input("Enter your item"))
i =0

while i <n:
    print("Add item you have not added full items")
    i=i+1
print("YOu have completed your shopping")


# In[15]:


# take user input to add item to shopping list
n =int(input("Enter your item "))
i =0

while i <n:
    list =input("Added item ")
    i=i+1
    print(f" Add {i}th item you have not added full items")
    list
print("YOu have completed your shopping")


# In[32]:


# take user input to add item to shopping list lets use append

items =[]

number =int(input("No of item you want to buy"))
for i in range(n):
    item_list =input("Select Item to add")
    print("added item is:",item_list)
    items.append(item_list)
print(items)


# In[25]:


# show max length string from list

name =["Ram","Shyam","Mohan","Radhyashyam"]
max_count =0
result =""
for max_len in name:
    print(max_len,len(max_len))
    if len(max_len) > max_count:
        max_count = len(max_len)
        result =max_len
print("final result is:",result,len(max_len))


# In[33]:


item =['pen', 'pencil', 'book']


# In[35]:


item.pop(0)
item


# In[49]:


# how to check if a number is ood or even in a list 

num =[1,10,15,20,25,30]
for i in range(len(num)):
    idx =num[i]
    print(f"The index is {i} and the value is {idx}")
    if idx%2 !=0:
        print(f"{idx} is odd number")    
    else:
        print(f"{idx} is even number")


# In[ ]:




