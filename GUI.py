from flask import Flask, request, render_template
from whoosh.qparser import QueryParser
from whoosh.index import open_dir

app = Flask(__name__)
ix = open_dir("indexdir")