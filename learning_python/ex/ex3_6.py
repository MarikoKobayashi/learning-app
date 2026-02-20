a = int(input("1つ目の整数を入力する:"))
b = int(input("2つ目の整数を入力する:"))
c = int(input("3つ目の整数を入力する:"))

max_value = a
if b > max_value:
    max_value = b
if c > max_value:
    max_value = c
print(max_value)

#問3.6. input関数で3つの整数を入力し
#最も大きい値のみを表示するプログラムを作成せよ。
#ただし、max関数は使わないこと。
