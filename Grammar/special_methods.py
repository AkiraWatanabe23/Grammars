'''pythonの特殊メソッド各種について記述'''
#https://blog.codecamp.jp/python-class-code

class Test:
    '''コンストラクタ'''
    #「__init__」pythonにおけるコンストラクタ(データの初期化)
    #インスタンスを生成した時に実行される関数
    #「None」...この関数の戻り値の型(Noneの場合、戻り値なし)
    def __init__(self, name) -> None:
        self.name = name

    def output(self):
        '''出力'''
        print(self.name)

instance = Test("aaa")
instance.output() # -> aaa


class FourArithmetic:
    '''四則演算(「+」「-」「*」「/」「//」)'''
    #戻り値の型を指定する「 -> xxx」は、記述しなくてもよい
    #(ただし、戻り値がある場合は記述しておいた方が型が分かりやすい)
    def __init__(self, value):
        self.value = value

    def __add__(self, add): #足し算(addition)
        return self.value + add.value

    def __sub__(self, sub): #引き算(subtraction)
        return self.value - sub.value

    def __mul__(self, mul): #掛け算(multiplication)
        return self.value * mul.value

    def __truediv__(self, tr_div): #割り算(division)
        return self.value / tr_div.value

    def __floordiv__(self, fl_div): #割り算(division) ※小数点以下切り捨て
        return self.value // fl_div.value

x = FourArithmetic(100.5)
y = FourArithmetic(20)

print(x + y) # -> 120.5
print(x - y) # -> 80.5
print(x * y) # -> 2010.0
print(x / y) # -> 5.025
print(x // y)# -> 5.0

class Calculation:
    '''「+=」「-=」「*=」「/=」'''
    def __init__(self, value):
        self.value = value

    def __iadd__(self, add):
        self.value += add
        return self.value

    def __isub__(self, sub):
        self.value -= sub
        return self.value

    def __imul__(self, mul):
        self.value *= mul
        return self.value

    def __itruediv__(self, tr_div):
        self.value /= tr_div
        return self.value

a = Calculation(50)
print(type(a)) # -> class '__main__.Calculation'
#↑最初の時点で、変数aにはCalculation型が格納されている

a += 5
print(type(a)) # -> class 'int'
#↑この時点で、Calculation型が格納されていた変数aに、int型が格納されている
print(a) # -> 55
a -= 5
print(a) # -> 50
a *= 10
print(a) # -> 500
a /= 5
print(a) # -> 100.0

class Compares:
    '''比較演算子'''
    def __init__(self, value):
        self.value = value

    #「__eq__」条件分岐などで、「==」(Equal)を利用した時に呼び出される(return bool)
    def __eq__(self, sample) -> bool:
        return self.value == sample

    #「__ne__」条件分岐などで、「!=」(Not Equal)を利用した時に呼び出される(return bool)
    def __ne__(self, no_eq) -> bool:
        return self.value != no_eq

x = Compares(100)
y = Compares('100')
z = Compares(100)

print(x == y) # -> False
print(x == z) # -> True

class StringConvert:
    '''「__str__」定義されたクラス内の入力を文字列型に変換する(return str)'''
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"My name is {self.name}, and I'm {self.age} years old."

x = StringConvert("mike", 18)
print(x) # -> My name is mike, and I'm 18 years old.
#↑pythonでは、文字列の中にintが入っているとエラーが発生するため、数値型もintに変換する必要がある

class IntConvert:
    '''「__int__」定義されたクラス内の入力を数値型に変換する(return int)'''
    def __init__(self, age):
        self.age = age

    def __int__(self) -> int:
        return int(self.age)

y = IntConvert("100")
print(int(y) + 5) # -> 105
