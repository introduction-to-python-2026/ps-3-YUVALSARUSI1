def move(my_list, direction):
  one = my_list.index(1)
  lengh = len(my_list)
  if direction == "right":
    if one == lengh - 1:
      return my_list
    else:
      my_list[one]=0
      my_list[one+1]=1
      return my_list
  elif direction == "left":
    if one ==0:
      return my_list
    else:
      my_list[one]=0
      my_list[one-1]=1
      return my_list

