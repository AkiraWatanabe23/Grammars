#「copy」「deepcopy」の違いについて記述
import copy

a = [1, 2, [3, 4]]
print(type(a)) # -> <class 'list'>

b = copy(a)
c = copy.deepcopy(a)