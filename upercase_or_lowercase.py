chr=input("Enter a character: ")
if len(chr)!=1:
    print("Enter only one character!!")
else:
    asci=ord(chr)
    if 65<=asci<=90:
        print(f"The '{chr}' is a upper case")
    elif 97<=asci<=122:
        print(f"The '{chr}' is a lower case")
    else:
        print(f"The '{chr}' is not a character!!")