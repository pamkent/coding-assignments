# NOTE: Throughout, if there is an error that you need to deal with
# like the input string was not valid URL, then your function should
# return None.
 
import requests 

def verification(domain):

   domains = re.findall("com$, net$, edu$, gov$", str)
   for domain in domains:
      return domain 
   else: 
      return None  
 
def basic_request(url):

   sc = ""
   out = verification(url)
   print (out) 
   if out == "none":
      return None
   else:
      sc = requests.get(url)
      return sc     

def request_user_agent(url, user):

   results = domain(url)
   if results:
      if isinstance(user, str):
         return results 
      else:
         return None

def request_post(url, dictionary):

   results = domain(url)
   if results:
      if isinstance(dictionary, dict) or dictionary != {}:
         results = requests.post(url)
         return results 
   else:
      return None                  
    