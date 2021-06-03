from flask import Flask, request
from nlp import *
import sys

app = Flask(__name__)

@app.route('/api/match/', methods=['GET'])
def hello_world():
	s_1 = eval(request.args['sentence_1']).strip('][').split(', ')
	s_2 = eval(request.args['sentence_2']).strip('][').split(', ')

	# return s_1.__class__.__name__ + s_2.__class__.__name__ + str(s_1) + str(s_2)

	return str(sentence_similarity(s_1, s_2))

if __name__ == '__main__':
	app.run(host = '0.0.0.0', port = 80, debug = True)