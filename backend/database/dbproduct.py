""" DATABASE PRODUCT
- In charge of the database CRUD product :
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
from backend.lib.product import Product
from backend.lib.category import Category


class DbProduct():
    def __init__(
        self,
        db_manager=None
    ):
        """ 'db_manager'            (obj ): an instance of DbManager.
            'err'                   (int ): error counter.
            'err_posts'             (list): errors posts.
            'result'                (    ): result of SQLAlchemy request.
            'prod_name_lenght_max'  (int ): max product name caraters """

        self.db_manager = db_manager
        self.current_connection = self.db_manager.db_connection
        self.Session = self.db_manager.Session
        self.new_session = self.db_manager.new_session

        self.err = 0
        self.err_posts = []
        self.result = None

        self.prod_name_lenght_max = 100

    def create(
        self,
        product_name=None,
        product_url=None,
        product_creator=None,
        product_stores=None,
        product_nutriscore=None,
        product_image_url=None,
        product_kcal=None,
        product_kj=None,
        product_category_id=None,
        product_sugar=None,
        product_brands=None
    ):
        """ Add new product to database.
            'product_name           (str): product name.
            'product_url'           (str): (optional) product OFF URL.
            'product_creator'       (str): (optional) product creator name.
            'product_stores'        (str): (optional) product stores.
            'product_nutriscore'    (str): (optional) product nutriscore.
            'product_image_url'     (str): (optional) product image url.
            'product_kcal'          (int): (optional) product Kcal value.
            'product_kj'            (int): (optional) product Kj value.
            'product_category_id'   (int): product category ID.
            'product_sugar'         (int): (optional) product sugar quantity.
            'product_brands'        (str): (optional) product Brand. """

        # err initialisation
        self.err = 0
        self.err_posts = []

        # Empty test
        if product_name is None:
            self.err += 1
            self.err_posts.append("Nom du produit manquant")
        elif product_category_id is None:
            self.err += 1
            self.err_posts.append("Identifiant de la catégorie manquante")

        # Lenght test
        elif len(product_name) > self.prod_name_lenght_max:
            self.err += 1
            self.err_posts.append(
                "Le nom d'utilisateur contient {} caractères contre {} maximum"
                .format(
                    len(product_name), self.prod_name_lenght_max
                )
            )

        # Query
        if self.err == 0:
            newProduct = Product(
                product_name,
                product_url,
                product_creator,
                product_stores,
                product_nutriscore,
                product_image_url,
                product_kcal,
                product_kj,
                product_category_id,
                product_sugar,
                product_brands
            )
            self.new_session.add(newProduct)
            self.new_session.commit()
        else:
            self.err += 1
            self.err_posts.append("Echec de l'ajout en base de donnée")

        return self.err

    def count(self, action=None, param=None):
        """ Count product. """

        if action is None:
            req_result = self.new_session.query(Product).count()
        elif action == "nutriscore":
            req_result = self.new_session.query(Product).\
                filter(
                    Product.productNutriscore == param
                ).count()
        elif action == "*":
            req_result = self.new_session.query(Product).count()

        return req_result

    def read(
        self,
        action=None,
        product_id=None,
        product_name=None,
        product_cat_id=None,
        product_cat_name=None,
        product_nutriscore=None
    ):
        """ 'action'             (str): name of action to execute.
            'product_id'         (int): unique id of product.
            'product_name'       (str): name of product.
            'product_cat_id'     (str): unique id of category.
            'product_cat_name'   (str): name of category.
            'product_nutriscore' (str): a, b, c, d or e """

        self.result = None

        # Product ID
        if action == "id":
            """ SQLAlchemy query to retrieve a product
            whose identifier we know. """

            try:
                product_id = int(product_id)
                req_results = self.new_session.query(Product).\
                    filter(
                        Product.productID == product_id
                    ).all()
            except Exception as e:
                self.err += 1
                self.err_posts.append("{}".format(e))

        # Product Substitutes
        elif action == "substitutes":
            """ SQLAlchemy query to retrieve substitutes products
            whose identifier we know. """

            try:
                product_id = int(product_id)

                pro = self.new_session.query(Product).\
                    filter(
                        Product.productID == product_id
                    ).one()

                req_results = self.new_session.query(Product).\
                    filter(
                        Product.productCategoryID == pro.productCategoryID
                    ).\
                    filter(
                        Product.productNutriscore < pro.productNutriscore
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
                req_results = self.new_session.query(Product).\
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
                req_results = self.new_session.query(Product).\
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

                req_results = self.new_session.query(Product).\
                    filter(
                        Product.productCategoryID == category.categoryID
                    ).all()
            except Exception as e:
                self.err += 1
                self.err_posts.append("{}".format(e))

        elif action == "nutriscore":
            """ SQLAlchemy query to retrieve a product
            whose identifier we know. """

            try:
                product_nutriscore = str(product_nutriscore)
                req_results = self.new_session.query(Product).\
                    filter(
                        Product.productNutriscore == product_nutriscore
                    ).all()

            except Exception as e:
                self.err += 1
                self.err_posts.append("{}".format(e))

        # All products
        elif action == "*":
            """ SQLAlchemy query to retrieve \
            all products. """
            try:
                req_results = self.new_session.query(Product).all()
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

                    product = {}

                    product[
                        "product_id"
                    ] = req_result.productID
                    product[
                        "product_name"
                    ] = req_result.productName
                    product[
                        "product_url"
                    ] = req_result.productUrl
                    product[
                        "product_creator"
                    ] = req_result.productCreator
                    product[
                        "product_store"
                    ] = req_result.productStore
                    product[
                        "product_nutriscore"
                    ] = req_result.productNutriscore
                    product[
                        "product_img_url"
                        ] = req_result.productImgUrl
                    product[
                        "product_kcal"
                        ] = req_result.productKcal
                    product[
                        "product_kj"
                        ] = req_result.productKj
                    product[
                        "product_category_id"
                        ] = req_result.productCategoryID
                    product[
                        "product_sugar"
                        ] = req_result.productSugar
                    product[
                        "product_brand"
                        ] = req_result.productBrand

                    result.append(product)

        return result

    def update(
        self,
        product_id=None,
        product_name=None,
        product_store=None,
        product_nutriscore=None,
        product_img_url=None,
        product_kcal=None,
        product_kj=None,
        product_sugar=None,
        product_brand=None,
    ):
        """ Update user to the database.
            'product_id             (int): product unique id.
            'product_name           (str): product name.
            'product_url'           (str): (optional) product OFF URL.
            'product_creator'       (str): (optional) product creator name.
            'product_stores'        (str): (optional) product stores.
            'product_nutriscore'    (str): (optional) product nutriscore.
            'product_image_url'     (str): (optional) product image url.
            'product_kcal'          (int): (optional) product Kcal value.
            'product_kj'            (int): (optional) product Kj value.
            'product_category_id'   (int): product category ID.
            'product_sugar'         (int): (optional) product sugar quantity.
            'product_brands'        (str): (optional) product Brand. """

        # err initialisation
        self.err = 0
        self.err_posts = []

        # Id test
        if product_id is None:
            self.err += 1
            self.err_posts.append("Identifiant du produit inconnu")
        else:
            update_product = self.new_session.query(Product).\
                filter(Product.productID == product_id).one()

        if product_name is not None:
            update_product.productName = product_name

        if product_store is not None:
            update_product.productStore = product_store

        if product_nutriscore is not None:
            update_product.productNutriscore = product_nutriscore

        if product_img_url is not None:
            update_product.productImgUrl = product_img_url

        if product_kcal is not None:
            update_product.productKcal = product_kcal

        if product_kj is not None:
            update_product.productKj = product_kj

        if product_sugar is not None:
            update_product.productSugar = product_sugar

        if product_brand is not None:
            update_product.productBrand = product_brand

        self.new_session.commit()

    def delete(
        self,
        product_id=None
    ):
        """ Delete product to the database.
            'product_id'   (int): id of product to delete. """

        # err initialisation
        self.err = 0
        self.err_posts = []

        # Id test
        if product_id is None:
            self.err += 1
            self.err_posts.append("Identifiant du produit inconnu")
        else:
            prod_to_del = self.new_session.query(Product).\
                filter(Product.productID == product_id).one()

        # Query
        if self.err == 0:

            self.new_session.delete(prod_to_del)
            self.new_session.commit()

        return self.err
