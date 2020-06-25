""" MENUBAR
This class is instantiate by an instance of MainView. """

# -*- coding: utf-8 -*-
# From Python 3
# From Tkinter
from tkinter import Menu, Label
# From Pillow
from PIL import Image, ImageTk
# From Program


class MenuBar():

    def __init__(self, displayer=None):
        """ window      (Frame): Tk window frame.
            displayer   (Obj  ): Instance of Displayer. """

        # Attributes initialised
        self.displayer = displayer
        self.window = self.displayer.window
        self.session = self.displayer.session
        self.previous_view = self.displayer.current_view
        self.other_language = "en"

        self.menubar = None

        en_flag = Image.open(
            "frontend/images/flags/en.png"
        )
        imgResize = en_flag.resize((18, 18), Image.ANTIALIAS)
        self.english_flag = ImageTk.PhotoImage(imgResize)

        fr_flag = Image.open(
            "frontend/images/flags/fr.png"
        )
        imgResize = fr_flag.resize((18, 18), Image.ANTIALIAS)
        self.french_flag = ImageTk.PhotoImage(imgResize)

        if self.session.gui_language == "en":
            self.current_flag = self.english_flag
            self.other_flag = self.french_flag
        elif self.session.gui_language == "fr":
            self.current_flag = self.french_flag
            self.other_flag = self.english_flag

        # Script
        self.json_script = None

        self.create_menu_bar()

    def display_home(self):
        """ Display "home" view. """

        self.previous_view = self.displayer.current_view
        self.displayer.display(
            c_view=self.previous_view,
            f_view="home"
        )

    def display_settings(self):
        """ Display "Settings" view. """

        self.previous_view = self.displayer.current_view
        self.displayer.display(
            c_view=self.previous_view,
            f_view="settings"
        )

    def display_welcome(self):
        """ Display "welcome" view. """

        self.displayer.session.user_id = None
        self.previous_view = self.displayer.current_view
        self.displayer.display(
            c_view=self.previous_view,
            f_view="user_welcome"
        )

    def display_favorites(self):
        """ Display "favorites" view. """

        self.previous_view = self.displayer.current_view
        self.displayer.display(
            c_view=self.previous_view,
            f_view="product_favorite"
        )

    def display_search(self):
        """ Display "search" view. """

        self.previous_view = self.displayer.current_view
        self.displayer.display(
            c_view=self.previous_view,
            f_view="search_engine"
        )

    def display_search_categories(self):
        """ Display "search_categories" view. """

        self.previous_view = self.displayer.current_view
        self.displayer.display(
            c_view=self.previous_view,
            f_view="search_categories"
        )

    def display_profil(self):
        """ Display "user_profil" view. """

        self.previous_view = self.displayer.current_view
        self.displayer.display(
            c_view=self.previous_view,
            f_view="user_profil"
        )

    def display_user_form(self):
        """ Display "user_form" view. """

        self.previous_view = self.displayer.current_view
        self.displayer.display(
            c_view=self.previous_view,
            f_view="user_form"
        )

    def gui_language(self):
        """ Change the GUI language. """

        if self.session.gui_language == "en":
            self.session.gui_language = "fr"
            self.current_flag = self.french_flag
            self.other_flag = self.english_flag
        elif self.session.gui_language == "fr":
            self.session.gui_language = "en"
            self.current_flag = self.english_flag
            self.other_flag = self.french_flag

        if self.session.gui_language == "en":
            self.other_language = "fr"
        elif self.session.gui_language == "fr":
            self.other_language = "en"

        current_view = self.displayer.current_view
        self.displayer.display(
            c_view=current_view,
            f_view=current_view
        )

        self.create_menu_bar()

    def create_menu_bar(self):
        """ Create Menu bar. """

        self.json_script = self.displayer.session.get_script(
            package_name="structure",
            file_name="menubar"
        )

        self.menubar = Menu(
            self.window,
            activeborderwidth=0,
            bg="#ffffff",
            activebackground="#7A57EC",
            activeforeground="#ffffff",
            bd=0,
            relief="flat"
        )
        self.window.config(menu=self.menubar)

        self.language_menu()
        self.main_menu()
        self.user_menu()
        self.search_menu()
        self.favorite_menu()

    def language_menu(self):
        """ Construct "Language" Menu. """

        languages_menu = Menu(
            self.menubar,
            tearoff=0,
            bg="#7A57EC",
            activebackground="#9473fd",
            activeforeground="#ffffff",
            foreground="#ffffff",
            relief="flat"
        )
        languages_menu.add_command(
            image=self.other_flag,
            label=self.other_language,
            command=self.gui_language
        )
        self.menubar.add_cascade(
            image=self.current_flag,
            label=self.session.gui_language,
            menu=languages_menu
        )
        languages_menu.image = self.current_flag
        languages_menu.image = self.other_flag

    def main_menu(self):
        """ Construct "Main" Menu. """

        # Get texts for this menu
        txt = self.json_script.get("main_menu")

        # ::: menu
        main_menu = Menu(
            self.menubar,
            tearoff=0,
            bg="#7A57EC",
            activebackground="#9473fd",
            activeforeground="#ffffff",
            foreground="#ffffff",
            relief="flat"
        )

        if self.session.user_id is not None:
            main_menu.add_command(
                label=txt.get("Home"),
                command=self.display_home
            )
            main_menu.add_command(
                label=txt.get("settings"),
                command=self.display_settings
            )
            main_menu.add_command(
                label=txt.get("sign_out"),
                command=self.display_welcome
            )
            main_menu.add_separator()

        main_menu.add_command(
            label=txt.get("exit"),
            command=self.window.quit
        )
        self.menubar.add_cascade(
            label=txt.get("label"),
            menu=main_menu
        )

    def search_menu(self):
        """ Construct "Search" Menu. """

        if self.session.user_id is not None:
            # Get texts for this menu
            txt = self.json_script.get("search_menu")

            search_menu = Menu(
                self.menubar,
                tearoff=0,
                bg="#7A57EC",
                activebackground="#9473fd",
                activeforeground="#ffffff",
                foreground="#ffffff",
                relief="flat"
            )
            search_menu.add_command(
                label=txt.get("research"),
                command=self.display_search
            )
            search_menu.add_command(
                label=txt.get("categories"),
                command=self.display_search_categories
            )
            self.menubar.add_cascade(
                label=txt.get("label"),
                menu=search_menu
            )

    def user_menu(self):
        """ Construct "User" Menu. """

        if self.session.user_id is not None:
            # Get texts for this menu
            txt = self.json_script.get("user_menu")

            user_menu = Menu(
                self.menubar,
                tearoff=0,
                bg="#7A57EC",
                activebackground="#9473fd",
                activeforeground="#ffffff",
                foreground="#ffffff",
                relief="flat"
            )
            user_menu.add_command(
                label=txt.get("profil"),
                command=self.display_profil
            )
            user_menu.add_command(
                label=txt.get("creation"),
                command=self.display_user_form
            )
            self.menubar.add_cascade(
                label=txt.get("label"),
                menu=user_menu
            )

    def favorite_menu(self):
        """ Construct "Favorite" Menu. """

        if self.session.user_id is not None:
            # Get texts for this menu
            txt = self.json_script.get("favorite_menu")

            favorite_menu = Menu(
                self.menubar,
                tearoff=0,
                bg="#7A57EC",
                activebackground="#9473fd",
                activeforeground="#ffffff",
                foreground="#ffffff",
                relief="flat"
            )
            favorite_menu.add_command(
                label=txt.get("products"),
                command=self.display_favorites
            )
            self.menubar.add_cascade(
                label=txt.get("label"),
                menu=favorite_menu
            )
