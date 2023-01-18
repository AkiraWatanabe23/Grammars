#pythonの条件分岐について記述
num = 100

#1つの条件について判定する場合、以下のように「if 条件式:」のように記述する
#記述した条件式がTrueだった場合に処理を実行する(後述の条件分岐は無視される)
if num <= 10:
    print("num は、10以下です")
#前述までの条件式とは別の条件式での判定をする場合、「elif 条件式:」のように記述する
elif num <= 50:
    print("num は、50以下です")
elif num <= 70:
    print("num は、70以下です")
#前述までの条件式が全てFalseだった場合の条件判定は、「else:」と記述する
else:
    print("num は、70より大きい数です")
    
#複数の条件を同時に判定したい場合、「and」「or」を使って記述する
a = 10
b = 45

if a >= 10 and b >= 50: # -> False
    print("上記の条件を満たしています")
else:
    print("上記の条件を満たしていません")
    
if a >= 10 or b <= 50: # -> True
    print("少なくとも上記の条件のうち片方は満たしています")
    
#「and」「or」は、2つ以上の条件を並べることも可能

#三項演算子を用いた条件分岐
n = 50
print("Yes" if n >= 20 else "No")
#print(a if c else b)

#c ... 条件文
#a ... Trueの場合の出力内容
#b ... Falseの場合の出力内容

#pythonには、他の言語に存在する「switch文」がない

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