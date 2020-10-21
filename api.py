from flask import Flask,jsonify,request
from search import *
app = Flask(__name__)

@app.route("/add",methods = ['POST'])
def ins():
	if(request.method  == 'POST'):
		input_json = request.get_json()

		try:
			data = input_json['data']
		except:
			print('data is not present in input json')
			return jsonify("Invalid input"),404

		try:
			filters = input_json['filter']
		except:
			# defaut filters
			filters = {
		        "lower":True,
		        "synonyms":False,
		        "split":True,
				"stopword":True
		    }
		add_dic(data,filters)
		return jsonify(input_json)

@app.route("/query",methods = ['POST'])
def que():
	if request.methods == 'POST':
		input_json = request.get_json()
		try:
			query_str = input_json['query']
		except:
			return jsonify([''])
		return jsonify(query(query_str))

if __name__ == '__main__':
	app.run(debug=False)
