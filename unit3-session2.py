# '''
# Problem 1: Sum of Strings

# Write a function sum_of_number_strings() that takes in a list of strings nums. Each string is a representations of integers. The function should return the sum of these strings as an integer.
# '''

# def sum_of_number_strings(nums):
#     total = 0

#     for num in nums:
#         total += int(num)

#     return total

# nums = ["10", "20", "30"]
# sum = sum_of_number_strings(nums)
# print(sum)
# # Example Output: 60
# '''
# Write a function remove_duplicates() that takes in a sorted list of integers nums as a parameter and removes all duplicates in the list. The function returns the modified list.
# '''

# # mutating a list in a while loop is safer than a for loop
# def remove_duplicates(nums):
#     if not nums:
#         return []
#     i = 0

#     while i < len(nums) - 1:
#         if nums[i] == nums[i + 1]:
#             nums.pop(i + 1)
#         else:
#             i += 1
#     return nums

# nums = [1, 1, 1, 2, 3, 4, 4, 5, 6, 6]

# print(remove_duplicates(nums))
# print(remove_duplicates(None))
# # Example Output: no_dups = [1,2,3,4,5,6]

# '''
# Write a function reverse_only_letters() that takes in a string s as a parameter. The function reverses the order of the letters in the string and returns the new string. Non-letter characters should remain in their original positions.
# '''

# def reverse_only_letters(s):
#     front = 0
#     back = len(s) -1
#     s_list = list(s)

#     while front <= back:
#         if not s_list[front].isalpha():
#             front += 1
#         if not s_list[back].isalpha():
#             back -= 1
#         else:
#             s_list[front], s_list[back] = s_list[back], s_list[front]
#             front += 1
#             back -= 1

#     return "".join(s_list)

# s = "a-bC-dEf-ghIj"
# reversed_s = reverse_only_letters(s)
# print(reversed_s)
# # Example Output: j-Ih-gfE-dCba

# '''
# Problem 4: Longest Uniform Substring
# Write a function longest_uniform_substring() that takes in a string s and returns the length of the longest uniform substring. A uniform substring consists of a single repeated character.
# '''

# def longest_uniform_substring(s):

# s1 = "aabbbbCdAA"
# l1 = longest_uniform_substring(s1)
# print(l1)

# s2 = "abcdef"
# l1 = longest_uniform_substring(s2)
# print(l1)

# # Example Output:
# # 4
# # 1

# #-----------------------------------------
# '''
# Write a function longest_uniform_substring() that takes in a string s and returns the length of the longest uniform substring. A uniform substring consists of a single repeated character.
# '''

# def longest_uniform_substring(s):
#     if not s:
#         return 0  # If the string is empty, return 0 as there are no substrings

#     max_length = 1  # Start with 1 because any single character is a uniform substring
#     current_length = 1  # The current uniform substring length also starts at 1

#     # Start from the second character and go through the string
#     for i in range(1, len(s)):
#         if s[i] == s[i-1]:
#             current_length += 1  # Increment the length if the current character matches the previous one
#             max_length = max(max_length, current_length)  # Update the maximum length found so far
#         else:
#             current_length = 1  # Reset current length if the current character does not match the previous one

#     return max_length  # Return the maximum length of uniform substring found

# #Example Usage:

# s1 = "aabbbbCdAA"
# #l1 = longest_uniform_substring(s1)
# #print(l1)

# #s2 = "abcdef"
# #l1 = longest_uniform_substring(s2)
# #print(l1)

# #-------------------------------------------------
'''
In the game League of Legends, Teemo attacks his enemy Ashe with poison arrows. Write a 
function find_poisoned_duration() that takes in two parameters: time_series (the time at which Teemo's attacks hits Ashe) 
and time_duration (the duration of the poisoning effect). 
The function returns the total 
time that Ashe is in a poisoned condition.

time_series is a list of integers that represents the times at which Teemo attacks and 
makes Ashe poisoned for the exact time_duration.

If Teemo hits Ashe while she is still poisoned, the poison's duration starts over. For example,
if Teemo attacks at times 1 and 4 for 3 seconds, the states at each time would be:

find_poisioned_duration([1,4], 3):
1: attacked
2: in poison state
3: in poison state
4: attacked, poison duration resets to 3
5: in poison state
6: in poison state
7: in poison state
8: in normal state
This means that the total time that Ashe is in a poisoned condition is 5.
'''


def find_poisioned_duration(time_series, duration):
    total_duration = 0
    for i in range(len(time_series) - 1):
        # Calculate the actual poisoning time between two attacks
        actual_duration = min(time_series[i + 1] - time_series[i], duration)
        total_duration += actual_duration
    # Add the duration of the last attack
    total_duration += duration
    return total_duration


print(find_poisioned_duration([1, 4], 3))
'''Example Usage:

time_series = [1,4,9]
damage = find_poisoned_duration(time_series, 3)
print(damage)
Example Output: 8
'''
