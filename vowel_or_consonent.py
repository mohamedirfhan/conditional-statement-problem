ch=input("Enter a character: ")
if ch.isalpha():
    if ch in ['a','e','i','o','u']:
        print(f"{ch} is vowel")
    else:
        print(f"{ch} is not vowel")
else:
    print("Not a alphabet")