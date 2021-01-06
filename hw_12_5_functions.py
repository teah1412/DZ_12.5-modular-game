import json
import random
import datetime

def play_game(level="easy"):
    secret = random.randint(1, 30)
    attempts = 0
    score_list = get_score_list()

    while True:
        guess = int(input("Guess the secret number (between 1 and 30): "))
        attempts += 1

        if guess == secret:
            score_list.append({"attempts": attempts, "date": str(datetime.datetime.now())})
            with open("score_list.txt", "w") as score_file:
                score_file.write(json.dumps(score_list))

            print("You've guessed it - congratulations! It's number " + str(secret))
            print("Attempts needed: " + str(attempts))
            break
        elif guess > secret and level == "easy":
            print("Your guess is not correct... try something smaller")
        elif guess < secret and level == "easy":
            print("Your guess is not correct... try something bigger")
        elif attempts % 5 == 0:
            change_level = input("would you like to change the level to easy? (The easy level gives you hints) (Y/N): ")
            if change_level.upper() == "Y":
                play_game(level="easy")
            else:
                continue
        else:
            print("Your guess is not correct.")


        while True:
            guess = int(input("Guess the secret number (between 1 and 30): "))
            attempts += 1

            if guess == secret:
                score_list.append({"attempts": attempts, "date": str(datetime.datetime.now())})
                with open("score_list.txt", "w") as score_file:
                    score_file.write(json.dumps(score_list))

                print("You've guessed it - congratulations! It's number " + str(secret))
                print("Attempts needed: " + str(attempts))
                break
            else:
                print("Your guess is not correct... try again")




def get_score_list():
    with open("score_list.txt", "r") as score_file:
        score_list = json.loads(score_file.read())
        return score_list

def get_top_scores():
    score_list = get_score_list()
    top_score_list = sorted(score_list, key=lambda k: k['attempts'])[:3]
    return top_score_list



