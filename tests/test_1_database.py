# tests/test_1_database.py

from app.database import db

def test_db_tables(client, global_data):
    # rv = client.get('/')
    # rv = client.post("/api/v1/signup", json={
    #     'username': 'testuser', 'password': '', 'email': 'test_user@mail.com'
    # })
    assert len(db.metadata.sorted_tables) == 1
    tables = ["examples"]
    assert all(table in [t.name for t in db.metadata.sorted_tables] for table in tables)
