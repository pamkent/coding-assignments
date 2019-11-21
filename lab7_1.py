# NOTE: Throughout, if there is an error that you need to deal with
# like the input string was not valid URL, then your function should
# return None.
 
import requests 

def verification(url):

   ulrs = re.findall("com$, net$, edu$, gov$", str)
   if url in urls:
      return url
   else: 
      return None  
 
def basic_request(url):

   out = verification(url)
   print (out) 
   if out == "none":
      return None
   else:
      sc = requests.get(url)
      return sc     

def request_user_agent(url, user):

   results = verification(url)
   if results.get(url):
      if isinstance(user, str):
         return results.get(url, headers={'user-agent': user_agent}) 
   else:
      return None 

def request_post(url, dictionary):

   results = verification(url)
   if results:
      if isinstance(dictionary, dict) or dictionary != {}:
         results = requests.post(url)
         return results 
   else:
      return None                  
    