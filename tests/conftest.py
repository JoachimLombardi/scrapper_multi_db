import pytest
from pymongo import MongoClient
from flask_.app import app

# pytest conftest.py


@pytest.fixture()  # fixture utilisée pour faire les tests
def app2():
    app.config.update({
        "TESTING": True,
    })
    yield app


@pytest.fixture()
def client(app2):
    return app2.test_client()


@pytest.fixture()
def runner(app2):
    return app2.test_cli_runner()


def test_api(client):  # Chaque test commence par la fonction test_
    response = client.get("/random")
    assert response.status_code == 200


def test_query(client):
    response = client.get("/search?query=love")
    assert response.status_code == 200


def test_insert(mongo_collection):
    try:
        mongo_collection.insert_one({"quote": "test", "author": "test"})
    except Exception:
        pytest.fail("Could not insert into MongoDB")


def test_verify_quotes(mongo_collection):
    for quote in mongo_collection.find({}):
        assert "quote" in quote
        assert "author" in quote


def test_verify_count(mongo_collection):
    count = mongo_collection.count_documents({})
    assert count >= 0


# testing the mongodb connection
@pytest.fixture()
def mongo_connection():
    try:
        client = MongoClient()
        return client
    except Exception:
        pytest.fail("Could not yield DB client")


@pytest.fixture()
def mongo_collection(mongo_connection):
    return mongo_connection.scrapy_db.quotes


def test_mongo_db(mongo_connection):
    try:
        mongo_connection.scrapy_db
    except Exception:
        pytest.fail("Could not connect to MongoDB")
