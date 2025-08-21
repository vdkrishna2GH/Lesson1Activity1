print(ord('#'))
print(ord('$'))
print(ord('R'))
print(ord('A'))
print(ord('M'))

print("Enter a Character: ", end="")
c = input()
if len(c)>1:
    print("\nInvalid Input!")
else:
    if c>='a' and c<='z':
        print("\n\"" +c+ "\" is an lower case alphabet.")
    elif c>='A' and c<='Z':
        print("\n\"" +c+ "\" is an upper case alphabet.")
    else:
        print("\n\"" +c+ "\" is not an alphabet!")