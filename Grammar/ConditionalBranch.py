#pythonの条件分岐について記述
a, b = map(int, input().split())

#記述した条件式がTrueだった場合に処理を実行する(後述の条件分岐は無視される)
if a <= 10:
    print("a は、10以下です")
#前述までの条件式とは別の条件式での判定をする場合、「elif 条件式:」のように記述する
elif a <= 50:
    print("a は、50以下です")
elif a <= 70:
    print("a は、70以下です")
#前述までの条件式が全てFalseだった場合の条件判定は、「else:」と記述する
else:
    print("a は、70より大きい数です")
    
#複数の条件を同時に判定したい場合、「and」「or」を使って記述する
if a >= 10 and b >= 50: # -> False
    print("aは10以上、bは50以上の数です")
else:
    print("上記の条件を満たしていません")
    
if a >= 10 or b <= 50: # -> True
    print("aは10以上または、bは50以下の数です")

#三項演算子を用いた条件分岐
print("bは20以上の数です" if b >= 20 else "bは20未満の数です")
#print(a if c else b)

#c ... 条件文
#a ... Trueの場合の出力内容
#b ... Falseの場合の出力内容

#pythonには、if, elif, else で簡単に記述できる、という理由でswitch文がない
#python3.10以降から、新しく「match文」という構文が追加された
name = "Ichiro"

match name:
    case "Ichiro":
        print("He is a baseball player")

    case "Ronaldo":
        print("He is a soccer player")
    
    case "Messi":
        print("He is a soccer player")
    # case "Ronaldo" or "Messi":とはできない

    case _:
        print("He is a professional player")