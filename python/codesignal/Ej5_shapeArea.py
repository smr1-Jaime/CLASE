# Below we will define an n-interesting polygon. Your task is to find the area of a polygon for a given n.
# A 1-interesting polygon is just a square with a side of length 1.
# An n-interesting polygon is obtained by taking the n - 1-interesting polygon and appending 1-interesting polygons to its rim, side by side.
# You can see the 1-, 2-, 3- and 4-interesting polygons in the picture below.

#                                                    ⬜
#                                ⬜               ⬜⬜⬜
#               ⬜            ⬜⬜⬜          ⬜⬜⬜⬜⬜
#   ⬜       ⬜⬜⬜       ⬜⬜⬜⬜⬜     ⬜⬜⬜⬜⬜⬜⬜
#               ⬜            ⬜⬜⬜          ⬜⬜⬜⬜⬜
#                                ⬜               ⬜⬜⬜
#                                                    ⬜

# n=1           n=2              n=3                 n=4

#(1, 1)        (2, 5)          (3, 13)             (4, 25)

def solution(n):
    area = n**2 + (n-1)**2
    return(area)

print(solution(4))