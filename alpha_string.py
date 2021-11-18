
def alpha_string(strParam):
  """
  Return an array of characters in a string in alphabetical order.
  :param strParam: a string
  :return str_array: alphabetized array of characters from strParam
  """
  sorted_str = sorted(strParam)
  str_array = "".join(sorted_str)
  
  return str_array
