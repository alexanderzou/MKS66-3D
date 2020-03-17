from display import *
from draw import *
from parse import *
from matrix import *
import math

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()

parse_file( 'script', edges, transform, screen, color )

screen = new_screen()
color = [ 255, 255, 0 ]
edges = []
transform = new_matrix()

parse_file( 'mypic', edges, transform, screen, color )