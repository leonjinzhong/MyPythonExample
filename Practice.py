
for i in range(3,6):
      print(i)


def my_function():
  print("Hello from a function")

my_function()


def my_function(food):
      for x in food:
       print(x)

fruits = ["apple","banana","cherry"]
my_function(fruits)


#message = input("Tell me something, and I will repeat it back to you: ")
#print(message)


class CustomList(object):
      def __init__(self, elements=0):
            self.my_custom_list = [0] * elements

      def __setitem__(self, index, value):
            self.my_custom_list[index] = value

      def __getitem__(self, index):
            return "Hey you are accessing {} element whose value is: {}".format(index, self.my_custom_list[index])

      def __str__(self):
            return str(self.my_custom_list)

obj = CustomList(12)
obj[0] = 1
print(obj[0])
print(obj)

print (id(obj[0]))

from abc import ABC, abstractmethod
 
class AbstractClassExample(ABC):
    
    @abstractmethod
    def do_something(self):
        print("Some implementation!")
        
class AnotherSubclass(AbstractClassExample):

    def do_something(self):
        super().do_something()
        print("The enrichment from AnotherSubclass")
        
x = AnotherSubclass()
x.do_something()

import logging
log = logging.getLogger(__name__)
log.info("Hello, world")

import logging

log = logging.getLogger(__name__)

def do_something():
    log.debug("Doing something!")

import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

logger.info('Start reading database')
# read database here
records = {'john': 55, 'tom': 66}
logger.debug('Records: %s', records)
logger.info('Updating records ...')
# update records here
logger.info('Finish updating records')


import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# create a file handler
handler = logging.FileHandler('hello.log')
handler.setLevel(logging.INFO)

# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# add the file handler to the logger
logger.addHandler(handler)

logger.info('Hello baby')


logbasefilename=None
if logbasefilename:
      print("ok")

class MethodTypes:

    name = "Ragnar"

    def instanceMethod(self):
        # Creates an instance atribute through keyword self
        self.lastname = "Lothbrock"
        print(self.name)
        print(self.lastname)

    @classmethod
    def classMethod(cls):
        # Access a class atribute through keyword cls
        cls.name = "Lagertha"
        print(cls.name)

    @staticmethod
    def staticMethod():
        print("This is a static method")

# Creates an instance of the class
m = MethodTypes()
# Calls instance method
m.instanceMethod()


MethodTypes.classMethod()
MethodTypes.staticMethod()



import logging
import sys
logger = logging.getLogger()
logger.setLevel(logging.INFO)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s - %(message)s")
handler.setFormatter(formatter)

logger.addHandler(handler)

logger.info("This is an info message")


name = "John"
age = 23
print("%s is %d years old." % (name, age))

data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."

print(format_string % data)

x = 10
#if x > 5:
    #raise Exception('x should not exceed 5. The value of x was: {}'.format(x))

def linux_interaction():
    assert ('linux' in sys.platform), "Function can only run on Linux systems."
    print('Doing something.')


'''
try:
    linux_interaction()
except:
    print('Linux function was not executed')
'''

try:
    linux_interaction()
except AssertionError as error:
      print(error)
      print('The linux_interaction() function was not executed')
      #raise error
print("ok next---")
try:
    linux_interaction()
except Exception as error:
      print(error)
      print('The linux_interaction() function was not executed')
      #raise error
print("ok")


'''
try:
      with open('file.log') as file:
            read_data = file.read()
except FileNotFoundError as fnf_error:
      print(fnf_error)
'''

'''
try:
    inp = input()
    print ('Press Ctrl+C or Interrupt the Kernel:')
except KeyboardInterrupt:
    print ('Caught KeyboardInterrupt')
else:
    print ('No exception occurred')
'''

'''
x = "hello"

#if condition returns True, then nothing happens:
assert x == "hello"

#if condition returns False, AssertionError is raised:
assert x == "goodbye","error ocurred"
'''

'''
x = "hello"

#if condition returns False, AssertionError is raised:
assert x == "goodbye", "x should be 'hello'"
'''

'''
import signal  
import time  
  
  
def handler(a, b):  # define the handler  
    print("Signal Number:", a, " Frame: ", b)  
  
signal.signal(signal.SIGINT, handler)  # assign the handler to the signal SIGINT  
  
while 1:  
    print("Press ctrl + c")  # wait for SIGINT  
    time.sleep(10) 

'''
'''
from jinja2 import Template

name = input("Enter your name: ")

tm = Template("Hello {{ name }}")
msg = tm.render(name=name)

print(msg)
'''

from jinja2 import Template
t = Template("Hello jinja2 template {{ something }}!")
print(t.render(something="World"))


t = Template("My favorite numbers: {% for n in range(1,10) %}{{n}} " "{% endfor %}")
print(t.render())

class Pizza(object):
      radius = 42
      @classmethod
      def get_radius(cls):
            return cls.radius
print(Pizza.get_radius())


# example of decorator
def sampleDecorator(func):
    def addingFunction():
        # some new statments or flow control
        print("This is the added text to the actual function.")
        # calling the function
        func()

    return addingFunction


@sampleDecorator
def actualFunction():
    print("This is the actual function.")


actualFunction()



def flowerDecorator(vasel):
    def newFlowerVase(n):
        print("We are decorating the flower vase.")
        print("You wanted to keep %d flowers in the vase." % n)

        vasel(n)

        print("Our decoration is done")

    return newFlowerVase


@flowerDecorator
def flowerVase(n):
    print("We have a flower vase.")


flowerVase(6)



# Python program to demonstrate  
# use of class method and static method. 
from datetime import date 
  
class Person: 
    def __init__(self, name, age): 
        self.name = name 
        self.age = age 
      
    # a class method to create a  
    # Person object by birth year. 
    @classmethod
    def fromBirthYear(cls, name, year): 
        return cls(name, date.today().year - year) 
      
    # a static method to check if a 
    # Person is adult or not. 
    @staticmethod
    def isAdult(age): 
        return age > 18
  
person1 = Person('mayank', 21) 
person2 = Person.fromBirthYear('mayank', 1996) 
  
print (person1.age) 
print (person2.age) 
  
# print the result 
print (Person.isAdult(22)) 

string='20200110155548_20200110155548_20200110155548_10724_cic_svoctestbdpeventhub02_ciclogs_3_2019_12_11_00_17_37.avro'
print(string.split("_",5)[5].split(".")[0])
print(string.split("_"))


#import this

'''
import psycopg2
import sys

con = None

try:

    con = psycopg2.connect(host='ed10-loannr', dbname='datafactory_metastore', user='svc-bdp-hdi3',  password = 'd@f!3svcdev')

    cur = con.cursor()
    cur.execute('SELECT version()')

    version = cur.fetchone()[0]
    print(version)

except psycopg2.DatabaseError as e:

    print(e)
    sys.exit(1)

finally:

    if con:
        con.close()
'''

from datetime import datetime

now = datetime.now() # current date and time

year = now.strftime("%Y")
print("year:", year)

month = now.strftime("%m")
print("month:", month)

day = now.strftime("%d")
print("day:", day)

time = now.strftime("%H:%M:%S")
print("time:", time)

date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
print("date and time:",date_time)
