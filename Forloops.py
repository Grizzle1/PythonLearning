#Task 1
#Looping strings
#Ask the user to create a string and then print out the strings length and then print each letter of that string. 
name = str(input("what is your name?"))
print(len(name))
for x in name:
    print (x)

#Task2
#I don’t like o’s
#Make a program to take in user input. The program must then print each string character to the string however it will remove all of the letter “o” from the user input. 
name = str(input("what is your name?"))
letter = "o"
for x in letter:
    name = name.replace(letter,"")
for l in name:
    print(l)

#Task3
#Write a for loop program that will print out the numbers from 0 to 10.
number = range(0,11)
for x in number:
    print(x)

#Extension1 - alter the program to make it print from 1 to 10.
number = range(1,11)
for x in number:
    print(x)

#Extension2 - This time make the program count upwards in 4’s.
for number in range(0,100,4):
    print(number)

#Extension3 - Now reverse the countdown. Go backwards from 10 in a sequence of 2’s
for number in reversed(range(0,12,2)):
    print (number)

#Extension4 - When the count gets to three make the program print out “Almost time for blast off”. When the program gets to 0 ensure it states blast off. 

for number in reversed(range(0,11,1)):
    print (number)
    if number == 3:
        print ("Almost time for blast off")
    elif number == 0:
        print ("blast off")

#Extension5 - attempt to create the same programs utilising a while loop.

number = 10
limit = 0
while number >= limit:
    print(number)
    number -=1
    if number == 3:
        print ("Almost time for blast off")
    elif number == -1:
        print ("This Rocket blast off")
##################################################################################################

#Task 3 - Make a program which will ask the user if they wish to count in odd or even numbers and the number they want to count up to. 
Q = str(input("do you wish to count odd or even number?"))
start = int(input("what number you want to start with?"))
end = int(input("what number you want to want to count up to?"))
if (Q) == "odd":
    for x in range (start, end+1):
        if x % 2 != 0:
            print ( x, end =" ")
elif (Q) == "even":
    for x in range (start, end+1):
        if x % 2 == 0:
            print ( x, end =" ")
else:
    print ("sorry your opition is not valid")

#Extension1 - Once at the end of the program make sure to ask the user if they want to go again. 
while True:
    Q = str(input("do you wish to count odd or even number?"))
    start = int(input("what number you want to start with?"))
    end = int(input("what number you want to want to count up to?"))
    if (Q) == "odd":
     for x in range (start, end+1):
          if x % 2 != 0:
               print ( x, end =" ")
    elif (Q) == "even":
     for x in range (start, end+1):
         if x % 2 == 0:
                print ( x, end =" ")
    else:
     print ("sorry your opition is not valid")
    check = input("enter (N) to quit or (Y) to start again?")
    if (check).upper() == "N":
       print ("bye")
       break




