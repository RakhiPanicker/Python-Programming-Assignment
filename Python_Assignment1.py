# 1 String Concatenation - Input from the user and then concatenates Output
String1 = "Hello "
String2 = input("Enter your name: ")
result = String1 + String2
print(result)

# Concatenate String3 and display the output String

String3 = ", Welcome to Python programming"
result = String1 + String2 + String3
print(result)

# String Slicing and Indexing
print(result[0])         # First character of the string
print(result[-1])        # Last character of the string
print(result[0:5])       # First 5 characters of the string
print(result[-11 :])     # Last 11 characters of the string
print(result[::-1])      # String in reverse
print(result[24:30])     # Use slicing and print the word “Python” from the existing string.

# String Methods
strM = "Python beginner tutorial"
print(strM.upper())        # Upper case
print(strM.lower())        # Lower case
print(strM.capitalize())   # Capitalize first letter of a sentence
print(strM.count("t"))     # Count the total number of occurrences of character ‘t’ in the string
print(strM.replace("Python","Machine Learning"))     # Replace "Python" to "Machine Learning"

# Tuples (Creation, Modifi cation and Access) :
t1 = (10,20,30)
t2 = (40,50,60)
t_combine = t1 + t2     
print(t_combine)       # Concatenate the two tuples and store it in “t_combine”
print(t_combine * 3)   # Repeat the elements 3 times from "t_combine"
print(t_combine[2])    # Find the 3rd element from “t_combine"
print(t_combine[0:3])   # Find the first three elements from “t_combine"
print(t_combine[-3:])   #Find the last three elements from “t_combine”