#1///
import math
n = 15
def d_to_r(n):
    print(n * (math.pi / 180))
d_to_r(n)
#2///
import math
def  area_of():
    h = 5
    a = 5
    b = 6
    print(((a + b) * h) / 2)
area_of()
#3///
from math import tan, pi
def area_of_reg():
    n_sides = 4
    s_lenght = 25
    P_area = n_sides * (s_lenght**2) / (4 * tan(pi / n_sides))
    print("The area of the pollygon is ", P_area)
area_of_reg()
#4///
import math
def area_of_par():
    s_lenght = 5
    h_height = 6
    S_area = s_lenght * h_height
    print(S_area)
area_of_par()
    