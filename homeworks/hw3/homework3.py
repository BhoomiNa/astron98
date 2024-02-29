import math
####################################
# Question 1
####################################
def power(x,y):
    answer = 1
    for z in range(0, y, 1):
        print("z", z, "answer", answer)
        answer *= x
    return answer

# I decided to do hyperoperations to make you proud :) 
def tetra(x,y):
    output = 1
    for k in range(y):
        output = power(x, output)
    return output

####################################
# Question 2
####################################
def min_max(nums):
    return (min(nums), max(nums))

####################################
# Question 3
####################################

def leap_check(year):
    if (year % 4 == 0):
        if (year % 100 != 0 or year % 400 == 0):
            return True
    return False

####################################
# Question 4
####################################

def bmi(weight,height):
    return weight / height**2

####################################
# Question 5
####################################

def rotate_digits(n):
    last_num = n % 10
    remain = n // 10
    if (remain == 0): return n # Return the input if it has one digit
    digits = math.floor(math.log(remain,10)) + 1
    return last_num*10**digits + remain

####################################
# Question 6
####################################

#for loop
def min_for(num_list):
    Min_Val = math.inf
    for var in num_list :
        if Min_Val > var :
            Min_Val = var
    return Min_Val

def max_for(num_list):
    Max_Val = -math.inf
    for var in num_list :
        if Max_Val < var :
            Max_Val = var
    return Max_Val

#while loop
def max_while(num_list):
    x = 0
    max_val = -math.inf
    while (x < len(num_list)) :
        if max_val < num_list[x] :
            max_val = num_list[x]
        x += 1
    return max_val

def min_while(num_list):
    x = 0
    min_val = math.inf
    while(x < len(num_list)) :
        if min_val > num_list[x] :
            min_val = num_list[x]
        x += 1
    return min_val

####################################
# Question 7
####################################

def vowel_finder(word):
    vowel = "aeiouAEIOU"
    x = 0
    for letter in word:
        if letter in vowel:
            x += 1
    return x


####################################
# Question 8
####################################

def digital_root_for(num):
    sum = 0
    digit_count = math.floor(math.log(num,10)+1)
    for digit_pos in range(0,digit_count):
        print(num)
        last_digit = num % 10
        sum += last_digit
        num = (num - last_digit) / 10
    return sum

#i tried the while loop too

def digital_root_while(num):
    sum = 0
    while(num > 0):
        last_digit = num % 10
        sum += last_digit
        num = (num - last_digit) / 10
    return sum