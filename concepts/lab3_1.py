def sums():
   
  	 #TODO: Initialize a variable called first_sum and store the sum of 
   	# 2 and 2

   	#TODO: Store to first_sum the value of first_sum times 10

  	 #TODO: Initialize a variable called secret and assign it the value 
   	# of first_sum plus 2

   	return secret

def string_manip(first_name):

   	# TODO: Initialize a variable called name and assign it the 
   	# parameter.

   	# TODO: Use builtin string functions and slices to replace None with 
   	# the appropriate manipulation of your name. I've done the first one.
   	all_caps = name.upper()
   	all_lowercase = None
   	first_five_letters = None
   	last_two_letters = None

   	return [all_caps, all_lowercase, first_five_letters, last_two_letters]

def greeter_bot():

   	# TODO: Use the input() function to prompt the user for their name.
   	# Then assign the value to a variable called name and print a greeting.
   	# I have started it for you, but you need to modify the input and 
   	# print functions.
   	# Hint: to get the test to pass, the greeting should be "Hello, input name"
   	fname = input()
   	print()

def temp_calculator():

   	# TODO: Write code that prompts the user for a temperature in degrees
   	# celsius and prints the equivalent temperature in degrees fahrenheit.
   	# The formula is C = (F - 32) * (5/9). 
   	print()

def equitable_bill_splitter():
   
   # TODO: Read the following code and add comments to each line explaining what
   # it does. To write a comment, begin the line with an octothorpe (hashtag, #)
   
   # this will give you a prompt to enter an interger that will equal the number of people
   people = int(input("How many people are paying? "))
   # this will create a array that can store multiple values
   salaries = []
   # this assigns '0' to the variable 'total' 
   total = 0
   # the for loop will execute a set of statements once for each item in a list, adding in range will make 
   # it so that it loops through a specific number of times (people)
   for i in range(people):
      # this will give a prompt for a specific person, .format will format the values and return the formatted string
      sal = int(input("What is the salary of person {}?".format(i+1)))
      # this will add sal to total and assign the result to the total      
      total += sal
      # this will add sal the the existing salaries list
      salaries.append(sal)
  # this gives a prompt to enter the amount for the bill total
  total_bill = int(input("How much is the bill? "))
   # this loop will iterate over a sequence in a list, in range will make it run through the length of the salaries
   #list and iterate over it 
   for j in range(len(salaries)):
       # this will print out the name of the person and how much they owe based off of the arithmetic sequence
       print("Person {} should pay ${}\n".format(j + 1, round((total_bill * (salaries[j]/total)), 2)))
