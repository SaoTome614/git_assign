import random

def number_guessing():

    answer = random.randint(100, 999)
    attempts = 0
    max_attempts = 10

    print("3桁の数字を入力してください")

    while attempts < max_attempts:
        guess = int(input(""))
        if not (100 <= guess < 999):
            print("【3桁】の数字を入力してください")
            continue

        if guess < answer:
            print("もっと大きいです")
        elif guess > answer:
            print("もっと小さいです")
        else:
            print("正解!")
            break

        attempts += 1
    
    else:
        print("残念! 答えは{}でした".format(answer))

number_guessing()