num1 = int(input("1回目の整数を入力してください："))
num2 = int(input("2回目の整数を入力してください："))
num3 = int(input("3回目の整数を入力してください："))
numbers = [num1,num2,num3]
print(f"最大値：{max(numbers)}")
print(f"最小値：{min(numbers)}")
print(f"平均値：{sum(numbers) / len(numbers)}")

#問2.6. input関数を用いて整数を3回入力して
#それらを要素としたリストを作成し
#そのリストの要素の最大値と最小値と平均値を
#順番に表示するプログラムを作成せよ。
