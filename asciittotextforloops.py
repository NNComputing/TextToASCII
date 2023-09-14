# Function to convert from ASCII list to a string using for loops

def decrypted(nums):
  result = "" # empty string to contain final result at the end
  for num in nums:
    result += chr(num) # iterates through the list and adds the string value to result
  return result


# main
sample = [67, 111, 109, 112, 117, 116, 105, 110, 103, 32, 105, 115, 32, 73, 110, 116, 101, 114, 101, 115, 116, 105, 110, 103]
print(decrypted(sample)) # returns 'Computing is Interesting'

#### MADE BY NAVIN AMAL ANAND ASRJC CLASS 24/12 ####
