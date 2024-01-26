from pymongo import MongoClient
from flask import Flask, request
import json
import logging
from waitress import serve

# flask --app app.py run

app = Flask(__name__)

logging.basicConfig(filename='app.log', level=logging.INFO)


# Rechercher par index
@app.route("/search", methods=["GET"])
def search():
    try:
        collection_name = "quotes"
        client = MongoClient("mongodb://localhost:27017/")
        db = client.scrapy_db
        collection = db[collection_name]
        # On test si l'index existe, sinon on le crée
        if not db["quotes"].create_index(
         [("quote", "text"), ("author", "text")]):
            # Indexer la collection
            db[collection_name].create_index(
                [("quote", "text"), ("author", "text")])
        query = request.args.get('query')
        results = collection.find(
            {"$text": {"$search": query}})  # $text exploite l'index texte
        liste = list(results)
        new_liste = []
        for result in liste:
            new_liste.append(
                {"quote": result["quote"], "author": result["author"]})
        return json.dumps(new_liste), 200
    except Exception as e:
        return json.dumps({"error": str(e)})


# Choisir une citation au hasard dans mong db
@app.route("/random", methods=["GET"])
def random():
    try:
        client = MongoClient("mongodb://localhost:27017/")
        db = client.scrapy_db
        quote_number = int(request.args.get('number'))
        results = db.quotes.aggregate(
            [{"$sample":
              {"size": quote_number}}])  # Selectionne une citation au hasard
        # $sample permet de selectionner une citation au hasard
        liste = list(results)
        new_liste = []
        for result in liste:
            new_liste.append(
                {"quote": result["quote"], "author": result["author"]})
        return json.dumps(new_liste), 200
    except Exception as e:
        return json.dumps({"error": str(e)})


if __name__ == '__main__':
    serve(app, host="0.0.0.0", port=5000)
