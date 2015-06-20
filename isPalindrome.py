import string
def is_palindrome(s):
    
    if len(s)==0:
        return True
    
    FormattedString = (s.lower().replace(" ",""))
    listFromString = list(FormattedString.translate(string.maketrans("",""),string.punctuation))   
    
    length = len(listFromString)
    for i in range(0,len(listFromString)/2+1):
          if(listFromString[i]==listFromString[length-i-1]):
              return True
          else:
              return False

print is_palindrome("If I had a hi-fi...")