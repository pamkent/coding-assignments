def is_even():
   # Notice, this will give us an error if we don't enter an integer
   # in Everyday Coding, we'll learn how to catch errors like this.
   user_data = int(input("Please give me an integer. "))
   out = None
   
   if user_data%2 == 0:
      print("This is even")
   else:
      print("This is odd")
    
   # This is for the test.
   return out 

def multi_condition():
   # Notice, this will give us an error if we don't enter an integer
   # in Everyday Coding, we'll learn how to catch errors like this.
   user_data = int(input("Please give me an integer. "))

   	if user_data == 0:
	   print("Don't be such a zero!")
	elif user_data%3 == 0:
	   print("Positively odd!")
	elif user_data%2 == 0:
	   print("Even Steven!")
	elif user_data < 0:
	   print("Negative Nelly!")
   
   return None


def is_underage():
   
   user_age = int(input("How old are you?")
   
	if user_age >= 21:
	   print("You may drink, smoke, and drive if you wish!")
	elif user_age >= 18 and user_age < 21:
	   print("You may smoke and drive!")
	elif user_age >= 16 and user_age < 18:
	   print("You may drive!")
	else:
	   print("Enjoy you bike, kid!")
  
   
   # So the tests fail and they don't throw errors
   return None

def countdown():
   
	countdown = 11
	for iterver in [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]:
	   countdown = countdown -1 
	   print(countdown)
	   

   # So the tests fail and they don't throw errors
   return None

def guessing_game(num):
  
    	user_input = int(input("Guess a number between 1 and 20"))
        for i in range(10):
	   if user_input ==  num:
	      print("You win!")
	      win = True
	   elif user_input > num:
	      print("Too high!")
           elif user_input < num: 
	      print("Too low!")
	   else:
	      print("You lose!")   
	      win = False
	input("Press 'q' to quit")
	mode = input ()
	   if mode == 'q':
	      print("Goodbye, quitter!")
   


   # So the tests fail and they don't throw errors
   return None
