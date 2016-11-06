from flask import Flask
from flask import request, render_template, g
from SolrClient import SolrClient
import math
app = Flask(__name__)

SOLR_HOST = 'solr'
SOLR_PORT = 8983
SOLR_CORE = 'pinboard'
DEFAULT_RESULTS_PER_PAGE = 30

def get_solr_client():
    if not hasattr(g, 'solr_client'):
        g.solr_client = SolrClient('http://%s:%s/solr' % (SOLR_HOST, SOLR_PORT))
    return g.solr_client

@app.route('/', methods=['GET'])
def search():
    query   = request.args.get('q', None)
    results = []
    meta    = {}

    if query:
        page  = request.args.get('p', 1)
        try:
            page = int(page)
        except ValueError:
            page = 1
        start = (page - 1) * DEFAULT_RESULTS_PER_PAGE
        if start < 0:
            start = 0

        solr = get_solr_client()
        response = solr.query(SOLR_CORE, {'q': query, 'start': start, 'rows': DEFAULT_RESULTS_PER_PAGE})
        results = response.docs

        meta['current_page']  = 1 + math.floor(start/DEFAULT_RESULTS_PER_PAGE) 
        meta['total_pages']   = 1 + math.floor(response.get_num_found()/DEFAULT_RESULTS_PER_PAGE)
        meta['total_results'] = response.get_num_found()

    return render_template('search.html', query=query, results=results, meta=meta)

@app.errorhandler(404)
def not_found(error):
    return 'Not found', 404

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
