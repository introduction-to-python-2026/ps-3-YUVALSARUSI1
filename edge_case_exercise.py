def move(my_list, direction = None):
   
    index_of_one = my_list.index(1)
    length = len(my_list)

    # Move the one to the left or to the right
    if direction == 'right':
      if index_of_one == length - 1 : 
        return my_list
      else:
        my_list[index_of_one] = 0
        my_list[index_of_one + 1] = 1
        return my_list
    elif direction == 'left':
      if index_of_one == 0 :
        return my_list
      else: 
        my_list [index_of_one] = 0
        my_list [index_of_one - 1] = 1
        return my_list

