import sys
import random

while True:
    question = input("Ask the magic 8 ball a question: (press enter to quit) ")

    answers = random.randint(0, 7)

    PrimList = ["It is certain", "Outlook good", "You may rely on it", "Ask again later",
                "Concentrate and ask again", "Reply hazy, try again", "My reply is no", "My sources say no"]

    if question == "":
        sys.exit()
    else:
        print(PrimList[answers])
