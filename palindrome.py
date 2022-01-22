all_palindromes = []
substrings = []
possible = []
probable = []
escalate = []
ignored = []

def palindrome_checker(s):

    for k in range(len(s)):
        if len(s[k]) > 240:
            print("input out of range")
            return


        for i in range(len(s[k])):
            for j in range(i + 1, len(s[k]) + 1):
                substrings.append(s[k][i : j])



        for all_str in substrings:
            rev = ''.join(reversed(all_str))

            if rev == all_str:
                all_palindromes.append(all_str)


        for grade in all_palindromes:
            if len(grade) >= 0 and len(grade) <= 2:
                ignored.append(grade)
            elif len(grade) >= 3 and len(grade) <= 10:
                possible.append(grade)
            elif len(grade) >= 11 and len(grade) <= 40:
                probable.append(grade)
            elif len(grade) >= 41 and len(grade) <= 150:
                escalate.append(grade)

        all_palindromes.clear()
        substrings.clear()

        if len(ignored) != 0 and len(possible) != 0 and len(probable) != 0 and len(escalate) != 0:
            print(s[k][-3 : len(s[k])] + " " + "escalate")
            escalate.clear()
            probable.clear()
            possible.clear()
            ignored.clear()

        elif len(ignored) != 0 and len(possible) != 0 and len(probable) != 0:
            print(s[k][-3 : len(s[k])] + " " + "probable")
            escalate.clear()
            probable.clear()
            possible.clear()
            ignored.clear()

            
        elif len(ignored) != 0 and len(possible) != 0:
            print(s[k][-3 : len(s[k])] + " " + "possible")
            escalate.clear()
            probable.clear()
            possible.clear()
            ignored.clear()


        else:
            print(s[k][-3 : len(s[k])] + " " + "ignored")
            escalate.clear()
            probable.clear()
            possible.clear()
            ignored.clear()
            


messages = int(input("enter number of messages: "))
s = []
for i in range(messages):
    message = str(input("enter message: "))
    s.append(message)

palindrome_checker(s)

        

            

        

        
