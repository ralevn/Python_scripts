x1, y1, x2, y2 = float(input()), float(input()), float(input()), float(input())

area = (max(x1, x2) - min(x1, x2)) * (max(y1,y2) - min(y1,y2))
perimeter = (max(x1, x2) - min(x1, x2)) * 2 + (max(y1,y2) - min(y1,y2)) * 2

print (f"%.2f \n %.2f" %(area, perimeter))