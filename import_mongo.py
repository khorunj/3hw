import pymongo
import json
from pymongo import MongoClient, InsertOne

client = pymongo.MongoClient('mongodb+srv://khorunj:25052005@khorunj.vkjiukc.mongodb.net/?retryWrites=true&w=majority&appName=khorunj')
db = client.hw03
collection_authors = db.authors  # коллекция для данных из authors.json
collection_quotes = db.quotes  # коллекция для данных из quotes.json

# Добавление данных из authors.json
requesting_authors = []
with open("authors.json") as f:
    data_authors = json.load(f)
    for item in data_authors:
        requesting_authors.append(InsertOne(item))

result_authors = collection_authors.bulk_write(requesting_authors)

# Добавление данных из quotes.json
requesting_quotes = []
with open("quotes.json") as f:
    data_quotes = json.load(f)
    for item in data_quotes:
        requesting_quotes.append(InsertOne(item))

result_quotes = collection_quotes.bulk_write(requesting_quotes)

client.close()
