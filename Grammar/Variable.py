'''「クラス変数」と「インスタンス変数」の違いについて'''

class Hoge:
    '''クラスメソッドとインスタンスメソッドの動きの違い'''
    cl_id = 0

    @classmethod
    def dump_class(cls):
        '''クラスメソッド'''
        print("クラス変数: ", cls.cl_id)

    def construct(self, se_id):
        '''インスタンスメソッド'''
        self.cl_id = se_id

    def dump_instance(self):
        '''インスタンスメソッド'''
        print("インスタンス変数: ", self.cl_id)


Hoge.dump_class()  # -> 0

hoge_instance = Hoge()         # インスタンスを生成
hoge_instance.dump_instance()  # -> 0(この時点ではインスタンス変数を定義していないため、同名のクラス変数が参照される)
hoge_instance.dump_class()     # -> 0

hoge_instance.construct(se_id=10)  # インスタンス化(キーワード引数で指定) ... 位置引数で指定してもOK
hoge_instance.dump_instance()   # -> 10, インスタンス変数の参照が優先
hoge_instance.dump_class()      # -> 0(クラス変数が参照される)

# クラス変数 ... 「クラス定義直下」で宣言した変数(上記例: id = 0)
# インスタンス変数 ... 生成したインスタンスで扱う変数
