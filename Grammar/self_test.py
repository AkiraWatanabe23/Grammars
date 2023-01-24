'''「self」とは'''
#https://www.sejuku.net/blog/64106
#https://prograshi.com/language/python/py-self-in-class/
#https://blog.pyq.jp/entry/python_kaiketsu_220720
#https://wa3.i-3-i.info/word1118.html

#↓ クラス、インスタンスの考え方(重要)
#クラス　　　 ... 「設計図」
#インスタンス ... 設計図をもとにして「実際につくったモノ」
#　->インスタンスを生成して処理を実行しても、クラスそのものの値や関数を変更する訳ではない

class SelfBase():
    '''「self」をどのように使うのか?'''
    def method(self): #def(関数)...definition
        '''出力'''
        print("Hello!!")

instance = SelfBase()
instance.method() # -> Hello!!
#self ... そのクラスの現在のインスタンス(つくったモノ)を示すもの
#         クラス内に定義した関数(インスタンスメソッド)の第一引数として扱う

class Instance():
    '''使い方 1 :インスタンスを参照'''
    def __init__(self, str_a, str_b):
        #インスタンス変数...コンストラクタ内で宣言された変数
        self.str_a = str_a
        self.str_b = str_b

test = Instance("Good", "Morning!") #ここでインスタンス化している
print(test.str_a) # -> Good
print(test.str_b) # -> Morning!
# 上記のようにインスタンス(今回は「test」)を生成する時に引数を渡すことで、
# selfを使ってインスタンス変数として代入することができる
# ※呼び出す側は、selfにあたる部分には引数として値を入れない

#以下のように、クラス内のメソッドでインスタンス変数を参照することができる
class ClassVariable():
    '''使い方 2 :クラス内メソッドで参照'''
    #クラス変数...クラス定義内で宣言された変数
    name = 'Name'

    def __init__(self, str_a, str_b):
        self.str_a = str_a
        self.str_b = str_b

    def output(self):
        '''出力'''
        print(self.str_a)
        print(self.str_b)

test = ClassVariable("Good", "Afternoon")
#クラス内の関数を呼び出す
test.output() # -> Good
#                  Afternoon
#クラス変数を出力する
print(test.name) # -> Name

class TestBase():
    '''使い方 3 :クラス継承に使う'''
    def __init__(self):
        self.str_a = "Hello World!"

#↓クラス定義時に、()内にクラス名を記述することでそのクラスを継承することができる
class Inheritance(TestBase):
    '''継承して扱う「self」'''
    def output(self):
        '''出力'''
        print(self.str_a)

test = Inheritance()
test.output() # -> Hello World!
#↑ TestBase(基底クラス)の「self.strA」を参照している

class Warns():
    '''注意点'''
    str_a = "Hello python"

    def __init__(self):
        print(f"1: {self.str_a}") # -> 1: Hello Python (クラス変数「strA」を参照)
        self.str_a = "Hello World!"
        print(f"2: {self.str_a}") # -> 2: Hello World! (インスタンス変数「self.strA」を参照)
        #str_a = "Hello everyone"
        print(f"3: {self.str_a}") # -> 3: Hello World! (インスタンス変数「self.strA」を参照)

test = Warns()

"""
3: の実行結果について
python の仕様として、「self.変数名」の形でクラス変数もインスタンス変数も参照できるが、
同じ名前のクラス変数とインスタンス変数があり、両方に値がある場合、インスタンス変数を優先して参照する

この時、コンストラクタ内でstrA(クラス変数)を"Hello everyone"に変更して出力しようとしたが、
クラス変数「strA」とインスタンス変数「strA」の両方に値が存在するため、
インスタンス変数「strA」("Hello World!")が優先して参照、出力される
"""

#合わせて理解 ... 「cls」
#cls ... クラス自身(設計図)を示すもの
#        「@classmethod」デコレータをつけたメソッド(クラスメソッド)の第一引数として扱う

# self とは何が違うのか?
# → self ... クラスのインスタンス(実際に作ったモノ)を指す
#   cls  ... クラスそのもの(設計図)を指す

class CLSTest:
    '''「cls」について'''
    name = "Mary"

    def __init__(self, word):
        self.word = word

    def call_name(self):
        '''インスタンスメソッド'''
        print(f"My name is {self.word}.")

    @classmethod
    def ask_name(cls):
        '''クラスメソッド'''
        print(f"Your name is {cls.name}, right?")

ins_f = CLSTest("Mike")
ins_s = CLSTest("Tony")

#call_name()はインスタンスメソッドであるため、それぞれのインスタンスの値が参照される
ins_f.call_name() # -> My name is Mike.
ins_s.call_name() # -> My name is Tony.

#ask_name()はクラスメソッドであるため、クラス変数「name = "Mary"」が参照される
ins_f.ask_name()  # -> Your name is Mary, right?
ins_s.ask_name()  # -> Your name is Mary, right?
