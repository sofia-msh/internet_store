from Internet_Store.server.DB import database as db
from flask import Flask
from Internet_Store.server.api import router as rt
from Internet_Store.server.encryption import encryption as e

if __name__ == '__main__':
    app = Flask(__name__)
    app.config
    db1 = db.DataBase('sonya_db')
    router = rt.Router(app, db1)
    db1.DropTables()
    db1.CreateAllTables()
    router.run()
    router.define_routes()


    db1.shutdown()
