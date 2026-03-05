import random

def play():
    choices = ["剪刀", "石頭", "布"]
    print("🎮 歡迎來到剪刀石頭布遊戲！")
    print("輸入：剪刀 / 石頭 / 布")
    print("輸入 q 可以離開遊戲")

    while True:
        user = input("請輸入你的選擇：").strip()

        if user.lower() == "q":
            print("👋 遊戲結束，再見！")
            break

        if user not in choices:
            print("⚠️ 請輸入：剪刀、石頭、布")
            continue

        computer = random.choice(choices)
        print(f"電腦出的是：{computer}")

        if user == computer:
            print("平手！")
        elif (user == "剪刀" and computer == "布") or \
             (user == "石頭" and computer == "剪刀") or \
             (user == "布" and computer == "石頭"):
            print("🎉 你贏了！")
        else:
            print("😢 你輸了！")

play()