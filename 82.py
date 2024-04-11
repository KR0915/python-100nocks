def calculate_pascal_triangle(rows):
    triangle = []
    for i in range(rows):
        row = [1]  # 各行の先頭は常に1
        if i > 0:
            # 左上と右上の値を足して新しい値を計算する
            prev_row = triangle[i - 1]
            for j in range(1, i):
                row.append(prev_row[j - 1] + prev_row[j])
            row.append(1)  # 各行の末尾も常に1
        triangle.append(row)
    return triangle

def display_triangle(triangle):
    for row in triangle:
        # 数字を左詰めでスペースで区切って表示
        print(" ".join(map(str, row)).center(50))

# 15段までのパスカルの三角形を計算して表示
pascal_triangle = calculate_pascal_triangle(15)
display_triangle(pascal_triangle)
