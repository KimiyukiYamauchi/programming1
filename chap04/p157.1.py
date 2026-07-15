def show_args(*args):
    '''与えられた複数の位置引数をタプルにまとめて受け取りそのタプルを表示して返す'''
    print('Positional arguments:', args)
    return args

print(show_args(1, 2, 3, 'da!'))
