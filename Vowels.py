wrd = input("Enter A Word: ")

wrd = wrd.lower()

def _count():
    global vow_count
    global con_count
    global num_count
    global space
    global special

    vow_count = 0
    con_count = 0
    num_count = 0
    space = 0
    special = 0
    vowels = ['a','e','i','o','u']

    for let in wrd:
        _ascii = ord(let)
        if let in vowels:
            vow_count+=1
        elif 65 <= _ascii <= 90 or 97 <= _ascii <= 122:
            con_count+=1
        elif _ascii == 32:
            space+=1
        elif 47 <= _ascii <= 56:
            num_count+=1
        else:
            special+=1

def _output():
    print("\nOutput:-")
    print(f"The Number Of Vowels in this string is {vow_count}.")
    print(f"The Number of Consonants In This String Is {con_count}.")
    print(f"The Number of Digits In This String Is {num_count}.")
    print(f"The Number of Spaces In This String Is {space}.")
    print(f"The Number of Special Characters In This String Is {special}.")

_count()
_output()
