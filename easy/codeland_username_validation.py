import re

def CodelandUsernameValidation(strParam):
  if bool(re.search('(^[a-z,A-Z])+(\w+)+([a-z,A-Z,0-9]$)', strParam)) == True:
    length = len(strParam) >= 4 and len(strParam) <= 25
    return True if length else False
  return False


# keep this function call here 
print(CodelandUsernameValidation(input()))
