#Data types
# 
#subrcripting - pulling out a character from a string using character position
# print("Hello"[4])
# print("Hello"[-4])
# print(230_293_323)
# print(3.495)
# print(True)

#Data types and functions
# len("goat")
# print(type(False))
# print(type(230))
# print(type(3.454))
# print(type("Adams Apple"))


#Type conversion or type casting - converting data types
# print(int("123") + int("456"))
# print(int("abc") + int("456"))

# print(f"Number of letters in your name: {len(input("Enter your name: "))}"), #Method 1

user_name = input("Enter your name: ")
length_of_name = len(user_name)

print("Number of letters in your name: " + str(length_of_name)) #Method2
# print(len(input("Enter your name")))