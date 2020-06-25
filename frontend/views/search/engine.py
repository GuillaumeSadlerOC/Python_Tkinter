""" SEARCH ENGINE
PACKAGE 'ENGINE'. """

# -*- coding: utf-8 -*-
# From Python 3
# From Tkinter
from tkinter import StringVar, PhotoImage
from tkinter import X
from tkinter import Label, Button, Canvas, Entry
# From Pillow
from PIL import Image, ImageTk
# From Program
from frontend.framework.grid import Grid


class SearchEngine():
    def __init__(
        self,
        container=None,
        displayer=None,
        session=None
    ):
        """ 'container'     (Obj  ): instance of Container.
            'displayer'     (obj  ): instance of Displayer.
            'session,'      (obj  ): instance of Session.
            'grid'          (Obj  ): instance of Grid.

            'f_container'   (Frame): container frame.
            'm_frame'       (Frame): master frame of view.

            'name'          (str  ): name of view.
            'json_script'   (dict ): json dict of script.

            'width'         (int  ): view width.
            'height'        (int  ): view height.
            'padx'          (int  ): view
            'pady'          (int  ): view
            'bg'            (str  ): view bg. """

        # Instances
        self.container = container
        self.displayer = displayer
        self.session = session
        self.grid = None

        # Frames
        self.f_container = self.container.f_container
        self.m_frame = None

        # Informations
        self.name = None

        # Script
        self.json_script = None

        # Style Sheet
        self.width = self.container.width
        self.height = self.container.height
        self.padx = 0
        self.pady = 0
        self.bg = "#ffffff"

        # Tk control variables
        self.var_product_name = StringVar()

        # Widgets row 0
        self.canvas = None
        self.search_entry = None
        self.search_button = None
        # Widgets row 1
        self.w_products_img = None
        self.w_products_button = None
        self.w_nutriscore_imgs = []
        self.w_nutriscore_buttons = []

        self.nutriscores = [
            {
                "nutriscore_a": "#038141",
                "nutriscore_b": "#85bb2f",
                "nutriscore_c": "#fecb02",
                "nutriscore_d": "#ee8100",
                "nutriscore_e": "#e63e11"
            }
        ]
        self.nutri_funcs = [
            {
                "nutriscore_a": self.display_products_a,
                "nutriscore_b": self.display_products_b,
                "nutriscore_c": self.display_products_c,
                "nutriscore_d": self.display_products_d,
                "nutriscore_e": self.display_products_e
            }
        ]
        self.products_count = []

        # Fill status
        self.fill_status = False

        # Previous View in **kwargs
        self.previous_view = None

        # -- Displayer initialisation -- #
        self.construct()

    def construct(self, **kwargs):
        """ Construt view.
            to not fill the view during initialization.
            'grid'      (obj): Instance of Grid.
            'm_frame'   (Frame): Tkinter master frame of view. """

        # 1. Create new grid in page container.
        self.grid = Grid(
            frame=self.f_container,
            width=self.width,
            height=self.height,
            padx=self.padx,
            pady=self.pady,
            bg=self.bg
        )
        # 2. Get view frame for displayer function
        self.m_frame = self.grid.master_frame

        # 3. Construct the view rows
        self.row_0(action="construct")
        self.row_1(action="construct")

    def fill(self, **kwargs):
        """ Fill the view rows.
            'json_script'   (dict): texts for view.
            'name'          (str): view name. """

        for key, value in kwargs.items():

            if key == "view":
                self.previous_view = value

        # 1. Get products
        products = self.session.dbmanager.db_product.count(
                action="*"
            )

        self.products_count.append(products)

        nutriscores = ["a", "b", "c", "d", "e"]
        for nutriscore in nutriscores:

            products = self.session.dbmanager.db_product.count(
                action="nutriscore",
                param=nutriscore
            )

            self.products_count.append(products)

        # 1. Get the script.
        self.json_script = self.session.get_script(
            package_name="search",
            file_name="engine"
        )
        # 2. Save name of view for displayer.
        self.name = self.json_script.get("view_name")

        # 3. Refresh rows.
        if self.fill_status is True:
            self.row_0(action="refresh")
            self.row_1(action="refresh")

        # 4. Fill the view rows.
        self.row_0(action="fill")
        self.row_1(action="fill")
        self.fill_status = True

    def display_previous(self):
        """ Display previous view. """

        self.displayer.display(
            c_view="search_engine",
            f_view=self.previous_view
        )

    def display_products_all(self):
        """ Display view search_result.
            Package "SEARCH" """

        self.displayer.display(
            c_view="search_engine",
            f_view="search_result"
        )

    def display_products_a(self):
        """ Display view search_result.
            Package "SEARCH" """

        self.displayer.display(
            c_view="search_engine",
            f_view="search_result",
            search_action="nutriscore",
            search_value="a"
        )

    def display_products_b(self):
        """ Display view search_result.
            Package "SEARCH" """

        self.displayer.display(
            c_view="search_engine",
            f_view="search_result",
            search_action="nutriscore",
            search_value="b"
        )

    def display_products_c(self):
        """ Display view search_result.
            Package "SEARCH" """

        self.displayer.display(
            c_view="search_engine",
            f_view="search_result",
            search_action="nutriscore",
            search_value="c"
        )

    def display_products_d(self):
        """ Display view search_result.
            Package "SEARCH" """

        self.displayer.display(
            c_view="search_engine",
            f_view="search_result",
            search_action="nutriscore",
            search_value="d"
        )

    def display_products_e(self):
        """ Display view search_result.
            Package "SEARCH" """

        self.displayer.display(
            c_view="search_engine",
            f_view="search_result",
            search_action="nutriscore",
            search_value="e"
        )

    def display_research(self):
        """ Display view search_result.
            Package "SEARCH" """

        self.product_name = self.var_product_name.get()
        self.displayer.display(
            c_view="search_engine",
            f_view="search_result",
            search_action="key",
            search_value=self.product_name
        )

    def row_0(self, action=None):
        """ Name : TITLE
            cols : 1 """

        if action == "construct":

            # -- CREATE ROW -- #
            self.grid.row(
                width=self.width,
                height=500,
                padx=0,
                pady=0,
                bg="#ffffff"
            )
            # -- CREATE COLS -- #
            self.grid.column(
                span=12,
                row=0,
                width=None,
                height=None,
                padx=None,
                pady=None,
                bg=None
            )

        elif action == "fill":

            # Get texts for this row
            txt = self.json_script.get("row_0")

            if self.canvas is None:

                img = Image.open(
                        "frontend/images/views/search/background.jpg"
                    )
                imgResize = img.resize((640, 500), Image.ANTIALIAS)
                imgTkinter = ImageTk.PhotoImage(imgResize)

                self.canvas = Canvas(
                    self.grid.col_frames[0][0],
                    width=self.width,
                    height=500,
                    highlightthickness=0
                    )
                self.canvas.pack(expand=True, fill="both")

                self.canvas.create_image(0, 0, image=imgTkinter, anchor="nw")
                self.canvas.image = imgTkinter

                self.canvas.create_text(
                    100,
                    100,
                    text=txt.get("view_title"),
                    anchor='nw',
                    fill="#ffffff",
                    font="Helvetica 20 bold")

                self.canvas.create_text(
                    100,
                    135,
                    text=txt.get("view_subtitle"),
                    anchor='nw',
                    fill="#ffffff",
                    font="Helvetica 12 bold")

                self.search_entry = Entry(
                    self.canvas,
                    textvariable=self.var_product_name,
                    borderwidth=0
                )
                self.search_entry.place(
                    x=100,
                    y=170,
                    height=50,
                    width=350
                )

                self.search_button = Button(
                    self.canvas,
                    text="Rechercher",
                    fg="#ffffff",
                    bg="#7A57EC",
                    activeforeground="#ffffff",
                    activebackground="#845EFF",
                    borderwidth=0,
                    command=self.display_research
                )
                self.search_button.place(
                    x=450,
                    y=170,
                    height=50,
                    width=100
                )

        elif action == "refresh":
            """ Refresh this row. """

            self.canvas.delete("all")
            self.canvas.pack_forget()
            self.search_entry.delete(0, 1000)
            self.search_entry.place_forget()
            self.search_button.place_forget()

            self.canvas = None
            self.search_entry = None
            self.search_button = None

    def row_1(self, action=None):
        """ Name : NUTRISCORES
            cols : 6 """

        if action == "construct":

            # -- CREATE ROW -- #
            self.grid.row(
                width=self.width,
                height=150,
                padx=self.padx,
                pady=self.pady,
                bg="#ffffff"
            )
            # -- CREATE COLS -- #
            self.grid.column(
                span=2,
                row=1,
                width=None,
                height=None,
                padx=None,
                pady=None,
                bg=None
            )
            self.grid.column(
                span=2,
                row=1,
                width=None,
                height=None,
                padx=None,
                pady=None,
                bg=None
            )
            self.grid.column(
                span=2,
                row=1,
                width=None,
                height=None,
                padx=None,
                pady=None,
                bg=None
            )
            self.grid.column(
                span=2,
                row=1,
                width=None,
                height=None,
                padx=None,
                pady=None,
                bg=None
            )
            self.grid.column(
                span=2,
                row=1,
                width=None,
                height=None,
                padx=None,
                pady=None,
                bg=None
            )
            self.grid.column(
                span=2,
                row=1,
                width=None,
                height=None,
                padx=None,
                pady=None,
                bg=None
            )

        elif action == "fill":

            # Get texts for this row
            txt = self.json_script.get("row_1")

            if self.w_products_img is None:
                img = Image.open(
                    "frontend/images/views/search/products.png"
                )
                imgResize = img.resize((80, 70), Image.ANTIALIAS)
                imgTkinter = ImageTk.PhotoImage(imgResize)

                self.w_products_img = Label(
                    self.grid.col_frames[1][0],
                    image=imgTkinter,
                    borderwidth=5,
                    bg="#ffffff"
                )
                self.w_products_img.image = imgTkinter
                self.w_products_img.pack(fill="both", expand=True)

            if self.w_products_button is None:

                self.w_products_button = Button(
                    self.grid.col_frames[1][0],
                    text="{} \n products".format(self.products_count[0]),
                    fg="#000000",
                    bg="#ffffff",
                    highlightbackground="#ffffff",
                    activeforeground="#000000",
                    activebackground="#ededed",
                    borderwidth=0,
                    font="Helvetica 10 bold",
                    command=self.display_products_all
                )
                self.w_products_button.pack(fill="both")

            nutri_count = 1
            for nutriscore in self.nutriscores:

                for key, value in nutriscore.items():

                    img = Image.open(
                        "frontend/images/nutriscores/{}.png"
                        .format(key)
                    )
                    imgResize = img.resize((90, 50), Image.ANTIALIAS)
                    imgTkinter = ImageTk.PhotoImage(imgResize)

                    w_nutriscore_img = Label(
                        self.grid.col_frames[1][nutri_count],
                        image=imgTkinter,
                        borderwidth=15,
                        bg=value
                    )
                    w_nutriscore_img.image = imgTkinter
                    w_nutriscore_img.pack(fill="both", expand=True)

                    w_nutriscore_button = Button(
                        self.grid.col_frames[1][nutri_count],
                        text="{} \n products".format(
                            self.products_count[nutri_count]
                        ),
                        fg="#ffffff",
                        bg=value,
                        highlightbackground=value,
                        activeforeground="#000000",
                        activebackground="#ededed",
                        borderwidth=0,
                        font="Helvetica 10 bold",
                        command=self.nutri_funcs[0].get(key)
                    )
                    w_nutriscore_button.pack(fill="both")

                    self.w_nutriscore_imgs.append(w_nutriscore_img)
                    self.w_nutriscore_buttons.append(w_nutriscore_button)

                    nutri_count += 1

        elif action == "refresh":
            """ Refresh this row. """

            if len(self.w_nutriscore_imgs) > 0:
                for w_nutriscore_img in self.w_nutriscore_imgs:
                    w_nutriscore_img.pack_forget()

            if len(self.w_nutriscore_buttons) > 0:
                for w_nutriscore_button in self.w_nutriscore_buttons:
                    w_nutriscore_button.pack_forget()

            self.w_products_img.pack_forget()
            self.w_products_button.pack_forget()

            self.w_products_img = None
            self.w_products_button = None

            self.w_nutriscore_imgs = []
            self.w_nutriscore_buttons = []
