import random

def play():
    print("🎮 歡迎來到『猜數字』小遊戲！")
    answer = random.randint(1, 100)
    tries = 0

    while True:
        s = input("請輸入 1~100 的數字（或輸入 q 離開）：").strip()

        if s.lower() == "q":
            print("👋 遊戲結束～")
            break

        if not s.isdigit():
            print("⚠️ 請輸入數字！")
            continue

        guess = int(s)
        tries += 1

        if guess < answer:
            print("太小了～")
        elif guess > answer:
            print("太大了～")
        else:
            print(f"🎉 恭喜猜對！答案是 {answer}，你猜了 {tries} 次。")
            break

if __name__ == "__main__":
    play()