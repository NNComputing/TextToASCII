# Function to convert from ASCII list to a string using while loops

def decrypted(nums):
  result = "" # empty string to contain final result at the end
  count = 0
  while count < len(nums):
    result += chr(nums[count]) # iterates through the list and adds string values to result
    count += 1 # count increases by 1 until length of list is reached to avoid an infinite loop


# main
sample = [67, 111, 109, 112, 117, 116, 105, 110, 103, 32, 105, 115, 32, 73, 110, 116, 101, 114, 101, 115, 116, 105, 110, 103]
print(decrypted(sample)) # returns 'Computing is Interesting'

#### MADE BY NAVIN AMAL ANAND ASRJC CLASS 24/12 ####
