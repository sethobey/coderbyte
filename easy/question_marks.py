def QuestionsMarks(strParam):
  sums = cases = 0
  for i, a in enumerate(strParam):
    if a.isdigit():
      count = 3
      for j, c in enumerate(strParam[i + 1:]):
        if c == "?":
          count -= 1
        elif c.isdigit():
          if int(c) + int(a) == 10:
            sums += 1
            if count == 0:
              cases += 1
          break
  return True if sums != 0 and cases == sums else False



  # code goes here
  return strParam

# keep this function call here 
print(QuestionsMarks(input()))
