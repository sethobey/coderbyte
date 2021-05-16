import re

def LongestWord(sen):
  length = 0
  longest = ""
  words = sen.split(" ")
  for word in words:
    parsed = re.search('([a-zA-Z0-9])+', word)
    if len(parsed.group()) > length:
      length = len(parsed.group())
      longest = parsed.group()
  return longest

# keep this function call here 
print(LongestWord(input()))
