# NOTE: Throughout, if there is an error that you need to deal with
# like the input string was not valid URL, then your function should
# return None.
 
import requests 

def verification(url):

   urls = ["com", "net", "edu", "gov"]
   if url[-3:] in urls:
      return url
   return None  
 
def basic_request(url):

   out = verification(url)
   print (out) 
   if verification(url) == None:
      return None
   sc = requests.get(url)
   return sc.status_code    

def request_user_agent(url, user):

   if verification(url) == None:
      return None
   if not isinstance(user, str):
      return None
      
   resp = requests.get(url, headers={'user-agent': user}) 
   return resp.txt    

def request_post(url, data):

   if verification(url) == None:
      return None
   if data == None or data == {} or not isinstance(data, dict):
      return None      
         
   resp = requests.post(url + "/post", data=data)
   return resp.txt
                
    