import random

def number_guessing():

    answer = random.randint(100, 999)
    attempts = 0
    max_attempts = 10
    history = []

    print("3桁の数字を入力してください")

    while attempts < max_attempts:
        guess = int(input("\n\nあと{}回 回答できます: ".format(max_attempts - attempts)))
        if not (100 <= guess <= 999):
            print("【3桁】の数字を入力してください")
            continue

        history.append(guess)

        if guess < answer:
            print("もっと大きいです")
        elif guess > answer:
            print("もっと小さいです")
        else:
            print("\n\n正解!")
            break

        attempts += 1

        print("ヒント: ", end = "")
        for attempt, past_guess in enumerate(history, 1):
            if attempt > 1:
                print(", ", end = "")
            if past_guess < answer:
                print(">{}".format(past_guess), end = "")
            else:
                print("<{}".format(past_guess), end = "")

    else:
        print("\n\n\n残念! 答えは{}でした".format(answer))

number_guessing()