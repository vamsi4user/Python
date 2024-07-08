#!/usr/bin/env python
# coding: utf-8

# In[14]:


print("Hello World!!")


# In[13]:


print("1. Top winning comes to Royal Flush in Poker")
print('2. Next comes Straight Flush')
print('3. Nextcomes "4" of a kind')
print("4. Next comes :'Full House' in the game")
print("5. Then Flush, followed by \"Straight\" and go on")


# Note: See quotations
# 
# 1,2- basic| 3,4- either wokrs| 5- alternative for 3,4

# In[37]:


print("Hello World!!\nHello World!!")


# \n - takes to next line

# In[32]:


print("1. Hello"+"Nancy")
print("2. Hello "+"Nancy")
print("3. Hello"+" Nancy")
print("4. Hello"+" "+"Nancy")


# String Concatenation(4- (+" "+))- involves joining two or more strings to create a single new string

# In[41]:


print("Hello "+ input("What is your name?\n"))


# Input- Input function allows user to enter data instead of simply just printing

# In[40]:


print('Enter your name:')
x = input()
print('Hello, ' + x)


# In[1]:


print(len(input()))


# len- it's input function calculates length of strings

# In[6]:


name = input("What is ur name?")
length = len(name)
print(length)


# Variables used here

# In[7]:


a = input()
b = input()
c = a
a = b
b = c
print("a:" + a)
print("b:" + b)


# In[16]:


print("Greetings from Card House")
name = input("What is ur name\n")
city = input("What city u live in\n")
print("Your id would be " + name + " " + city)


# Data types:
# 
# print("Hello" + "World") - String
# print("2yio" + "468")    - String
# print(123 + 368)         - Integer
# print(123_252 + 156_262) - Integer(Underscore is just for human understanding for larger numbers)
# 3.2782                   - float
# True, False              - Boolean
# 
# type                     - checks which function is it and shows in output
# 
# print(2 ** 3)            - 8(** - exponent)

# In[18]:


num_char = len(input("what is your name?"))
new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters.")


# In[22]:


two_digit_number=input()
first_digit= int(two_digit_number[0])
second_digit= int(two_digit_number[1])
two_digit_number= first_digit + second_digit
print(two_digit_number)


# Mathematical Operations:
# 
# PEMDASLR = 
# () 
# ** 
# * / 
# + - (order for operations, left to right)
# 

# In[24]:


print(3 * 3 + 3 / 3 - 3)


# In[30]:


height = input()
weight = input()
weight_as_int = int(weight)
height_as_float = float(height)
bmi = weight_as_int / height_as_float ** 2
bmi_as_int = int(bmi)
print(bmi_as_int)


# In[34]:


score = 0
height = 1.8
isWinning = True
print(f"your score is {score},\nyour height is {height},\nyou are winning is {isWinning}")


# F string- instead of mentioning all data types individually, by using f we can make it this way

# In[35]:


score = input("Enter your score: ")
height = input("Enter your height: ")
isWinning = input("Are you winning (True/False): ")

score_as_int = int(score)
height_as_float = float(height)
isWinning_as_bool = isWinning.lower() == 'true'

print(f"your score is {score_as_int},\nyour height is {height_as_float},\nyou are winning is {isWinning_as_bool}")


# In[2]:


age = input()
years = 90 - int(age)
weeks = years * 52
print(f"you have {weeks} weeks left")


# In[12]:


print("Welcome to tip calculator")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12 or 15?"))
people = int(input("How many people to split the bill?"))
bill_with_tip = tip / 100 * bill + bill
bill_per_person = bill_with_tip / people
##final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person)

print(f"Each person should pay: ${final_amount}")


# {:.2f} - rounds 4.98984 to 4.98
# format- is a function for that
# 

# In[ ]:


def node1 = 1
def node_adjacent= 
print("node_adjcent")


# define starting node,
# find its adjacent nodes
# print them
# 

# The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.
# 
# 
# sleep_in(False, False) → True
# sleep_in(True, False) → False
# sleep_in(False, True) → True

# In[1]:


def sleep_in(weekday, vacation):
  if not weekday or vacation:
    return True
  else:
    return False


# We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling. We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble.
# 
# 
# monkey_trouble(True, True) → True
# monkey_trouble(False, False) → True
# monkey_trouble(True, False) → False

# In[ ]:


def monkey_trouble(a_smile, b_smile):
  if a_smile and b_smile:
    return True
  if not a_smile and not b_smile:
    return True
  return False


# Given two int values, return their sum. Unless the two values are the same, then return double their sum.
# 
# 
# sum_double(1, 2) → 3
# sum_double(3, 2) → 5
# sum_double(2, 2) → 8

# In[ ]:


def sum_double(a, b):
  sum = a + b
  if a == b:
    sum = sum * 2
  return sum


# Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.
# 
# 
# diff21(19) → 2
# diff21(10) → 11
# diff21(21) → 0

# In[ ]:


def diff21(n):
  if n <= 21:
    return 21 - n
  else:
    return (n - 21) * 2


# We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23. We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble.
# 
# 
# parrot_trouble(True, 6) → True
# parrot_trouble(True, 7) → False
# parrot_trouble(False, 6) → False

# In[ ]:


def parrot_trouble(talking, hour):
  return (talking and (hour < 7 or hour > 20))


# Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.
# 
# 
# makes10(9, 10) → True
# makes10(9, 9) → False
# makes10(1, 9) → True

# In[ ]:


def makes10(a, b):
  return (a == 10 or b == 10 or a+b == 10)


# Given a string and a non-negative int n, return a larger string that is n copies of the original string.
# 
# 
# stringTimes("Hi", 2) → "HiHi"
# stringTimes("Hi", 3) → "HiHiHi"
# stringTimes("Hi", 1) → "Hi"

# In[ ]:


public String stringTimes(String str, int n) {
  String result = "";
  for (int i=0; i<n; i++) {
    result = result + str;
  }
  return result;
}


# Given an array of ints, return true if the sequence of numbers 1, 2, 3 appears in the array somewhere.
# 
# 
# array123([1, 1, 2, 3, 1]) → true
# array123([1, 1, 2, 4, 1]) → false
# array123([1, 1, 2, 1, 2, 3]) → true
# 

# In[ ]:


public boolean array123(int[] nums) {
  // Note: iterate < length-2, so can use i+1 and i+2 in the loop
  for (int i=0; i < (nums.length-2); i++) {
    if (nums[i]==1 && nums[i+1]==2 && nums[i+2]==3) return true;
  }
  return false;
}


# Given a string, we'll say that the front is the first 3 chars of the string. If the string length is less than 3, the front is whatever is there. Return a new string which is 3 copies of the front.
# 
# 
# front3('Java') → 'JavJavJav'
# front3('Chocolate') → 'ChoChoCho'
# front3('abc') → 'abcabcabc'

# In[ ]:


def front3(str):
  front_end = 3
  if len(str) < front_end:
    front_end = len(str)
  front = str[:front_end]
  return front + front + front 


# Given a string, return a new string where the first and last chars have been exchanged.
# 
# 
# front_back('code') → 'eodc'
# front_back('a') → 'a'
# front_back('ab') → 'ba'

# In[ ]:


def front_back(str):
  if len(str) <= 1:
    return str
  
  mid = str[1:len(str)-1]  # can be written as str[1:-1]
    return str[len(str)-1] + mid + str[0]

