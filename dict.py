def add_items(some_dict):
  # Add new items to dict
  some_dict.update({'k': 3, 'l': 4})
  return some_dict
  
  
if __name__ == __main__:
  some_dict = {'a': 1, 'b': 2}
  new_dict = add_items()
  print(new_dict)
