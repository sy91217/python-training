# 在 geometry 模組中定義幾何運算功能
# 計算兩個點的距離
def distance(x1,y1,x2,y2): # x1,y1 是第一個點, x2,y2 是第二個點
    return ((x2-x1)**2+(y2-y1)**2)**0.5
# 計算線段的斜率
def slope(x1,y1,x2,y2):
    return (y2-y1)/(x2-x1)