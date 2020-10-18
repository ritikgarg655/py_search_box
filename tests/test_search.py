from test_data import *
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', ''))
from search import *

add_dic(data)

while 1:
	query_q = input("Enter query")
	lis = query(query_q)
	for i in lis:
		print(data[i])
