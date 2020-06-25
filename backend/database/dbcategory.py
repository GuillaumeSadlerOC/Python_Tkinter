""" DATABASE CATEGORY
- In charge of the database CRUD category :
Create - Read - Update - Delete
- Need an instance of Connection.
- The database connection must be active.
- (!) An internet connection must be active. """

# -*- coding: utf-8 -*-
# From Python 3
# From Requests
from requests import get
# From SQLAlchemy
from sqlalchemy import update
from sqlalchemy.orm import sessionmaker
# From Program
from backend.lib.base import Base
from backend.lib.category import Category


class DbCategory():
    def __init__(
        self,
        db_manager=None
    ):
        """ 'db_manager'            (obj ): an instance of DbManager.
            'err'                   (int ): error counter.
            'err_posts'             (list): errors posts.
            'result'                (    ): result of SQLAlchemy request.
            'cat_name_lenght_max'   (int ): lenght max of category name """

        self.db_manager = db_manager
        self.current_connection = self.db_manager.db_connection
        self.Session = self.db_manager.Session
        self.new_session = self.db_manager.new_session

        self.err = 0
        self.err_posts = []
        self.result = None

        self.cat_name_lenght_max = 100

    def create(
        self,
        category_name="",
        category_off_id="",
        category_products=0
    ):
        """ Add a new user to the database.
            'category_name'     (str): name of category.
            'category_off_id'   (str): name of category in OFF.
            'category_products' (int): (optional) number of products. """

        # err initialisation
        self.err = 0
        self.err_posts = []

        # Empty test
        if category_name == "":
            self.err += 1
            self.err_posts.append("Nom de la catégorie manquante")
        elif category_off_id == "":
            self.err += 1
            self.err_posts.append("Identifiant OFF manquant")
        # Lenght test
        elif len(category_name) > self.cat_name_lenght_max:
            self.err += 1
            self.err_posts.append(
                "Le nom d'utilisateur contient {} caractères contre {} maximum"
                .format(
                    len(category_name), self.cat_name_lenght_max
                )
            )

        # Query
        if self.err == 0:
            new_category = Category(
                category_products,
                category_name,
                category_off_id
            )
            self.new_session.add(new_category)
            self.new_session.commit()
        else:
            self.err += 1
            self.err_posts.append("Echec de l'ajout en base de donnée")

        return self.err

    def read(
        self,
        action=None,
        category_id=None,
        category_name=None
    ):
        """ 'action'          (str): name of action to execute.
            'category_id'     (int): unique id of category.
            'category_name'   (str): name of category. """

        self.result = None

        # Category ID
        if action == "id":
            """ SQLAlchemy query to retrieve a category
            whose identifier we know. """

            try:
                category_id = int(category_id)
                req_results = self.new_session.query(Category).\
                    filter(
                        Category.categoryID == category_id
                    ).all()
            except Exception as e:
                self.err += 1
                self.err_posts.append("{}".format(e))

        # Category Name
        elif action == "name":
            """ SQLAlchemy query to retrieve a category
            whose name we know. """

            try:
                category_name = str(category_name)
                req_results = self.new_session.query(Category).\
                    filter(
                        Category.categoryName == category_name
                    ).all()
            except Exception as e:
                self.err += 1
                self.err_posts.append("{}".format(e))

        # Category count
        elif action == "count":
            """ SQLAlchemy query to retrieve \
            the number of categories. """

            try:
                req_results = self.new_session.query(Category).count()
            except Exception as e:
                self.err += 1
                self.err_posts.append("{}".format(e))

        # All categories
        elif action == "*":
            """ SQLAlchemy query to retrieve \
            all categories. """

            try:
                req_results = self.new_session.query(Category).all()
            except Exception as e:
                self.err += 1
                self.err_posts.append("{}".format(e))

        # Error
        else:
            self.err += 1
            self.err_posts.append("Action non reconnue.")

        if self.err == 0:

            result = []

            for req_result in req_results:

                category = {}

                category["category_id"] = req_result.categoryID
                category["category_products"] = req_result.categoryProducts
                category["category_name"] = req_result.categoryName
                category["category_id_off"] = req_result.categoryIDOFF

                result.append(category)

        return result

    def update(
        self,
        category_id=None,
        category_name=None,
        category_products=None
    ):
        """ Update user to the database.
            'category_id'       (int): id of user.
            'category_name'     (str): (optional) name of category.
            'category_products' (int): (optional) number of products. """

        # err initialisation
        self.err = 0
        self.err_posts = []

        # Id test
        if category_id is None:
            self.err += 1
            self.err_posts.append("Identifiant de la catégorie inconnu")
        else:
            cat_to_up = self.new_session.query(Category).\
                filter(Category.categoryID == category_id).one()

        # Query
        if self.err == 0:

            if category_name is not None:
                cat_to_up.categoryName = category_name
            elif category_products is not None:
                cat_to_up.categoryProducts = category_products

            self.new_session.commit()

        return self.err

    def delete(
        self,
        category_id=None
    ):
        """ Delete category to the database.
            'category_id'   (int): id of category to delete. """

        # err initialisation
        self.err = 0
        self.err_posts = []

        # Id test
        if category_id is None:
            self.err += 1
            self.err_posts.append("Identifiant de la catégorie inconnu")
        else:
            cat_to_del = self.new_session.query(Category).\
                filter(Category.categoryID == category_id).one()

        # Query
        if self.err == 0:

            self.new_session.delete(cat_to_del)
            self.new_session.commit()

        return self.err
