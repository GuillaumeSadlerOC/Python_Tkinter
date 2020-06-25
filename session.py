""" SESSION
between frontend and backend. """

# -*- coding: utf-8 -*-
# From Python 3
import json
# From Program
from backend.database.dbmanager import DbManager
from frontend.window import Window
from frontend.displayer import Displayer


class Session():
    def __init__(self):
        """ 'displayer'     (obj): instance of Displayer.
            'user_id'       (int): User id who use program. """

        # Instances
        self.displayer = None
        self.user_id = None
        self.gui_language = "en"

        self.dbmanager = DbManager()
        self.window = Window()
        self.displayer = Displayer(
            window=self.window,
            session=self
        )

        self.start_session()
        self.window.mainloop()

    def start_session(self):
        """ Start the new session. """

        if self.dbmanager.err == 0:
            self.displayer.display(
                f_view="user_welcome"
            )
        elif self.dbmanager.err >= 1:
            self.displayer.display(
                f_view="update_server_conn"
            )

    def get_script(
        self,
        file_name=None,
        package_name=None
    ):
        """ get the .json scripts.
            'language'  (str): 'fr' or 'en'.
            'view_name' (str): file name whitout '.py'. """

        if package_name is None:
            with open(
                "frontend/languages/{}/{}.json"
                .format(self.gui_language, file_name)
            ) as json_data:

                json_dict = json.load(json_data)
        else:
            with open(
                "frontend/languages/{}/{}/{}.json"
                .format(self.gui_language, package_name, file_name)
            ) as json_data:

                json_dict = json.load(json_data)

        return json_dict

    def off_requests(
        self,
        req_type=None,
        **kwargs
    ):
        """ Open Food Facts requests. """

        result = None

        for key, value in kwargs.items():

            if key == "language":
                language = value

        if self.dbmanager.err >= 1:
            self.dbmanager.start()

        if req_type == "categories":

            self.dbmanager.offmanager.get_categories(
                language=language
            )

            result = self.dbmanager.offmanager.categories

        return result

    def upload(
        self,
        language=None,
        categories=None
    ):
        """
        """

        count = 0
        for cat in categories:

            products = self.dbmanager.offmanager.get_products(
                    language=language, category=cat
                )

            self.dbmanager.db_category.create(
                category_name=cat,
                category_off_id=cat,
                category_products=0
            )

            for product in products:

                self.dbmanager.db_product.create(
                    product_name=product.get("product_name"),
                    product_url=product.get("product_url"),
                    product_creator=product.get("product_creator"),
                    product_stores=product.get("product_stores"),
                    product_nutriscore=product.get("product_nutriscore"),
                    product_image_url=product.get("product_image_url"),
                    product_kcal=product.get("product_kcal"),
                    product_kj=product.get("product_kj"),
                    product_category_id=count,
                    product_sugar=product.get("product_sugar"),
                    product_brands=product.get("product_brands")
                )

            count += 1
