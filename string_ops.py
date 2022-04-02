def find_nth_occurrence(substring, string, occurrence = 1):
    id = -1
    for i in range(occurrence):
        id = string.find(substring, id + 1)
        if id == -1:
            return -1
    return print(id)




try:
    def solve(a, b):

        if a == b:
            print(True)
        elif '*' in a:
            if (len(a)-1) <= len(b):
                return print(True)
            else:
                return print(False)
        else:
            return print(False)
    
except:
    print("wrong input")




def is_palindrome(s):
    palindrome = False
    s = s.lower()
  
    if s == s[::-1]:
      palindrome = True

    return print(palindrome)