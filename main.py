# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# .lower() could also be use but .casefold() will make even Bobby JAMes lower case .lower() wouls not.
new_name1=name1.casefold()
new_name2=name2.casefold()
new_name3 = new_name1 +' '+ new_name2

t = new_name3.count('t')
r = new_name3.count('r')
u = new_name3.count('u')
e = new_name3.count('e')

l = new_name3.count('l')
o = new_name3.count('o')
v = new_name3.count('v')
e = new_name3.count('e')

true = t + r + u + e
love = l + o + v + e
true_love = str(true) + str(love)

# print(true_love)
# true_love_score = int(true_love) or true_love = int(str(true) + str(love)) could be used to fix the concatenation error.

true_love_score = int(true_love)

if true_love_score < 10 or true_love_score > 90:
    print(f'Your score is {true_love_score}, you go together like coke and mentos.')
elif true_love_score >= 40 and true_love_score <= 50:
    print(f'Your score is {true_love_score}, you are alright together.')
else:
    print(f'Your score is {true_love_score}.')


