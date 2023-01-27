'''「グローバル変数」と「ローカル変数」'''

#グローバル変数 ... 関数の外で定義した変数
GLB_NUM = 10

class Test():
    '''変数テスト'''

    def out_put(self):
        '''グローバル変数'''
        global GLB_NUM

        GLB_NUM += 5

instance = Test()
print(GLB_NUM)
instance.out_put()
print(GLB_NUM)


def get(get_num):
    '''ローカル変数'''
    #ローカル変数 ... 関数内で定義した変数
    num = 5
    return num + get_num

print(get(10))
