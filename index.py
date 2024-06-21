import os
import json
from whoosh.index import create_in, open_dir
from whoosh.fields import Schema, TEXT, ID

# Define schema
schema = Schema(title=TEXT(stored=True), url=ID(stored=True), content=TEXT)