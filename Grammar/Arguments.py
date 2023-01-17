####################
#引数(Argumant)の参照渡し、値渡しについて

#値渡し...関数を呼び出したり変数を定義したりする時に、元の値を「コピーして渡す」方法
#        (コピーを渡すため、値渡しで定義した変数の値を変更しても呼び出し元の値は変更されない)
#参照渡し...関数を呼び出したり変数を定義したりする時に、そこに「保管されている場所の情報も渡す」方法
#　　　　   (元の変数と新しく定義した変数がメモリ内の同じ場所を見ていることになるので、一方の変更が他方にも反映される)

#変更できないオブジェクトを引数に指定した場合
def func_one(n):
    print(id(n)) #引数nのIDを出力

def pass_by_value_like(n):
    print(n)
    n += 5
    print(n)

a = 10
print(id(a))
func_one(a)
#↑同じIDが出力される -> 同じオブジェクトを参照している

print(a)              # -> 10
pass_by_value_like(a) # -> 10
#                       -> 15
print(a)              # -> 10 ... 呼び出し元の変数の値に変更がない
#これは、関数内で値を更新した時に新しいオブジェクトを参照するようになったため

#変更できるオブジェクトを引数に指定した場合
def func_two(n):
    print(id(n))

def pass_by_refarence(n):
    print(n)
    n[0] += 5
    print(n)

a = [10, 20]
print(id(a))
func_two(a)
#↑同じIDが出力される -> 同じオブジェクトを参照している

print(a)             # -> [10, 20]
pass_by_refarence(a) # -> [10, 20]
#                      -> [15, 20]
print(a)             # -> [15, 20] ... 呼び出し元の変数の値が変更されている
#※List等の変更可能なオブジェクトを値渡しで参照したい場合、「copy(), deepcopy() 関数」を利用する
####################

####################
#位置引数、キーワード引数とは

#呼び出す関数に引数がある場合、「位置引数」「キーワード引数」という記述方法を用いて記述できる
def positional_arg(arg1, arg2):
    print(f"引数1 : {arg1}, 引数2 : {arg2}")

def keyword_arg(arg1, arg2):
    print(f"引数1 : {arg1}, 引数2 : {arg2}")

positional_arg(10, 'aaa')         # -> 引数1 : 10, 引数2 : aaa
keyword_arg(arg1='test', arg2=39) # -> 引数1 : test, 引数2 : 39

"""
位置引数
→ 呼び出し側で指定した引数の値を関数で定義した引数の順番に代入する形式

キーワード引数
→ 呼び出す側でどの仮引数にどの値を渡すのかを 「仮引数の名前=値」 の形で指定する形式
  (入れる値を仮引数に直接指定するため以下のような記述も可)

  ex.) keyword_arg(arg2=39, arg1='test')
"""
####################

####################
#可変長引数「*args」「**kwrags」

"""
*args ... 「*」をつけた引数を定義することで、任意の数の引数を指定できる
             位置引数やキーワード引数と組み合わせることもできる
            (複数の値を引数として渡した場合、それらはタプルとして受け取られる)
            (位置引数のみが渡された場合、空のタプルになる)

**kwargs ... 「**」をつけた引数を定義することで、任意の数の「キーワード引数」を指定できる
                (関数内では、引数名->key, 値->value の辞書として受け取られる)
                ※「**」をつけた引数は、引数の最後でのみ定義できる

両方とも、宣言しておいて使わないこともできる
"""

def tuple_arg(*args):
    print(type(args))
    print(*args)
    print(sum(args))

#以下のように、複数の引数を渡すことができる
tuple_arg(1, 3, 5, 7, 9) # -> <class 'tuple'>
#                          -> 1 3 5 7 9
#                          -> 25

def dic_arg(**kwrags):
    print(type(kwrags))
    print(kwrags)

dic = {'key1' : 1, 'key2' : 2, 'key3' : 3}

dic_arg(test=1) # -> <class 'dict'>
#                 -> {'test': 1}
dic_arg(**dic)  # -> <class 'dict'>
#                 -> {'key1': 1, 'key2': 2, 'key3': 3}
#辞書に「**」をつけて引数に指定することもできる
####################

####################
#「変更可能」「変更不可能」なオブジェクトとは何か
#https://pouhon.net/python-immutable/1831/

#ex.)  変更不可能(イミュータブル)なオブジェクト...文字列、数値、tuple
#      変更可能(ミュータブル)なオブジェクト...list, dict

#1, 変更不可能(イミュータブル)なオブジェクト
tup = (1, 2, 3, 4, 5)
print(id(tup))
print(id((1, 2, 3, 4, 5)))
#↑同じID(識別値)...tupと(1, 2, 3, 4, 5)は、同じ値が代入されている
tup += (6, 7, 8)
print(id(tup))
#↑tupを参照しているのに、さっきとIDが変わっている

"""
変数と値の関係性について
変数名がついた箱に値そのものが入っている ... x
変数と値がそれぞれ別々の領域に確保され、紐でつながっている ... ○

print(id(tup))
print(id((1, 2, 3, 4, 5)))
↑この2行をみた時、上記の2つは同じ値を指し示しているので、同じIDが出力されることになる
tup += (6, 7, 8)
↑ここでは、元々の「tup = (1, 2, 3, 4, 5)」に「(6, 7, 8)」を加えているのではなく
「(1, 2, 3, 4, 5) + (6, 7, 8)」という「新たな値」が生成され、変数tupの参照先(紐のつながる先)を
切り替えている
これにより、2つ目の print(id(tup)) では元のIDとは別のものになっている
(print(id((1, 2, 3, 4, 5))) は、新しく値を生成しているのではなく「既にある値」を読み込んでいる)
"""
#まとめ
#変更不可能とは、何が不可能なのか?
# →「不可能」とは、値そのものを書き換えることが不可能であるということ
#  実際に変更されているのは、変数の「参照先」であって「値そのもの」ではない

#2, 変更可能(ミュータブル)なオブジェクト
li = [1, 2, 3]
print(id(li))
li += [4, 5, 6]
print(id(li))
#↑Listの値が変更されているが、「元の値を上書きしている」ため同じIDが返ってくる

new_li = [1, 2, 3]
tup2 = (new_li, 4, 5)
print(tup2) # -> ([1, 2, 3], 4, 5)
print(id(tup2))
#上記のタプルには、変更可能なオブジェクト(List)が入っている
new_li[0] = 10
print(tup2) # -> ([10, 2, 3], 4, 5)
#↑Listは変更可能なオブジェクトなので、要素の値を変更することができる
print(id(tup2))

"""
この時、Listの中身が「直接書き換えられた」状態であり、
Listもタプルも参照先を切り替えてはいないので
変更後の print(id(tup2)) は元のListと同じIDを出力する
"""
#まとめ
#変更可能とは、何が可能なのか?
# →「可能」とは、変更不可能なオブジェクトとは逆に、
#    値そのものを書き換えることが可能であるということ
####################