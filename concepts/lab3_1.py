def sums():
   
  	
	first_sum = 2 + 2

	first_sum = first_sum * 10

	secret = first_sum + 2

	return secret


def string_manip(first_name):

   	name = first_name

   	all_caps = name.upper()

   	all_lowercase = name.lower()

   	first_five_letters = name[0:5]

   	last_two_letters = name[-2:]

   	return [all_caps, all_lowercase, first_five_letters, last_two_letters]

def greeter_bot():

   	fname = input('What is you name?')

	name = fname
	
	print('Hello, ' +  name) 
	
  

def temp_calculator():

   	# The formula is C = (F - 32) * (5/9)
 
   	inp = input('Enter a Celsius Temperature: ')

	cel = float(inp)

	fahr = (cel + 32) * 5 / 9

        print(fahr)

def equitable_bill_splitter():
   
   # TODO: Read the following code and add comments to each line explaining what
   # it does. To write a comment, begin the line with an octothorpe (hashtag, #)
   
   # this will give you a prompt to enter an interger that will store the number in variable people
   people = int(input("How many people are paying? "))
   # this will create a array that can store multiple values
   salaries = []
   # this assigns '0' to the variable 'total' to track the total 
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
