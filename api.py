from flask import Flask,jsonify,request

app = Flask(__name__)

@app.route("/",methods = ['GET', 'POST'])
def hello():
	if(request.method  == 'POST'):
		input_json = request.get_json()
		print(type(input_json['filter']))
		return jsonify(input_json)

if __name__ == '__main__':
	app.run(debug=True)