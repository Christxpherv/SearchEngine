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

# Create or open the index
if not os.path.exists(os.path.join(index_dir, "MAIN_WRITELOCK")):  # Check if index is empty
    ix = create_in(index_dir, schema)
else:
    ix = open_dir(index_dir)

def add_document(title, url, content):
    writer = ix.writer()
    writer.add_document(title=title, url=url, content=content)
    writer.commit()
    print(f"Indexed document: title={title}, url={url}, content length={len(content)}")