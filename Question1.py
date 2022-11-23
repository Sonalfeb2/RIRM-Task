str = input()
import re
pattern=r"^\s*(?:\+?(\d{1,3}))?[-. (]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})(?: *x(\d+))?\s*$"  
match = re.match(pattern,str) 
if match: 
      print("Valid")
else:
      print("Invalid")