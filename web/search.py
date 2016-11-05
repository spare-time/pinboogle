from flask import Flask
from flask import request, render_template
app = Flask(__name__)

@app.route('/', methods=['GET'])
def search():
    query = request.args.get('q', None)
    return render_template('search.html', query=query)

@app.errorhandler(404)
def not_found(error):
    return 'Not found', 404
