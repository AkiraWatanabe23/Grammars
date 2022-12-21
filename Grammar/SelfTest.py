#https://www.sejuku.net/blog/64106
#https://prograshi.com/language/python/py-self-in-class/
#https://blog.pyq.jp/entry/python_kaiketsu_220720
#https://wa3.i-3-i.info/word1118.html

#↓ クラス、インスタンスの考え方(重要)
#クラス　　　 ... 「設計図」
#インスタンス ... 設計図をもとにして「実際につくったモノ」
#　->インスタンスを生成して処理を実行しても、クラスそのものの値や関数を変更する訳ではない

class SelfBase():
    def method(self): #def(関数)...definition
        print("Hello!!")

instance = SelfBase()
instance.method() # -> Hello!!
#self ... そのクラスの現在のインスタンス(つくったモノ)を示すもの
#         クラス内に定義した関数(インスタンスメソッド)の第一引数として扱う

"""
もし、class内で定義したメソッドに引数を1つも渡さなかった場合(使う、使わないに関わらず)
「TypeError: クラス名.メソッド名() takes 0 positional arguments but 1 was given」
(メソッドには1つの引数が必須ですが、0個しか渡されていません)というエラーが出る

why?
pythonでは、クラスをインスタンスとしてから中の関数を呼び出す場合、
「関数(function)」としてではなく、「メソッド(method)」として呼び出す
この時、メソッドにはインスタンス自身を引数として渡さなければいけない設定になっているため、
インスタンス自身が入る引数を渡す必要がある
このインスタンス自身を入れる引数に習慣として「self」が使われる
"""

#使い方 1 :インスタンス変数として参照する
class Instance():
    def __init__(self, strA, strB):
        #インスタンス変数...コンストラクタ内で宣言された変数
        self.strA = strA
        self.strB = strB

test = Instance("Good", "Morning!") #ここでインスタンス化している
print(test.strA) # -> Good
print(test.strB) # -> Morning!
"""
上記のようにインスタンス(今回は「test」)を生成する時に引数を渡すことで、
selfを使ってインスタンス変数として代入することができる
※呼び出す側は(selfにあたる部分には)引数として値を入れない
"""

#使い方 2 :クラス内メソッドで参照する
#以下のように、クラス内のメソッドでインスタンス変数を参照することができる
class ClassVariable():
    #クラス変数...クラス定義内で宣言された変数
    name = 'Name'

    def __init__(self, strA, strB):
        self.strA = strA
        self.strB = strB

    def output(self):
        print(self.strA)
        print(self.strB)

test = ClassVariable("Good", "Afternoon...") #インスタンス化
#クラス内の関数を呼び出す
test.output() # -> Good (\n) Afternoon...
#クラス変数を出力する
print(test.name) # -> Name

#使い方 3 :クラス継承に使う
#selfはクラス変数として参照できるため、クラスを継承した時にも参照することができる
class TestBase():
    def __init__(self):
        self.strA = "Hello World!"

#↓クラス定義時に、()内にクラス名を記述することでそのクラスを継承することができる
class Inheritance(TestBase):
    def output(self):
        print(self.strA)

test = Inheritance()
test.output() # -> Hello World!

#注意点↓
class Warns():
    strA = "Hello python"

    def __init__(self):
        print(f"1: {self.strA}") # -> 1: Hello Python (クラス変数「strA」を参照)
        #インスタンス変数
        self.strA = "Hello World!"
        print(f"2: {self.strA}") # -> 2: Hello World! (インスタンス変数「self.strA」を参照)
        strA = "Hello everyone"
        print(f"3: {self.strA}") # -> 3: Hello World! (インスタンス変数「self.strA」を参照)

test = Warns()

"""
3: の実行結果について
python の仕様として、「self.変数名」の形でクラス変数もインスタンス変数も参照できるが、
同じ名前のクラス変数とインスタンス変数があり、両方に値がある場合、インスタンス変数を優先して参照する

この場合、コンストラクタ内でstrA(クラス変数)を"Hello everyone"に変更して出力しようとしたが、
この時点でクラス変数「strA」とインスタンス変数「strA」の両方に値が存在するため、
インスタンス変数「strA」("Hello World!")が優先して出力される
"""


#合わせて理解 ... 「cls」
#cls ... クラス自身(設計図)を示すもの
#        「@classmethod」デコレータをつけたメソッド(クラスメソッド)の第一引数として扱う

"""
self とは何が違うのか?
→ self ... クラスのインスタンス(実際に作ったモノ)を指す
  cls  ... クラスそのもの(設計図)を指す
"""

class CLSTest:
    name = "Mary"

    def __init__(self, word):
        self.word = word

    def call_name(self):
        print(f"My name is {self.word}.")

    @classmethod
    def ask_name(cls):
        print(f"Your name is {cls.name}, right?")

ins_f = CLSTest("Mike")
ins_s = CLSTest("Tony")

ins_f.call_name() # -> My name is Mike.
ins_s.call_name() # -> My name is Tony.
#call_name()はインスタンスメソッドであるため、それぞれのインスタンスの値が参照される

ins_f.ask_name()  # -> Your name is Mary, right?
ins_s.ask_name()  # -> Your name is Mary, right?
#ask_name()はクラスメソッドであるため、クラス変数「name = "Mary"」が参照される