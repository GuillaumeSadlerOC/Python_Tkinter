""" DATABASE USER PRODUCTS
- In charge of the database CRUD user product :
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
# From Program
from backend.lib.userproduct import UserProduct
from backend.lib.product import Product


class DbUserProduct():
    def __init__(
        self,
        db_manager=None
    ):
        """ 'db_manager'            (obj ): an instance of DbManager.
            'err'                   (int ): error counter.
            'err_posts'             (list): errors posts.
            'result'                (    ): result of SQLAlchemy request. """

        self.db_manager = db_manager
        self.current_connection = self.db_manager.db_connection
        self.Session = self.db_manager.Session
        self.new_session = self.db_manager.new_session

        self.err = 0
        self.err_posts = []
        self.result = None

    def create(
        self,
        user_id=None,
        product_id=None
    ):
        """ Add a new user to the database.
            'user_id'      (int): unique id of user.
            'product_id'   (int): unique id of product. """

        # err initialisation
        self.err = 0
        self.err_posts = []

        # Empty test
        if user_id is None:
            self.err += 1
            self.err_posts.append("Identifiant de l'utilisateur manquant")
        elif product_id is None:
            self.err += 1
            self.err_posts.append("Identifiant du produit manquant")

        # Query
        if self.err == 0:

            test = self.new_session.query(UserProduct).\
                filter(
                    UserProduct.userProductProductID == int(product_id)
                ).\
                filter(
                    UserProduct.userProductUserID == int(user_id)
                ).all()

            if len(test) == 0:
                new_user_product = UserProduct(
                    user_id=int(user_id),
                    product_id=int(product_id)
                )
                self.new_session.add(new_user_product)
                self.new_session.commit()

        return self.err

    def read(
        self,
        action=None,
        user_id=None,
        product_id=None
    ):
        """ 'user_id'   (int): unique id of user. """

        # err initialisation
        self.err = 0
        self.err_posts = []
        result = []

        # User id
        if user_id is None:
            self.err += 1
            self.err_posts.append("Identifiant de l'utilisateur inconnu")
        # Query
        elif self.err == 0:

            if action == "test":

                try:
                    req_results = self.new_session.query(UserProduct).filter(
                        UserProduct.userProductProductID == int(product_id)
                    ).filter(
                        UserProduct.userProductUserID == int(user_id)
                    ).all()

                    result = []

                    for req_result in req_results:

                        favorite = {}

                        favorite["product_id"] = req_result.userProductProductID

                        result.append(favorite)

                except Exception as e:
                    self.err += 1
                    self.err_posts.append("{}".format(e))

            else:
                try:

                    user_products = self.new_session.query(UserProduct).filter(
                        UserProduct.userProductUserID == int(user_id)
                    ).all()

                    req_results = []

                    for user_prod in user_products:

                        results = self.new_session.query(Product).\
                            filter(
                                Product.productID ==
                                user_prod.userProductProductID
                            ).one()
                        req_results.append(results)

                    for req_result in req_results:

                        favorite = {}

                        favorite["product_id"] = req_result.productID
                        favorite["product_name"] = req_result.productName
                        favorite["product_img_url"] = req_result.productImgUrl

                        result.append(favorite)

                except Exception as e:
                    self.err += 1
                    self.err_posts.append("{}".format(e))
                    print(e)

        return result

    def update(
        self
    ):
        """ Update user product """

        # err initialisation
        self.err = 0
        self.err_posts = []

    def delete(
        self,
        user_id=None,
        product_id=None
    ):
        """ Delete user to the database.
            'user_id'       (int): id of user to delete userproduct.
            'product_id'    (int): id of user product to delete. """

        # err initialisation
        self.err = 0
        self.err_posts = []

        # User id
        if user_id is None:
            self.err += 1
            self.err_posts.append("Identifiant de l'utilisateur inconnu")
        # delete user product
        else:

            user_product = self.new_session.query(UserProduct).\
                filter(
                    UserProduct.userProductUserID == user_id,
                    UserProduct.userProductProductID == product_id,
                ).one()

            self.new_session.delete(user_product)
            self.new_session.commit()

        return self.err
