#Question 1: Define a function ‘fib’ that takes a number, ‘n’, as a parameter and prints all the Fibonacci numbers 
#less than ‘n’ to the screen.

## Generally good comments but make sure to use doc strings for your function headed (define
## purpose of the functions and parameters) so the help function will work with your function.

## Why did you print the logical result of a<n?
def fib(n):
    a, b = 0, 1
    if n== 0: return 0 #the first number should be zero
    if n== 1: return 1 #second number should be 1
    while a < n: #run until n is larger than a
        print(a, a<n) #print must go first (before the below) so we print the zero
        a, b = b, a+b # for loop, a=b and b=a+b, then a=0, b=1 is a,b=1+(1+0)=2... and so on for the loop
         
    #all values less than a will show "true", else "false" 
   
fib(30)


#Question 2: Define a function mymax() that takes two numbers as arguments and returns the largest of them. 
#Use the if-then-else construct available in Python. 
#(It is true that Python has the max() function built in, but writing it yourself is nevertheless a good exercise.)

def mymax(a,b):
    if a>b: return a #if a is larger than b, we return a (since then, a is max)
    else: return b #if b is larger than a, we return b (since then, b would be max)

mymax(5,9) #no matter what we define a and b as, this will return the largest number of a and b.


#Question 3: Define a function max_of_three() that takes three numbers as arguments and returns the largest of them.

#use question 2 info from above (mymax function) and build new function:

## Nice solution!
def max_of_three(a,b,c):
    return mymax( a, mymax( b, c ) ) #first mymax(b,c) will see which is larger, then mymax(a,mymax(b,c)) will see
                                     #what is larger between a and whatever was the max for mymax(b,c) and return
                                     #the largest number
max_of_three(4,6,80)


#Question 3, another way to do it (for own practice):
# def max_of_three(a,b,c):
#     if a > b: #rule one
#         if a > c: #this is within first if function
#             return a
#         else:
#             return c
#     else: #new rule
#         if b > c:
#             return b
#         else:
#             return c
# #Set a, b and c to whatever numbers you'd like
# a=60
# b=23
# c=54
# max_of_three(a,b,c)


#Question 4: Define a function mylen() that computes the length of a given list or string. 
#(It is true that Python has the len() function built in, but writing it yourself is nevertheless a good exercise.)

## The function should return count instead of printing count
def mylen(n):
    count = 0 #set count to zero
    for i in n: #for each letter/string (i) in n
        count=count+1   #this will count how many strings (i) are in n
    print (count)

mylen("apple")


#Question 5: Write a function that takes a character (i.e. a string of length 1) and returns True if it is a vowel,
#False otherwise.

## This function returns a string, instead it should return a logical value
def vowel(char):

 if (char == "a" or char == "A" or char == "e" or char == "E" or char == "i" or char == "I" or char == "o" or 
     char == "O" or char == "u" or char == "U"): #defining the vowles
     return ("True") #it is true if the character equals one of the defined characters above (i.e.a vowel)
 else:
     return ("False") #returns false since there is no vowel found
#vowels("O")#change this as needed to whatever letter desired.



#Question 6: Write a function translate() that will translate a text into "rövarspråket" (Swedish for "robber's 
#language"). That is, double every consonant and place an occurrence of "o" in between. For example, translate
#("this is fun") should return the string "tothohisos isos fofunon".

## Function name was not corret - how did this run properly? Also, logic does not meet specifications.
def translate(char):
 trans = ""
 for i in char:
    if vowel(i)=="True": #using function vowels() from question 5 to find vowels for each character
         trans = trans+2*str(i) 
    elif vowel(i) == "False": #for consontants, we double them and place an 'o' between the vowel.
         trans = trans+str(i)+"o"+str(i)

    return (trans)

translate("this is fun")


#Question 7, part 1 (add): Define a function sum() and a function multiply() that sums and multiplies (respectively) all the
#numbers in a list of numbers. For example, sum([1, 2, 3, 4]) should return 10, and multiply([1, 2, 3, 4])
#should return 24.

#for adding
def sum(n):
    a=0  #start at zero for addition
    for i in n: #for each value in "n" 
        a+=i    #we add them together
    return (a)

sum([1,2,3,4]) #put the desired numbers you would like to add here

#Question 7: part 2 (multiply):

#for multiplying
def multiply(n):
    b=1 #start at 1 for multiplication 
    for i in n:
        b*=i #multiply here
    return (b)

multiply([1, 2, 3, 4])#put the desired numbers you would like to multiply here




#Question 8: Define a function reverse() that computes the reversal of a string. For example, 
#reverse("I am testing") should return the string "gnitset ma I".

def reverse(n):
    a=''
    b=len(n) #use len() to count number of characters in n

    for i in range(0,b): #start range at zero and go to b (which is all the characters in n)
     a= a+n[-i-1] #this will reverse n...each letter of n will be backwards here

    return (str(a))

reverse("I am testing")


#Question 9: Define a function is_palindrome() that recognizes palindromes (i.e. words that look the same written 
#backwards). For example, is_palindrome("radar") should return True.
#build off function from question 8:

def is_palindrome(n):
    a='' 
    b= len(n) #use len() to count number of characters in n
    for i in range(0,b):
     a= a+n[-i-1] #as above for len(), this will reverse characters in n
    print (str(a))
    
    if n == a:  return ("True") #if the word is the same written backwards and reversed, output will be true
    else: return ("False")

is_palindrome("radar") #change the word here to run function


#Question 10: Write a function is_member() that takes a value (i.e. a number, string, etc) x and a list of values a,
#and returns True if x is a member of a, False otherwise. (Note that this is exactly what the in operator does, 
#but for the sake of the exercise you should pretend Python did not have this operator.)

def is_member(x,values): 
    for i in values: #i represents each item in the list of values 
        if (i== x): 
             return (True) #if one of the items on the list of values is equal to x, it will return true
    return (False) #if not, it will return false
values=['apple','a','carmen'] #change this list of values as desired.
is_member('a',values) #change 'a' here to see if it is a member of the list


#Question 11: Define a function overlapping() that takes two lists and returns True if they have at least one member 
#in common, False otherwise. You may use your Homework is_member() function, or the in operator, but for the sake 
#of the exercise, you should (also) write it using two nested for-loops.

def overlapping(a,b):
    for x in a: #for all items in list a
        for y in b: #for all items in list b
            if x==y: #if one of the items in list a is the same as list b (e.g. "apple" is in list a and b)
                return (True) #then it will return true 
    else: return (False) #it will return false if no items in list a and b are the same

overlapping(['apple','a','carmen'],["123","cat","a"])   

#Question 12: Define a function generate_n_chars() that takes an integer n and a character c and returns a string,
#n characters long, consisting only of c:s. For example, generate_n_chars(5,"x") should return the string "xxxxx". 
#(Python is unusual in that you can actually write an expression 5 * "x" that will evaluate to "xxxxx". For the 
#sake of the exercise you should ignore that the problem can be solved in this manner.)

def generate_n_chars(n,char):
    x=''
    for i in range(n): #for the number in n
        x=x+char #x will be returned n number of times
    return x
generate_n_chars(5,'s')


##TEST CASES
print('#1\n')
fib(500)
print('\n')

print('#2\n')
print(mymax(45,987), '\n')

print('#3\n')
print(max_of_three(3,4,5),'\n')

print('#4\n')
print(mylen('Gerhard'))
print(mylen([1,2,3,4,5,6,7]))
print('\n')

print('#5\n')
print(vowel('e'))
print(vowel('H'))
print('\n')

print('#6\n')
print(translate("this is fun"))
print(translate('aeiou'))
print(translate('YYYYYYY'))
print(translate("mmmmmm"))
print('\n')

print('#7\n')
print(sum([1,2,3,4,5]))
print('\n')

print('#8\n')
print(multiply([0,1,2,3]))
print(multiply([1,2,3,4]))
print('\n')

print('#9\n')
print(reverse("gnitset ma I"))
print('\n')

print('#10\n')
print(is_palindrome('radar'))
print(is_palindrome('Gerhard'))
print('\n')

print('#11\n')
print(is_member('dog', ['cat', 'dog', 'zebra']))
print(is_member(3, [1,2,3,4]))
print(is_member(3, [5,6,7]))
print('\n')

print('#12\n')
print(overlapping([1,2,3], [3,4,5]))
print(overlapping([1,2,3], [6,4,5]))
print('\n')

print('#13\n')
print(generate_n_chars(7, 'g'))