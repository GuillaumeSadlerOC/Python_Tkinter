""" DISPLAYER
Is responsible for managing the display \
of the different program frames. """

# -*- coding: utf-8 -*-
# From Python 3
import json
import time
# From Tkinter
from tkinter import Tk, PhotoImage
# From Program - Views - Package 'Others'
from frontend.views.others.error404 import Error404
from frontend.views.others.empty import Empty
from frontend.views.others.home import Home
from frontend.views.others.load import Load
from frontend.views.others.settings import Settings
# From Program - Views - Package 'Product'
from frontend.views.product.edit import ProductEdit
from frontend.views.product.favorite import ProductFavorite
from frontend.views.product.sheet import ProductSheet
from frontend.views.product.substitutes import ProductSubstitutes
# From Program - Views - Package 'Search'
from frontend.views.search.categories import SearchCategories
from frontend.views.search.engine import SearchEngine
from frontend.views.search.result import SearchResult
# From Program - Views - Package 'Update'
from frontend.views.update.serverconn import UpdateServerConn
from frontend.views.update.languages import UpdateLanguages
from frontend.views.update.categories import UpdateCategories
# From Program - Views - Package 'User'
from frontend.views.user.avatars import UserAvatars
from frontend.views.user.form import UserForm
from frontend.views.user.profil import UserProfil
from frontend.views.user.welcome import UserWelcome

from frontend.structure.page import Page


class Displayer():
    def __init__(
        self,
        window=None,
        session=None
    ):
        """ 'window'  (Obj): Tk window.
            'page'    (Obj): instance of Page.
            'session' (Obj): instance of Session. """

        # Instances
        self.window = window
        self.session = session
        self.page = None

        self.views = {}

        # Package of views : Update
        self.update_server_conn = None
        self.update_languages = None
        self.update_categories = None

        self.current_view = "user_welcome"

        # Package of views : Others
        self.load = None

        self.page = Page(
            window=self.window,
            displayer=self
        )

        self.initialization_views()

    def display(
        self,
        c_view=None,
        f_view=None,
        **kwargs
    ):
        """ Display view. """

        # 1. Remove the view that calls the function
        if c_view is not None:
            self.views[
                c_view
            ].m_frame.grid_remove()

        # VIEW
        error = self.views[f_view].fill(
            view=c_view,
            **kwargs
        )

        if error is None:

            self.page.menubar.create_menu_bar()

            self.views[f_view].m_frame.grid()

            self.current_view = f_view

            name = self.views[f_view].name
            self.page.header.var_title.set(name)

    def initialization_views(self):
        """ Initialize all frames of program.
        Must only be called once. """

        # 02. 'Empty' view - Package 'Others'
        self.empty = Empty(
            container=self.page.container,
            displayer=self,
            session=self.session
        )
        self.views[
            "empty"
        ] = self.empty
        # 02. 'Home' view - Package 'Others'
        self.error_404 = Error404(
            container=self.page.container,
            displayer=self,
            session=self.session
        )
        self.views[
            "error_404"
        ] = self.error_404
        # 02. 'Home' view - Package 'Others'
        self.home = Home(
            container=self.page.container,
            displayer=self,
            session=self.session
        )
        self.views[
            "home"
        ] = self.home
        # 03. 'Load' view - Package 'Others'
        self.load = Load(
            container=self.page.container,
            displayer=self,
            session=self.session
        )
        self.views[
            "load"
        ] = self.load
        # 03. 'Settings' view - Package 'Others'
        self.settings = Settings(
            container=self.page.container,
            displayer=self,
            session=self.session
        )
        self.views[
            "settings"
        ] = self.settings

        # 04. 'edit' view - Package 'Product'
        self.product_edit = ProductEdit(
            container=self.page.container,
            displayer=self,
            session=self.session
        )
        self.views[
            "product_edit"
        ] = self.product_edit
        # 05. 'favorite' view - Package 'Product'
        self.product_favorite = ProductFavorite(
            container=self.page.container,
            displayer=self,
            session=self.session
        )
        self.views[
            "product_favorite"
        ] = self.product_favorite
        # 06. 'sheet' view - Package 'Product'
        self.product_sheet = ProductSheet(
            container=self.page.container,
            displayer=self,
            session=self.session
        )
        self.views[
            "product_sheet"
        ] = self.product_sheet
        # 07. 'substitutes' view - Package 'Product'
        self.product_substitutes = ProductSubstitutes(
            container=self.page.container,
            displayer=self,
            session=self.session
        )
        self.views[
            "product_substitutes"
        ] = self.product_substitutes
        # 08. 'categories' view - Package 'Search'
        self.search_categories = SearchCategories(
            container=self.page.container,
            displayer=self,
            session=self.session
        )
        self.views[
            "search_categories"
        ] = self.search_categories
        # 09. 'engine' view - Package 'Search'
        self.search_engine = SearchEngine(
            container=self.page.container,
            displayer=self,
            session=self.session
        )
        self.views[
            "search_engine"
        ] = self.search_engine
        # 10. 'result' view - Package 'Search'
        self.search_result = SearchResult(
            container=self.page.container,
            displayer=self,
            session=self.session
        )
        self.views[
            "search_result"
        ] = self.search_result
        # 10. 'categories' view - Package 'Update'
        self.update_categories = UpdateCategories(
            container=self.page.container,
            displayer=self,
            session=self.session
        )
        self.views[
            "update_categories"
        ] = self.update_categories

        # 11. 'languages' view - Package 'Update'
        self.update_languages = UpdateLanguages(
            container=self.page.container,
            displayer=self,
            session=self.session
        )
        self.views[
            "update_languages"
        ] = self.update_languages
        # 12. 'server_conn' view - Package 'Update'
        self.update_server_conn = UpdateServerConn(
            container=self.page.container,
            displayer=self,
            session=self.session
        )
        self.views[
            "update_server_conn"
        ] = self.update_server_conn
        # 12. 'avatars' view - Package 'User'
        self.user_avatars = UserAvatars(
            container=self.page.container,
            displayer=self,
            session=self.session
        )
        self.views[
            "user_avatars"
        ] = self.user_avatars
        # 14. 'form' view - Package 'User'
        self.user_form = UserForm(
            container=self.page.container,
            displayer=self,
            session=self.session
        )
        self.views[
            "user_form"
        ] = self.user_form
        # 15. 'profil' view - Package 'User'
        self.user_profil = UserProfil(
            container=self.page.container,
            displayer=self,
            session=self.session
        )
        self.views[
            "user_profil"
        ] = self.user_profil
        # 16. 'welcome' view - Package 'User'
        self.user_welcome = UserWelcome(
            container=self.page.container,
            displayer=self,
            session=self.session
        )
        self.views[
            "user_welcome"
        ] = self.user_welcome

        for key, value in self.views.items():
            value.m_frame.grid_forget()
