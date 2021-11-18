
def calculator(strParam):
  """
  Evaluate the mathematical expression within the string.
  :param strParam: string that contains mathematical expression
  :return result: resulting integer of math expression
  """
  res1 = eval(strParam)
  result = int(res1)
  
  return result
