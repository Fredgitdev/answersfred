# Question 1: FizzBuzz
# Write a program that prints the numbers from 1 to 100. For multiples of 3, print "Fizz"; for 
# multiples of 5, print "Buzz"; and for numbers that are multiples of both 3 and 5, print 
# "FizzBuzz"
def fizz_buzz(n):
    for num in range(1, n + 1):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)
fizz_buzz(100)



# Question 2: Fibonacci Sequence
# Write a program to generate the Fibonacci sequence up to 100
def fibonacci_to_100(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_term = fib_sequence[-1] + fib_sequence[-2]
        if next_term <= n:
            fib_sequence.append(next_term)
        else:
            break
    return fib_sequence
fibonacci_sequence = fibonacci_to_100(100)
print(f"Fibonacci sequence:{fibonacci_sequence}")



# Question 3: Power of Two
# Write a program that takes an integer as input and returns true if the input is a power of two.
# Examples: 
# 8=> returns true
# 6=> returns false

def power_of_two(num):
    return num > 0 and (num & (num - 1)) == 0
num = int(input("Enter a number:"))
result = power_of_two(num)
print(result)




# Question 4: Capitalize Words
# Write a program that accepts a string as input, capitalizes the first letter of each word in the 
# string, and then returns the result string.
# Examples: 
# "hi"=> returns "Hi"
# "i love programming"=> returns "I Love Programming"

def capitalize_words(sentence):
    words = sentence.split()
    capitalized_words = [word[0].upper() + word[1:] for word in words]
    result = " ".join(capitalized_words)
    
    return result
sentence = input("Enter a sentence:")
result = capitalize_words(sentence)
print("Result =>:",result)




# Question 5: Reverse Integer
# Write a program that takes an integer as input and returns an integer with reversed digit 
# ordering.
# Examples:
# For input 500, the program should return 5.
# For input -56, the program should return -65.
# For input -90, the program should return -9.
# For input 91, the program should return 19.

def reverse_integer(num):
    # Determining the sign of the number
    sign = -1 if num < 0 else 1
    # Ensuring num is positive 
    num = abs(num)
    reversed_str = ''
    for digit in str(num):
        reversed_str = digit + reversed_str
    reversed_num = int(reversed_str) * sign
    
    return reversed_num
num = int(input("Enter an integer:"))
result = reverse_integer(num)
print(f"Reversed integer of {num} is {result}.")




# Question 6: Count Vowels
# Write a program that counts the number of vowels in a sentence.
# eg " Hello World " => returns 2

def num_vowels(sentence):
    vowels = set("AEIOUaeiou")
    vowel_count = 0
    for char in sentence:
        if char in vowels:
            vowel_count += 1
    
    return vowel_count
sentence = input("Please enter a sentence:")
result = num_vowels(sentence)
print(f"\n \n \n Number of vowels:{result}.")
