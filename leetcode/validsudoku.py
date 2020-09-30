ip = [
  ["8","3",".",".","7",".",".",".","3"],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
# checking columns and rows 
for i in range(9):
  d_col = {} 
  d_row = {}
  for j in range(9):
    x = ip[j][i]
    y = ip[i][j]
    if x in d_col and x != ".":
      print(f"False x = {x} and {j},{i}") 
    else: 
      d_col[x] = 1 
      # print(f"true x = {x} and {j},{i}") 
    if y in d_row and y != ".":
      print(f"False y= {y} and {i},{j}") 
    else:
      d_row[y] = 1  

# checking rows
# for i in range(9):
#   d = {}
#   for j in range(9):
#     x = ip[i][j] 
#     if x in d and x != ".":
#       print(f"False x = {x} and {i},{j}") 
#     else:
#       d[x] = 1   
#       print(f"True x = {x} and {i},{j}") 
# checking 3*3 squares 
      
for i in range(0,9,3):
  for j in range(0,9,3):
      row = [j for j in ip[i][j:j+3] + ip[i+1][j:j+3] + ip[i+2][j:j+3] if j != '.']
      if len(row) != len(set(row)):
         print("Flase grid") 
x = [j for j in range(5) if j != 4]  
print(x)       

  