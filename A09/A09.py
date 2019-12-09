#Benjamin Shelton and Garrett Morris
#A09
#Simple python program that generates users and has them send messages and times 
#how long it took, by default it's 1000000 users, but can be paramaterized as well.
from random import randint
from time import time
from time import sleep
#startTime is universal
startTime = time()

choice = input("Generic or Paramaterized? (G or P)")
choice = choice.upper()

if choice == 'G':
    for x in range(1000000):
        #Generate percentage for age
        age = randint(1, 100)
        #13-17
        if age <= 6:
            age = 1
        #18-24
        elif age <= 31:
            age = 2
        #25-34
        elif age <= 63:
            age = 3
        #35-44
        elif age <= 78:
            age = 4
        #45-54
        elif age <= 88:
            age = 5
        #55-64
        elif age <= 94:
            age = 6 
        #65+
        else:
            age = 7
        #We just kind of eyeballed the number of messages sent by each age group
        if age == 1:
            messages = randint(50, 150)
        elif age == 2:
            messages = randint(25,100)
        elif age == 3:
            messages = randint(15, 75)
        elif age == 4:
            messages = randint(75, 140)
        elif age == 5:
            messages = randint(50, 75)
        elif age == 6:
            messages = randint(5, 15)
        elif age == 7:
            messages = randint(30, 80)
        #Simple print statement so we know it's running
        for y in range(messages):
            print("Message " + str(y) + " Sent from User " + str(x))

elif choice == "P":
    print("If you don't want to change the parameters just input 0")
    users = input("Number of users: ")
    users = int(users)

    delay = input("Delay time per message: ")
    delay = float(delay)

    numMessages = input("Number of messages sent: ")
    numMessages = int(numMessages)

    runTime = input("Run time desired (Input Syntax: min, sec): ")
    runTime = runTime.strip(",")
    runTime = [int(runTime[0]), int(runTime[2])]
    #if we want a certain number of users
    if users > 0:
        #if we want a certain time limit, also we assume if you want a time limit, you won't want to limit the number of messages
        if runTime[1] > 0:
            runTime = (runTime[0] * 60) + runTime[1]

            while time()-startTime < runTime:
                for x in range(users):
                    age = randint(1, 100)
                    #13-17
                    if age <= 6:
                        age = 1
                    #18-24
                    elif age <= 31:
                        age = 2
                    #25-34
                    elif age <= 63:
                        age = 3
                    #35-44
                    elif age <= 78:
                        age = 4
                    #45-54
                    elif age <= 88:
                        age = 5
                    #55-64
                    elif age <= 94:
                        age = 6 
                    #65+
                    else:
                        age = 7

                    if age == 1:
                        messages = randint(50, 150)
                    elif age == 2:
                        messages = randint(25,100)
                    elif age == 3:
                        messages = randint(15, 75)
                    elif age == 4:
                        messages = randint(75, 140)
                    elif age == 5:
                        messages = randint(50, 75)
                    elif age == 6:
                        messages = randint(5, 15)
                    elif age == 7:
                        messages = randint(30, 80)
                    
                    for y in range(messages):
                        print("Message " + str(y) + " Sent from User " + str(x))
                        #if there be a delay
                        if delay > 0:
                            sleep(delay)
        #if we want a certain amount of messages
        elif numMessages > 0:
            totalMessages = 0
            while totalMessages < numMessages:
                for x in range(users):
                    age = randint(1, 100)
                    #13-17
                    if age <= 6:
                        age = 1
                    #18-24
                    elif age <= 31:
                        age = 2
                    #25-34
                    elif age <= 63:
                        age = 3
                    #35-44
                    elif age <= 78:
                        age = 4
                    #45-54
                    elif age <= 88:
                        age = 5
                    #55-64
                    elif age <= 94:
                        age = 6 
                    #65+
                    else:
                        age = 7

                    if age == 1:
                        messages = randint(50, 150)
                    elif age == 2:
                        messages = randint(25,100)
                    elif age == 3:
                        messages = randint(15, 75)
                    elif age == 4:
                        messages = randint(75, 140)
                    elif age == 5:
                        messages = randint(50, 75)
                    elif age == 6:
                        messages = randint(5, 15)
                    elif age == 7:
                        messages = randint(30, 80)
                    
                    for y in range(messages):
                        print("Message " + str(y) + " Sent from User " + str(x))
                        if delay > 0:
                            sleep(delay)
                        totalMessages += 1
                        #the way the for loop above works, it will send more messages even after we hit the totalMessage cap
                        if totalMessages >= numMessages:
                            break
                    #same idea as the other break, gets us to the while loop so we can stop, else it'll print out users-1 more messages
                    if totalMessages >= numMessages:
                        break
        else:
            for x in range(users):
                age = randint(1, 100)
                #13-17
                if age <= 6:
                    age = 1
                #18-24
                elif age <= 31:
                    age = 2
                #25-34
                elif age <= 63:
                    age = 3
                #35-44
                elif age <= 78:
                    age = 4
                #45-54
                elif age <= 88:
                    age = 5
                #55-64
                elif age <= 94:
                    age = 6 
                #65+
                else:
                    age = 7

                if age == 1:
                    messages = randint(50, 150)
                elif age == 2:
                    messages = randint(25,100)
                elif age == 3:
                    messages = randint(15, 75)
                elif age == 4:
                    messages = randint(75, 140)
                elif age == 5:
                    messages = randint(50, 75)
                elif age == 6:
                    messages = randint(5, 15)
                elif age == 7:
                    messages = randint(30, 80)
                
                for y in range(messages):
                    print("Message " + str(y) + " Sent from User " + str(x))
                    if delay > 0:
                        sleep(delay)
    #if we want 1,000,000 users
    else:
        if runTime[1] > 0:
            runTime = (runTime[0] * 60) + runTime[1]

            while time()-startTime < runTime:
                for x in range(1000000):
                    age = randint(1, 100)
                    #13-17
                    if age <= 6:
                        age = 1
                    #18-24
                    elif age <= 31:
                        age = 2
                    #25-34
                    elif age <= 63:
                        age = 3
                    #35-44
                    elif age <= 78:
                        age = 4
                    #45-54
                    elif age <= 88:
                        age = 5
                    #55-64
                    elif age <= 94:
                        age = 6 
                    #65+
                    else:
                        age = 7

                    if age == 1:
                        messages = randint(50, 150)
                    elif age == 2:
                        messages = randint(25,100)
                    elif age == 3:
                        messages = randint(15, 75)
                    elif age == 4:
                        messages = randint(75, 140)
                    elif age == 5:
                        messages = randint(50, 75)
                    elif age == 6:
                        messages = randint(5, 15)
                    elif age == 7:
                        messages = randint(30, 80)
                    
                    for y in range(messages):
                        print("Message " + str(y) + " Sent from User " + str(x))
                        #if there be a delay
                        if delay > 0:
                            sleep(delay)
        #if we want a certain amount of messages
        elif numMessages > 0:
            totalMessages = 0
            while totalMessages < numMessages:
                for x in range(1000000):
                    age = randint(1, 100)
                    #13-17
                    if age <= 6:
                        age = 1
                    #18-24
                    elif age <= 31:
                        age = 2
                    #25-34
                    elif age <= 63:
                        age = 3
                    #35-44
                    elif age <= 78:
                        age = 4
                    #45-54
                    elif age <= 88:
                        age = 5
                    #55-64
                    elif age <= 94:
                        age = 6 
                    #65+
                    else:
                        age = 7

                    if age == 1:
                        messages = randint(50, 150)
                    elif age == 2:
                        messages = randint(25,100)
                    elif age == 3:
                        messages = randint(15, 75)
                    elif age == 4:
                        messages = randint(75, 140)
                    elif age == 5:
                        messages = randint(50, 75)
                    elif age == 6:
                        messages = randint(5, 15)
                    elif age == 7:
                        messages = randint(30, 80)
                    
                    for y in range(messages):
                        print("Message " + str(y) + " Sent from User " + str(x))
                        if delay > 0:
                            sleep(delay)
                        totalMessages += 1
                        #the way the for loop above works, it will send more messages even after we hit the totalMessage cap
                        if totalMessages >= numMessages:
                            break
                    #same idea as the other break, gets us to the while loop so we can stop, else it'll print out users-1 more messages
                    if totalMessages >= numMessages:
                        break
        else:
            for x in range(1000000):
                age = randint(1, 100)
                #13-17
                if age <= 6:
                    age = 1
                #18-24
                elif age <= 31:
                    age = 2
                #25-34
                elif age <= 63:
                    age = 3
                #35-44
                elif age <= 78:
                    age = 4
                #45-54
                elif age <= 88:
                    age = 5
                #55-64
                elif age <= 94:
                    age = 6 
                #65+
                else:
                    age = 7

                if age == 1:
                    messages = randint(50, 150)
                elif age == 2:
                    messages = randint(25,100)
                elif age == 3:
                    messages = randint(15, 75)
                elif age == 4:
                    messages = randint(75, 140)
                elif age == 5:
                    messages = randint(50, 75)
                elif age == 6:
                    messages = randint(5, 15)
                elif age == 7:
                    messages = randint(30, 80)
                
                for y in range(messages):
                    print("Message " + str(y) + " Sent from User " + str(x))
                    if delay > 0:
                        sleep(delay)

else:
    print("Invalid choice (G or P, silly)")
#Final printout of the total time it took
endTime = time() - startTime
print("Total time spent sending messages: " + str(int(endTime / 60)) + " minutes and " + str(endTime % 60) + " seconds")
