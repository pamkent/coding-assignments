def divisible_by_7(num):
   if num %7 == 0:
      return num /7
   else:
      print("not divisble by 7")
      return None 

def compare_it(x, y):
   if not isinstance(x, int) and not isinstance(y, int):
      return False
   if x != y:
      return False 
   if x < 0 and y < 0:
      return False
   else:
      return True

def keyword_counter(word_list, logic, test): 
   data = test
   if not logic:
      with open(test, "r") as f:
         text = f.read().replace("\n", " ")
results = {}
for word in word_list:
   results[word] = text.count(word)
return results

