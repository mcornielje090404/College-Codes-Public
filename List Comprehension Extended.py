str1 = "Practice Problems to Drill List Comprehendsion In Your Head"

def numberOfSpaces(str1):
    list_spaces = [i for i in str1 if i == " "]
    list_spaces_num = len(list_spaces)
    return(list_spaces_num)

def lessThanFive(str1):
    list_five = str1.split(" ")
    list_under = [i for i in list_five if len(i) < 5]
    return(list_under)

def removeVowel(text):
  return "".join([text for text in text if text not in "aeiouAEIOU"])

print(removeVowel(str1))
print(lessThanFive(str1))
print(numberOfSpaces(str1))
