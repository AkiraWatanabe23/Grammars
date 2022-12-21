name = 'aaa'

#以下のように、文字列は「" "」「' '」のどちらで記述してもよい
print('Hello')
print(f"Your name is {name}, right? \n Please answer with 'yes' or 'no'.")

#以下のように(変数名の後に型名)記述することで、変数の型を指定することができる
call: str = input()

if call == "yes":
    #以下のformat(f"... { } ...")で記述することで、文字列の中に { } で変数を入れることができる
    print(f"{name}, Nice to meet you.")
elif call == "no":
    print("Sorry, please tell me your name.")
else:
    print("Please answer with 'yes' or 'no'.")