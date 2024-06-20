'''
Write a function is_long_pressed() that takes in a string name and a string typed as parameters. Imagine your friend is typing their name into a keyboard and when typing a character, the key might get long pressed and the character will be typed 1 or more times.

The function should examine the typed characters and return True if it is possible that it was your friends name with some characters being long pressed and False otherwise.

Use the two-pointer approach to solve the problem, which is a common technique in which we initialize two variables (also called a pointer in this context) to track different indices or places in a list or string, then moves the pointers to point at new indices based on certain conditions. A common variation of this technique is to point one variable at the beginning of one string and a second pointer at the beginning of a second string, then increment each pointer conditionally to solve a problem.
'''
def is_long_pressed(name, typed):
  i, j = 0, 0

  # basically checking if words are the same with the added caveat that
  # typed is allowed to have duplicates
  while i < len(name) and j < len(typed):
    if name[i] == typed[j]:
      i += 1
      j += 1
    elif j > 0 and typed[j] == typed[j-1]:
      j += 1
    else:
      return False

  # If there are still characters left in name, it means not all characters were matched
  if i < len(name):
      return False

  # Check remaining characters in typed to ensure they are all the same as the last 
  # character in name
  while j < len(typed):
      if typed[j] != name[-1]:
          return False
      j += 1

  return True

'''
Problem 2: Sharing Cookies
Imagine you're an awesome babysitter and want to give the kids you're 
looking after some cookies as a snack.
Each child i has a greed factor g[i], which is the minimum size of a cookie 
that the child will be content with.
Each cookie j has a cookie size s[j].
If s[j] >= g[i], we can assign the cookie j to the child i, and the child will be content.
If s[j] < g[i], the child will not be content.

Write a function find_content_children() that takes in the greed list g and the cookie 
size list s as parameters and maximizes the number of content children you are 
babysitting! The function returns
'''
def find_content_children(cookie_sizes, greed_sizes):
  satisfied_children = 0
  cookie_ptr = 0
  greed_ptr = 0

  while cookie_ptr < len(cookie_sizes) and greed_ptr < len(greed_sizes):
    if greed_sizes[greed_ptr] > cookie_sizes[cookie_ptr]:
      cookie_ptr += 1
    else:
      satisfied_children += 1
      cookie_ptr += 1
      greed_ptr += 1
  return satisfied_children

# # Example 1:

# g = [1,2,3]
# s = [1,1,3]
# # There are 3 children and 3 cookies
# # child `0` has a greed factor of 1
# # cookie `0` has a size of 1 --> content child

# # child `1` has a greed factor of 2
# # cookie `1` has a size of 1, this child will not be content

# # child `2` has a greed factor of 3
# # cookie `2` has a size of 3 --> content child

# print(find_content_children(s, g))
# # Output: 2 
# # Example 2:

# g1 = [1,1]
# s1 = [2,2,2]
# # There are 2 children and 3 cookies
# # child `0` has a greed factor of 1
# # cookie `0` has a size of 2 --> content child

# # child `1` has a greed factor of 1
# # cookie `1` has a size of 1 --> content child

# print(find_content_children(s1, g1))
# Output: 2 