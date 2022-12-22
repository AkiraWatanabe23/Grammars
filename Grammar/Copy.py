#「copy」「deepcopy」の違いについて記述
import copy

a = [1, 2, [3, 4]]
b = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

print(type(a)) # -> <class 'list'>
print(type(b)) # -> <class 'list'>

"""
浅いコピー ... 多次元リスト等の「深い要素」が存在し、その「深い要素」を変更する場合にコピー先と連動するもの
深いコピー
"""

