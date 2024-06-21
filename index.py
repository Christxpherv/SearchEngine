import os
import json
from whoosh.index import create_in, open_dir
from whoosh.fields import Schema, TEXT, ID

# Define schema
schema = Schema(title=TEXT(stored=True), url=ID(stored=True), content=TEXT)

# Ensure index directory exists and is properly initialized
index_dir = "indexdir"
if not os.path.exists(index_dir):
    os.mkdir(index_dir)

