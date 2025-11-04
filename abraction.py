# abstraction is when I hide
# the conplex details for something
# alot more simple

#personal information
# a funtion allows us to wrap data or
# information into a special box or
# enclosure for reuse
# define a function
def personInformation():
    question1 = input("how old are you?")
    question2 = input("where do you live?")
    question3 = input("what school di you go to?")
    print(question1 + question2 + question3)

#call the funtion
personInformation()
personInformation()
personInformation()

# make a funtion that guesses how old you are?
def yearsOld():
    q1 = int(input("What year is it now?"))
    q2 = int(input("what year were you born?"))
    answer = q1 - q2
    result = print(f'you are {answer} years old')

yearsOld()
yearsOld()
yearsOld()2
2
2
