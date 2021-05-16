def MinWindowSubstring(strArr):
  table = {}
  minLength = len(strArr[0])
  left = 0
  right = minLength - 1
  found = False

  for char in strArr[1]:
    if char in table:
      table[char] += 1
    else:
      table[char] = 1
  
  i = j = 0
  count = len(table)

  while j < len(strArr[0]):
    endChar = strArr[0][j]
    j += 1
    if endChar in table:
      table[endChar] -= 1
      if table[endChar] == 0:
        count -= 1
    
    if count > 0:
      continue
    
    while count == 0:
      startChar = strArr[0][i]
      i += 1
      if startChar in table:
        table[startChar] += 1
        if table[startChar] > 0:
          count += 1
    
    if j - i < minLength:
      left = i
      right = j
      minLength = j - i
      found = True
    
  return strArr[0][left - 1:right] if found else ""


# keep this function call here 
print(MinWindowSubstring(input()))
