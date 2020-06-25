""" OPEN FOOD FACTS MANAGER
In charge of recovering Open Food Facts API data.
The database connection must be active.
(!) An internet connection must be active. """

# -*- coding: utf-8 -*-
# From Python 3
import time
# From Requests
from requests import get
# From SQLAlchemy
# From Program


class OffManager():
    def __init__(self):

        self.products = []
        self.pages = 0
        self.finish = False
        self.counting = False

    def get_categories(
        self,
        language=None
    ):
        """ Ask JSON API Open Food Facts \
        to retrieve product languages.
            'language'  (str): Language of category."""

        self.categories = []

        r = get(
            "https://{}.openfoodfacts.org/categories.json"
            .format(language)
        )
        cat_dict = r.json()

        for cat in cat_dict["tags"]:

            category = {
                "category_off_id": cat["id"],
                "category_name": cat["name"],
                "category_products": cat["products"],
                "language": language
            }

            if cat["products"] >= 10:
                self.categories.append(category)
            else:
                pass

    def get_products(
        self,
        language=None,
        category=None
    ):
        """ Ask JSON API Open Food Facts \
        to retrieve product languages.
            'language'    (str): language of products.
            'off_cat_id'  (str): name of category.
            'page_number' (int): number of page. """

        self.products = []
        self.pages = 0
        self.finish = False
        self.counting = False

        count = 1
        # Get all Open Food Facts products
        while self.finish is not True:

            r = get(
                "https://{}.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0={}&page_size=1000&action=display&json=1&page={}"
                .format(language, category, count)
            )
            result = r.json()
            products_number = result["count"]

            if self.counting is not True:

                count_pages = products_number / 1000

                if count_pages <= 1000:
                    self.pages = 1
                else:
                    self.pages = int(count_pages) + 1

                self.counting = True

            if self.pages == count:
                self.finish = True

            count += 1

            products_list = self.product_treatment(
                category=category,
                products=result["products"])

        return products_list

    def product_treatment(
        self,
        category=None,
        products=None
    ):

        err = 0

        products_list = []

        for product in products:

            product_dict = {}

            # -- NAME OF PRODUCT [500 POINTS] -- #
            try:

                product_name = str(product["product_name"])

                if product_name == "":
                    err += 1

            except Exception as e:
                product_name = "empty"

            # -- URL OF PRODUCT [100 POINTS] -- #
            try:
                product_url = str(product["url"])
            except Exception as e:
                product_url = "empty"

            # -- NAME OF CREATOR PRODUCT SHEET [100 POINTS] -- #
            try:
                product_creator = str(product["creator"])
            except Exception as e:
                product_creator = "empty"

            # -- STORES NAME OF PRODUCTS [50 POINTS] -- #
            try:
                product_stores = str(product["stores"])
            except Exception as e:
                product_stores = "empty"

            # -- NUTRITION GRADE VALUE [500 POINTS] -- #
            try:
                product_nutriscore = str(product["nutrition_grades"])
            except Exception as e:
                product_nutriscore = "empty"

            # -- IMAGE URL OF PRODUCT [25 POINTS] -- #
            try:
                product_image_url = str(product["image_url"])
            except Exception as e:
                product_image_url = "empty"

            # -- ENERGY OF PRODUCT [50 POINTS] -- #
            try:
                energy = str(product["nutriments"]["energy_unit"])
                energy_value = int(
                    product["nutriments"]["energy_100g"]
                )

                if energy.lower() == "kcal":
                    product_kj = energy_value * 4.1868
                    product_kcal = energy_value
                elif energy.lower() == "kj":
                    product_kj = energy_value
                    product_kcal = energy_value / 4.1868

            except Exception as e:
                product_kj = 0
                product_kcal = 0

            # -- CATEGORY ID [100 POINTS] -- #
            try:
                product_category_id = str(category)
            except Exception as e:
                product_category_id = "empty"

            # -- SUGAR VALUE [50 POINTS] -- #
            try:
                product_sugar = int(product["nutriments"]["sugars_100g"])
            except Exception as e:
                product_sugar = 0

            # -- BRANDS TAGS OF PRODUCTS [50 POINTS] -- #
            try:
                brands_list = product["brands_tags"]
                product_brands = ",".join(brands_list)
            except Exception as e:
                product_brands = "empty"

            if err == 0:
                product_dict["product_name"] = product_name
                product_dict["product_url"] = product_url
                product_dict["product_creator"] = product_creator
                product_dict["product_stores"] = product_stores
                product_dict["product_nutriscore"] = product_nutriscore
                product_dict["product_image_url"] = product_image_url
                product_dict["product_category_id"] = product_category_id
                product_dict["product_kj"] = product_kj
                product_dict["product_kcal"] = product_kcal
                product_dict["product_sugar"] = product_sugar
                product_dict["product_brands"] = product_brands

                products_list.append(product_dict)

        return products_list
