# from .. import index_intersection
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', ''))
from index_intersection import *

 
print(index_intersection([[1,5,3,2],[2,3,4,6,9],[3,1,4,2,5,6]]))