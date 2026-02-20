def get_square_area(base, height):
    return base * height
base = int(input("底辺を入力"))
height = int(input("高さを入力"))
area = get_square_area(base,height)
print(F"面積は{area}")