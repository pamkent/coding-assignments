def divisible_by_7(num):
   if num %7 == 0:
      return num /7
   else:
      print("not divisble by 7")
      return None 

def compare_it(x, y):
   if type(x) is not int and type(y) is not int:
      return False
   if x != y:
      return False 
   if x <= 0 and y <= 0:
      return False
   else:
      return True

# Had a lot of trouble and couldn't figure this one out
def keyword_counter(a, b, c):
   fhand = open('test6_1.txt')
   counts = dict()
   names = ['apple', 'banana', 'grapefruit']
   for names in fhand:
      counts[name] = counts.get(name, 0) + 1 
   print(counts)   
with open(file_name, "r") as f:
   text = f.read().replace("\n", " ")


