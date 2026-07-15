# グローバル変数を定義します
animal = 'cat'
# グローバル変数をプリントします
print("animal:", animal)

def my_func():
    # ローカル変数を定義します
    vegetable = 'carrot'
    # 関数の中でグローバル変数の値をプリントします
    print("animal in my_func:", animal)
    # ローカル変数の値をプリントします。
    print("vegetable in_the_func:", vegetable)

my_func()

print("vegetable:", vegetable)
