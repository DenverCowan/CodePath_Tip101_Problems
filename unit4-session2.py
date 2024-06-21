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
    elif j > 0 and typed[j] == typed[j - 1]:
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
'''Problem 3: Valid Palindrome
Write a function valid_palindrome() that takes in a string s as a parameter and returns True if s can be a palindrome after deleting at most one character from it and False otherwise.
'''


def valid_palindrome(s):

  def is_palindrome(word):
    left = 0
    right = len(word) - 1

    while left < right:
      if word[left] != word[right]:
        return False
      left += 1
      right += 1

    return True

  start = 0
  end = len(s) - 1

  while start < end:
    if s[start] != s[end]:
      print(s)
      print(s[start + 1:])
      print(s[start:end])
      return is_palindrome(s[start + 1:]) or is_palindrome(s[start:end])
    start += 1
    end -= 1

  return True


# Example Usage:

s = "aba"
s2 = "abca"
s3 = "abc"

# print(valid_palindrome(s))
# print(valid_palindrome(s2))
# print(valid_palindrome(s3))
# Example Output:

# True
# True
# False

'''
Write a function find_largest_k() that takes in a list of integers nums 
that does not contain any zeroes as a parameter. 
The function finds the largest positive integer k such that -k 
also exists in the array and returns k. 
If there is no such integer, return -1.
'''
def find_largest_k(nums):
  nums.sort()
  largestK = -1

  left = 0
  right = len(nums) -1

  while left < right:
    sum = nums[left] + nums[right]

    if sum < 0:
      left += 1
    elif sum > 0:
      right -=1
    else:
      largestK = max(largestK, nums[right])
      left += 1
      right -= 1
  return largestK


nums = [-1,-2,2,-3,3,-1]
# -3,-2,-1,-1,2,3
# print(find_largest_k(nums))

# nums2 = [-10,2,7,-3]
# print(find_largest_k(nums2))
# Example Output:

# 3
# -1

'''
Write a function count_good_substrings() that takes in a string s as a parameter and returns the number of good substrings of length three. A string is good if there are no repeated characters. A substring is a continuous sequence of characters in a string.
If there are multiple occurrences of the same substring, every occurrence should be counted.
'''
def count_good_substrings(s):
  if len(s) < 3:
    return 0
    
  left = 0
  right = 2
  count = 0

  while right < len(s):
    if len(set(s[left: right+1])) == 3:
      count += 1
      
    left += 1
    right += 1

  return count



# Example Usage:

s1 = "xyzzaz"
s2 = "xyzxyz"
# print(count_good_substrings(s1))
# print(count_good_substrings(s2))
# 1
# 4

'''
Write a function contains_nearby_duplicate() that takes in a list lst and a
positive number k as parameters.

The function returns True if the list contains any duplicate elements within the range k and False otherwise. 

If k is more than the list's size, the solution should check for duplicates in the complete list.
'''
def contains_nearby_duplicate(lst, k):
  element_indices = {}

  for i, element in enumerate(lst):
    # {0:a, 1:b, 2:c, 3:c}
    if element in element_indices and i - element_indices[element] <= k:
      return True
    element_indices[element] = i

  return False
# Example Usage:

lst = [1, 2, 3, 1, 2, 3]
lst2 = [1, 0, 1, 1]
print(contains_nearby_duplicate(lst, 2))
print(contains_nearby_duplicate(lst2, 1))

# Example Output:
# False
# True