#「クラス変数」と「インスタンス変数」の違いについて
#https://qiita.com/yaboxi_/items/70249bd5a977d614aa4c

class Hoge:
    id = 0

    @classmethod
    def dump_class(cls):
        print("クラス変数: ", cls.id)

    def construct(self, id):
        self.id = id

    def dump_instance(self):
        print("インスタンス変数: ", self.id)
        

Hoge.dump_class()  # -> 0

hoge_instance = Hoge()         # インスタンスを生成
hoge_instance.dump_instance()  # -> 0(この時点ではインスタンス変数を定義していないため、同名のクラス変数が参照される)
hoge_instance.dump_class()     # -> 0

hoge_instance.construct(id=10)  # インスタンス化(キーワード引数で指定) ... (10)でもOK
hoge_instance.dump_instance()   # -> 10, インスタンス変数の参照が優先
hoge_instance.dump_class()      # -> 0(クラス変数が参照される)