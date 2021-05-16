def FindIntersection(strArr):
  intersect = [x for x in strArr[0].split(', ') if x in strArr[1].split(', ')]
  return ",".join(intersect) if len(intersect) > 0 else "false"

# keep this function call here 
print(FindIntersection(input()))
