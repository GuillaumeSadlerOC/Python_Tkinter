""" DATABASE MANAGER
- In charge of the database management.
- Need an instance of Connection.
- The database connection must be active.
- (!) An internet connection must be active. """

# -*- coding: utf-8 -*-
# From Python 3
import json
# From Requests
from requests import get
# From SQLAlchemy
from sqlalchemy import update
from sqlalchemy.orm import sessionmaker
# From Program
from backend.database.dbconnection import DbConnection
from backend.database.dbcategory import DbCategory
from backend.database.dbproduct import DbProduct
from backend.database.dbuser import DbUser
from backend.database.dbuserprod import DbUserProduct

from backend.offmanager import OffManager

from backend.lib.base import Base
from backend.lib.category import Category
from backend.lib.product import Product
from backend.lib.user import User
from backend.lib.userproduct import UserProduct


class DbManager():
    def __init__(
        self
    ):
        """ 'err'       (int ): error counter.
            'err_posts' (list): errors posts. """

        self.err = 0
        self.err_posts = []
        self.db_category = None
        self.db_connection = None
        self.db_product = None
        self.db_user = None
        self.db_user_prod = None
        self.offmanager = None

        self.db_connection = DbConnection()

        self.start()

    def start(self):
        """ Start the db manager """

        self.db_connection.connection()

        if self.db_connection.server_conn == 0:
            self.err += 1
            self.err_posts.append("Pas de connexion avec le serveur")
        elif self.db_connection.server_conn == 1:
            self.err_posts.append("Base de données non connecté")
        elif self.db_connection.server_conn == 2:
            # 1 : Create Base
            self.Base = Base
            # 2 : Create Session
            self.Session = sessionmaker(bind=self.db_connection.engine)
            # 3 : Create
            self.Base.metadata.create_all(self.db_connection.engine)
            # 4 : Create new session
            self.new_session = self.Session()
            # 5 : Create db elements
            self.db_category = DbCategory(
                db_manager=self
            )
            self.db_product = DbProduct(
                db_manager=self
            )
            self.db_user = DbUser(
                db_manager=self
            )
            self.db_user_prod = DbUserProduct(
                db_manager=self
            )
            self.offmanager = OffManager()
            # 6 : err initialisation
            self.err = 0
            self.err_posts = []
        else:
            self.err = 1

    def remove(self):
        """ Remove the program.
        (!) This action is irremediable. """

        try:

            products = self.new_session.query(Product).all()
            if len(products) > 0:
                for product in products:
                    self.new_session.delete(product)
                    self.new_session.commit()

            categories = self.new_session.query(Category).all()
            if len(categories) > 0:
                for category in categories:
                    self.new_session.delete(category)
                    self.new_session.commit()

            users = self.new_session.query(User).all()
            if len(users) > 0:
                for user in users:
                    self.new_session.delete(user)
                    self.new_session.commit()

            user_products = self.new_session.query(UserProduct).all()
            if len(user_products) > 0:
                for user_product in user_products:
                    self.new_session.delete(user_product)
                    self.new_session.commit()

            # Write in JSON File
            write_json = {}
            write_json["server_logs"] = {}
            write_json["server_logs"]["server_user"] = None
            write_json["server_logs"]["server_pass"] = None
            write_json["server_logs"]["server_host"] = None

            write_json["server_status"] = {}
            write_json["server_status"]["server_conn"] = None
            write_json["server_status"]["server_db_name"] = None

            with open(
                "backend/serverconfigs.json", "w", encoding="utf-8"
            ) as json_file:

                json.dump(write_json, json_file, indent=4)

        except Exception as e:
            print(e)
