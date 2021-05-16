def BracketMatcher(strParam):
  c = 0
  for char in strParam:
    if char == "(":
      c += 1
    elif char == ")":
      c -= 1
    if c < 0:
      return 0;
  return 1 if c == 0 else 0


# keep this function call here 
print(BracketMatcher(input()))
