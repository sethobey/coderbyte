def FirstReverse(strParam):
  string = ""
  for index in range(len(strParam) - 1, -1, -1):
    string += strParam[index]
  return string

# keep this function call here 
print(FirstReverse(input()))
