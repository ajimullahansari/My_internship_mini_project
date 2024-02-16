import time
#welcome to the user :
print("Welcome to the simple quiz game !")
time.sleep(1)
#chances
chances=1
print("you will have ",chances,"chance to answer correctly.\nplease put the alphabet of the answer\n")
time.sleep(2)
#score
score=0
#question 1
question_1 = print("1) what is the capital of India?\n(a) lucknow \n(b) gujrat \n(c) new-delhi \n(d) punjab \n\n")
answer_1="c"
for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_1):
        print("Correct! Good Job.\n ")
        score = score+1
        break
    else:
        print("Incorrect!\n")
        time.sleep(0.5)
        print("The correct answer is ",answer_1, "\n\n")
time.sleep(2)
#question 2        
question_2 = print("2) who is develop the c language?\n(a) Denish rechei \n(b) ajim \n(c) guido van russum \n(d) maxwell \n\n")
answer_2="a"
for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_2):
        print("Correct! Good Job.\n ")
        score = score+1
        break
    else:
        print("Incorrect!\n")
        time.sleep(0.5)
        print("The correct answer is ",answer_2, "\n\n")
time.sleep(2)
#question 3       
question_3 = print("3) who is the prime minister of Bangladesh?\n(a) Nar--modi \n(b) Shekh hashina  \n(c) guido van russum \n(d) maxwell \n\n")
answer_3="b"
for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_3):
        print("Correct! Good Job.\n ")
        score = score+1
        break
    else:
        print("Incorrect!\n")
        time.sleep(0.5)
        print("The correct answer is ",answer_3, "\n\n")
time.sleep(2)
#question 4       
question_4 = print("4) who is the president of USA?\n(a) Nar--modi \n(b) ajim \n(c) guido van russum \n(d) joe-biden \n\n")
answer_4="d"
for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_4):
        print("Correct! Good Job.\n ")
        score = score+1
        break
    else:
        print("Incorrect!\n")
        time.sleep(0.5)
        print("The correct answer is ",answer_4, "\n\n")
time.sleep(2)
#question 5       
question_5 = print("5) Which planet are called coldest planet ?\n(a) mercury \n(b) jupiter \n(c) urenus \n(d) venus \n\n")
answer_5="c"
for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_5):
        print("Correct! Good Job.\n ")
        score = score+1
        break
    else:
        print("Incorrect!\n")
        time.sleep(0.5)
        print("The correct answer is ",answer_5, "\n\n")
time.sleep(2)
#print the score
while score >= 4:
    print("Well done! Your score was ",score)
    break
while score <= 3:
    print("Better luck next time! Your score was",score)
    break
#Good bye Massage
print("Thank you for playing the simple quiz game!")
#feedback
feedback=input("<<<---Give you feedback here-->>>>")
print(feedback)
print("Thank you soo much for giving the feedback..... ")
