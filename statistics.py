import math

def sum(values):
  sum = 0
  for i int values:
    sum = sum + i
  return sum


def mean(values):
  number_of_elem=len(values)
  sum = 0
  mean = 0
  for i int values:
    sum = sum + i
  mean = sum / number_of_elem
  return mean



def median(values):
  median=0
  number_of_elem = len(values)
  values_sorted = sorterd(values)
  if number_of_elem % 2 == 0:
    median = (values_sorted[number_of_elem/2]+values_sorted[(number_of_elem/2)+1])/2
    else:
        median = values_sorted[math.ceil(number_of_elem/2)]
  return median
