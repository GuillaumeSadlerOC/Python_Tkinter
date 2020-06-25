""" SEARCH ENGINE
Need an instance of Connection.
The database connection must be active.
(!) An internet connection must be active. """

# -*- coding: utf-8 -*-
# From Python 3
# From SQLAlchemy
from sqlalchemy.orm import sessionmaker
# From Program
from backend.lib.base import Base
from backend.lib.category import Category
from backend.lib.product import Product
from backend.lib.user import User
from backend.lib.userproduct import UserProduct


class Search():
    def __init__(self, current_connection=None):
        """ 'current_connection' (obj ): an instance of Connection.
            'result'             (list): contains the result of methods.
            'err'                (int ): error counter.
            'err_posts'          (list): errors posts."""

        self.current_connection = current_connection
        self.err = 0
        self.err_posts = []
        self.result = []

        if self.current_connection.server_conn == 0:
            self.err += 1
            self.err_posts.append("Pas de connexion avec le serveur")
        elif self.current_connection.server_conn == 1:
            self.err += 1
            self.err_posts.append("Base de données non connecté")
        elif self.current_connection.server_conn == 2:
            # 1 : Create Base
            self.Base = Base
            # 2 : Create Session
            self.Session = sessionmaker(bind=current_connection.engine)
            # 3 : Create
            self.Base.metadata.create_all(current_connection.engine)
            # 4 : Create new session
            self.new_session = self.Session()
            # 5 : err initialisation
            self.err = 0
            self.err_posts = []

    def get_search(self, search=None, option=None):
        """ Examples :
        get_search(search="user", option=("id", 1))
        get_search(search="user", option=("name", "guillaume"))
        get_search(search="user", option=("", "*"))

        get_search(search="category", option=("id", 72))
        get_search(search="category", option=("name", "Jambon"))
        get_search(search="category", option=("info", "count"))
        get_search(search="category", option=("", "*"))

        get_search(search="product", option=("id", 50))
        get_search(search="product", option=("name", "Nutella"))
        get_search(search="product", option=("catId", 60))
        get_search(search="product", option=("catName", "Pate à tartiner"))
        get_search(search="product", option=("*", ""))

        get_search(search="substituts", option=("id", 1))

        get_search(search="favorites", option=("id", 1)) """

        # err + result initialisation
        self.err = 0
        self.err_posts = []
        self.result = []

        if search is None:
            self.err += 1
            self.err_posts.append("Type de la recherche manquante")
        else:
            # USER
            if search == "user":
                if option[0] == "id":
                    req_result = self.get_users(
                        action="id",
                        user_id=option[1]
                    )
                elif option[0] == "name":
                    req_result = self.get_users(
                        action="name",
                        user_name=option[1]
                    )
                elif option[0] == "info":
                    req_result = self.get_users(
                        action=option[1]
                    )
                elif option[0] == "*":
                    req_result = self.get_users(
                        action=option[1]
                    )
            # CATEGORY
            elif search == "category":
                if option[0] == "id":
                    req_result = self.get_categories(
                        action="id",
                        category_id=option[1]
                    )
                elif option[0] == "name":
                    req_result = self.get_categories(
                        action="name",
                        category_name=option[1]
                    )
                elif option[0] == "info":
                    req_result = self.get_categories(
                        action=option[1]
                    )
                elif option[0] == "*":
                    req_result = self.get_categories(
                        action=option[1]
                    )
            # PRODUCT
            elif search == "product":
                if option[0] == "id":
                    req_result = self.get_products(
                        action="id",
                        product_id=option[1]
                    )
                elif option[0] == "name":
                    req_result = self.get_products(
                        action="name",
                        product_name=option[1]
                    )
                elif option[0] == "catId":
                    req_result = self.get_products(
                        action="cat_id",
                        product_name=option[1]
                    )
                elif option[0] == "catName":
                    req_result = self.get_products(
                        action="cat_name",
                        product_name=option[1]
                    )
                elif option[0] == "info":
                    req_result = self.get_products(
                        action=option[1]
                    )
                elif option[0] == "*":
                    req_result = self.get_products(
                        action=option[1]
                    )
            # SUBSTITUTES
            elif search == "substituts":

                if option[0] == "id":
                    req_result = self.get_substituts(
                        action="id",
                        product_id=option[1]
                    )
            # FAVORITES
            elif search == "favorites":

                if option[0] == "id":
                    req_result = self.get_favorites(
                        action="id",
                        user_id=option[1]
                    )

    def get_users(
        self,
        action=None,
        user_id=None,
        user_name=None
    ):
        """ 'action'            (str): name of action to execute.
            'user_id'           (int): unique id of user.
            'user_name'         (str): name of user.
            'req_result'        ()   : result of SQLAlchemy request. """

        req_result = None

        # User id
        if action == "id":
            """ SQLAlchemy query to retrieve a user
            whose identifier we know. """

            try:
                user_id = int(user_id)
                req_result = self.new_session.query(User).\
                    filter(
                        User.userID == user_id
                    ).all()
            except Exception as e:
                self.err += 1
                self.err_posts.append("{}".format(e))

        # User name
        elif action == "name":
            """ SQLAlchemy query to retrieve an user
            whose name we know. """

            try:
                user_name = str(user_name)
                req_result = self.new_session.query(User).\
                    filter(
                        User.userName == user_name
                    ).all()
            except Exception as e:
                self.err += 1
                self.err_posts.append("{}".format(e))

        # All users
        elif action == "*":
            """ SQLAlchemy query to retrieve \
            all users. """

            try:
                req_result = self.new_session.query(User).all()
            except Exception as e:
                self.err += 1
                self.err_posts.append("{}".format(e))

        # Error
        else:
            self.err += 1
            self.err_posts.append("Action non reconnue.")

        return req_result

    def get_categories(
        self,
        action=None,
        category_id=None,
        category_name=None
    ):
        """ 'action'          (str): name of action to execute.
            'category_id'     (int): unique id of category.
            'category_name'   (str): name of category.
            'req_result'      ()   : result of SQLAlchemy request. """

        req_result = None

        # Category ID
        if action == "id":
            """ SQLAlchemy query to retrieve a category
            whose identifier we know. """

            try:
                category_id = int(category_id)
                req_result = self.new_session.query(Category).\
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
                req_result = self.new_session.query(Category).\
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
                req_result = self.new_session.query(Category).count()
            except Exception as e:
                self.err += 1
                self.err_posts.append("{}".format(e))

        # All categories
        elif action == "*":
            """ SQLAlchemy query to retrieve \
            all categories. """

            try:
                req_result = self.new_session.query(Category).all()
            except Exception as e:
                self.err += 1
                self.err_posts.append("{}".format(e))

        # Error
        else:
            self.err += 1
            self.err_posts.append("Action non reconnue.")

        return req_result

    def get_products(
        self,
        action=None,
        product_id=None,
        product_name=None,
        product_cat_id=None,
        product_cat_name=None
    ):
        """ 'action'             (str): name of action to execute.
            'product_id'         (int): unique id of product.
            'product_name'       (str): name of product.
            'product_cat_id'     (str): unique id of category.
            'product_cat_name'   (str): name of category.
            'req_result'         ()   : result of SQLAlchemy request. """

        req_result = None

        # Product ID
        if action == "id":
            """ SQLAlchemy query to retrieve a product
            whose identifier we know. """

            try:
                product_id = int(product_id)
                req_result = self.new_session.query(Product).\
                    filter(
                        Product.productID == product_id
                    ).all()
            except Exception as e:
                self.err += 1
                self.err_posts.append("{}".format(e))

        # Product Name
        elif action == "name":
            """ SQLAlchemy query to retrieve a product
            whose name we know. """

            try:
                product_name = str(product_name)
                req_result = self.new_session.query(Product).\
                    filter(
                        Product.productName == product_name
                    ).all()
            except Exception as e:
                self.err += 1
                self.err_posts.append("{}".format(e))

        # Product category id
        elif action == "cat_id":
            """ SQLAlchemy query to retrieve \
            all products of an category whose id we know. """

            try:
                product_cat_id = int(product_cat_id)
                req_result = self.new_session.query(Product).\
                    filter(
                        Product.productCategoryID == product_cat_id
                    ).all()
            except Exception as e:
                self.err += 1
                self.err_posts.append("{}".format(e))

        # Product category name
        elif action == "cat_name":
            """ SQLAlchemy query to retrieve \
            all products of an category whose name we know. """

            try:
                product_cat_name = str(product_cat_name)

                category = self.new_session.query(Category).\
                    filter(
                        Category.categoryName == product_cat_name
                    ).all()

                req_result = self.new_session.query(Product).\
                    filter(
                        Product.productCategoryID == category.categoryID
                    ).all()
            except Exception as e:
                self.err += 1
                self.err_posts.append("{}".format(e))

        # All products
        elif action == "*":
            """ SQLAlchemy query to retrieve \
            all products. """
            try:
                req_result = self.new_session.query(Product).all()
            except Exception as e:
                self.err += 1
                self.err_posts.append("{}".format(e))

        # Error
        else:
            self.err += 1
            self.err_posts.append("Action non reconnue.")

        return req_result

    def get_substituts(
        self,
        action=None,
        product_id=None
    ):
        """ 'action'        (str): name of action to execute.
            'product_id'    (int): unique id of product.
            'req_result'    ()   : result of SQLAlchemy request. """

        req_result = None

        # Product to compare id
        if action == "id":
            """ SQLAlchemy query to retrieve products substitutes\
            whose identifier of product to compare we know. """

            try:
                product_id = int(product_id)

                pro = self.new_session.query(Product).\
                    filter(
                        Product.productID == product_id
                    ).one()

                req_result = self.new_session.query(Product).\
                    filter(
                        Product.productCategoryID == pro.productCategoryID
                    ).\
                    filter(
                        Product.productNutriscore < pro.productNutriscore
                    ).all()
            except Exception as e:
                self.err += 1
                self.err_posts.append("{}".format(e))

        # Error
        else:
            self.err += 1
            self.err_posts.append("Action non reconnue.")

        return req_result

    def get_favorites(
        self,
        action=None,
        user_id=None
    ):
        """ 'action'        (str): name of action to execute.
            'user_id'       (int): unique id of user.
            'req_result'    ()   : result of SQLAlchemy request. """

        req_result = None

        # User id
        if action == "id":
            """ SQLAlchemy query to retrieve user products\
            whose identifier of user we know. """

            try:
                user_id = int(user_id)

                user = self.new_session.query(UserProduct).\
                    filter(
                        UserProduct.userProductUserID == user_id
                    ).all()

                result = []

                count = 0
                while count != len(user):
                    product = self.new_session.query(Product).\
                        filter(
                            Product.productID ==
                            user[count].userProductProductID
                        ).one()
                    result.append(product)
                    count += 1

            except Exception as e:
                self.err += 1
                self.err_posts.append("{}".format(e))

        # Error
        else:
            self.err += 1
            self.err_posts.append("Action non reconnue.")

        return req_result
