def BracketCombinations(n):
  return int(factorial(2 * n) / (factorial(n + 1) * factorial(n)))


def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)


# keep this function call here 
print(BracketCombinations(input()))
