from flask import Flask, request, render_template
from whoosh.qparser import QueryParser
from whoosh.index import open_dir

app = Flask(__name__)
ix = open_dir("indexdir")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
    query_str = request.args.get('q')
    with ix.searcher() as searcher:
        query = QueryParser("content", ix.schema).parse(query_str)
        results = searcher.search(query)
        print(f"Query: {query_str}, Results: {len(results)}")
        for result in results:
            print(dict(result))
        return render_template('results.html', results=results)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)