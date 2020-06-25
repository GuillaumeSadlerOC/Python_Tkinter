""" PRODUCT SHEET
PACKAGE 'PRODUCT'. """

# -*- coding: utf-8 -*-
# From Python 3
import requests
from io import BytesIO
# From Tkinter
from tkinter import PhotoImage
from tkinter import BOTTOM, X, RIGHT
from tkinter import Label, Button, Canvas
# From Pillow
from PIL import Image, ImageTk
# From Program
from frontend.framework.grid import Grid


class ProductSheet():
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

        # Widgets row 0
        self.w_title = None
        # Widgets row 1
        self.w_img_product = None
        self.w_name_product = None
        self.w_brand_product = None
        self.w_nutriscore_product = None
        # Widgets row 2
        self.w_best_button = None
        self.w_edit_button = None
        self.w_trash_button = None
        self.w_add_button = None

        # Widgets row 4
        self.canvas_calories = None
        self.w_calories_img = None
        self.w_calories_label = None

        # Widgets row 5
        self.canvas_sugar = None
        self.w_sugar_img = None
        self.w_sugar_label = None
        self.w_sugar_value = None

        # Widgets row 6
        self.w_stores_img = None
        self.w_stores_label = None
        self.w_stores_value = None
        # Widgets row 7
        self.w_author_img = None
        self.w_author_label = None
        self.w_author_value = None
        # Widgets row 8
        self.w_submit_button = None

        self.favorite_status = False

        self.product = None
        self.product_id = 0
        self.product_img = None
        self.product_name = None
        self.product_brand = None
        self.product_nutriscore = None
        self.product_kcal = 0
        self.product_sugar = 0
        self.product_author = None
        self.product_store = None

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
        self.row_2(action="construct")
        self.row_3(action="construct")
        self.row_4(action="construct")
        self.row_5(action="construct")
        self.row_6(action="construct")
        self.row_7(action="construct")

    def fill(self, **kwargs):
        """ Fill the view rows.
            'json_script'   (dict): texts for view.
            'name'          (str): view name. """

        for key, value in kwargs.items():

            if key == "view":
                self.previous_view = value
            elif key == "product_id":
                self.product_id = value

        # 1. Get the script.
        self.json_script = self.session.get_script(
            package_name="product",
            file_name="sheet"
        )
        # 2. Save name of view for displayer.
        self.name = self.json_script.get("view_name")

        # Get product informations
        self.product = self.session.dbmanager.db_product.read(
            action="id",
            product_id=self.product_id
        )

        favorite = self.session.dbmanager.db_user_prod.read(
            action="test",
            user_id=self.session.user_id,
            product_id=self.product_id
        )

        if len(favorite) == 1:
            self.favorite_status = True
        else:
            self.favorite_status = False

        self.product_img = self.product[0]["product_img_url"]
        self.product_name = self.product[0]["product_name"]
        self.product_brand = self.product[0]["product_brand"]
        self.product_nutriscore = self.product[0]["product_nutriscore"]
        self.product_kcal = self.product[0]["product_kcal"]
        self.product_sugar = self.product[0]["product_sugar"]
        self.product_author = self.product[0]["product_creator"]
        self.product_store = self.product[0]["product_store"]

        # 3. Refresh rows.
        if self.fill_status is True:
            self.row_0(action="refresh")
            self.row_1(action="refresh")
            self.row_2(action="refresh")
            self.row_3(action="refresh")
            self.row_4(action="refresh")
            self.row_5(action="refresh")
            self.row_6(action="refresh")
            self.row_7(action="refresh")

        # 4. Fill the view rows.
        self.row_0(action="fill")
        self.row_1(action="fill")
        self.row_2(action="fill")
        self.row_3(action="fill")
        self.row_4(action="fill")
        self.row_5(action="fill")
        self.row_6(action="fill")
        self.row_7(action="fill")
        self.fill_status = True

    def display_substitutes(self):
        """ Display substitues. """

        self.displayer.display(
            c_view="product_sheet",
            f_view="product_substitutes",
            product_id=self.product_id
        )

    def display_edit(self):
        """ Display product edit. """

        self.displayer.display(
            c_view="product_sheet",
            f_view="product_edit",
            product_id=self.product_id
        )

    def display_search(self):
        """ Display "search". """

        self.displayer.display(
            c_view="product_sheet",
            f_view="search_engine"
        )

    def add_product(self):
        """ Add product to favorite in database. """

        self.session.dbmanager.db_user_prod.create(
            user_id=self.session.user_id,
            product_id=self.product_id
        )

        self.favorite_status = True
        self.row_1("refresh")
        self.row_1("fill")

    def del_product_to_favorite(self):
        """ Add product to favorite in database. """

        self.session.dbmanager.db_user_prod.delete(
            user_id=self.session.user_id,
            product_id=self.product_id
        )

        self.favorite_status = False
        self.row_1("refresh")
        self.row_1("fill")

    def trash_product(self):
        """ Delete product to database. """

        self.session.dbmanager.db_product.delete(
            product_id=self.product_id
        )

        self.display_search()

    def row_0(self, action=None):
        """ Name : PRODUCT IMAGE
            cols : 3 """

        if action == "construct":

            # -- CREATE ROW -- #
            self.grid.row(
                width=self.width,
                height=250,
                padx=self.padx,
                pady=self.pady,
                bg="#ffffff"
            )
            # -- CREATE COLS -- #
            self.grid.column(
                span=6,
                row=0,
                width=None,
                height=None,
                padx=None,
                pady=None,
                bg=None
            )
            self.grid.column(
                span=5,
                row=0,
                width=None,
                height=None,
                padx=30,
                pady=30,
                bg=None
            )
            self.grid.column(
                span=1,
                row=0,
                width=None,
                height=None,
                padx=None,
                pady=None,
                bg=None
            )

        elif action == "fill":

            if self.w_img_product is None:
                # -- COLUMN 1 : PRODUCT IMAGE -- #
                if self.product_img == "empty":
                    img = Image.open(
                        "frontend/images/no_image.png"
                    )
                else:
                    req = requests.get(self.product_img)
                    img = Image.open(BytesIO(req.content))

                img_resize = img.resize((150, 200), Image.ANTIALIAS)
                tk_img_product = ImageTk.PhotoImage(img_resize)
                self.w_img_product = Label(
                    self.grid.col_frames[0][0],
                    image=tk_img_product,
                    bg="#ffffff"
                )
                self.w_img_product.image = tk_img_product
                self.w_img_product.pack(fill='both', expand=True)

            if self.w_name_product is None:
                # -- COLUMN 2 : PRODUCT NAME -- #
                self.w_name_product = Label(
                    self.grid.col_frames[0][1],
                    text="{}".format(self.product_name),
                    bg="#ffffff",
                    fg="#000000",
                    font="Helvetica 13 normal"
                )
                self.w_name_product.pack(fill='both')

            if self.w_brand_product is None:
                # -- COLUMN 2 : PRODUCT BRAND -- #
                self.w_brand_product = Label(
                    self.grid.col_frames[0][1],
                    text="{}".format(self.product_brand),
                    bg="#ffffff",
                    fg="#000000",
                    font="Helvetica 13 bold"
                )
                self.w_brand_product.pack(fill='both')

            if self.w_nutriscore_product is None:
                # -- COLUMN 2 : PRODUCT NUTRISCORE -- #
                img = Image.open(
                    "frontend/images/nutriscores/nutriscore_{}.png"
                    .format(self.product_nutriscore)
                )
                imgResize = img.resize((160, 90), Image.ANTIALIAS)
                nutriscore_img = ImageTk.PhotoImage(imgResize)

                self.w_nutriscore_product = Label(
                    self.grid.col_frames[0][1],
                    image=nutriscore_img,
                    bg="#ffffff"
                )
                self.w_nutriscore_product.image = nutriscore_img
                self.w_nutriscore_product.pack(fill="both", expand=True)

        elif action == "refresh":

            self.w_img_product.pack_forget()
            self.w_name_product.pack_forget()
            self.w_brand_product.pack_forget()
            self.w_nutriscore_product.pack_forget()

            self.w_img_product = None
            self.w_name_product = None
            self.w_brand_product = None
            self.w_nutriscore_product = None

    def row_1(self, action=None):
        """ Name : BUTTONS
            cols : 6 """

        if action == "construct":

            # -- CREATE ROW -- #
            self.grid.row(
                width=self.width,
                height=50,
                padx=0,
                pady=0,
                bg="#ffffff"
            )
            # -- CREATE COLS -- #
            self.grid.column(
                span=7,
                row=1,
                width=None,
                height=None,
                padx=5,
                pady=5,
                bg=None
            )
            self.grid.column(
                span=1,
                row=1,
                width=None,
                height=None,
                padx=5,
                pady=5,
                bg=None
            )
            self.grid.column(
                span=1,
                row=1,
                width=None,
                height=None,
                padx=5,
                pady=5,
                bg=None
            )
            self.grid.column(
                span=1,
                row=1,
                width=None,
                height=None,
                padx=5,
                pady=5,
                bg=None
            )
            self.grid.column(
                span=1,
                row=1,
                width=None,
                height=None,
                padx=5,
                pady=5,
                bg=None
            )
            self.grid.column(
                span=1,
                row=1,
                width=None,
                height=None,
                padx=5,
                pady=5,
                bg=None
            )

        elif action == "fill":

            # -- COLUMN 1 : EMPTY -- #

            if self.w_best_button is None:

                # -- COLUMN 3 : SUBSTITUTES BUTTON -- #
                img = Image.open(
                    "frontend/images/views/product_sheet/best_product_1.png"
                )
                imgResize = img.resize((25, 25), Image.ANTIALIAS)
                best_img = ImageTk.PhotoImage(imgResize)

                self.w_best_button = Button(
                    self.grid.col_frames[1][1],
                    image=best_img,
                    bg="#ffffff",
                    command=self.display_substitutes
                )
                self.w_best_button.image = best_img
                self.w_best_button.pack(fill='both', expand=True)

            if self.w_edit_button is None:

                # -- COLUMN 4 : PRODUCT SHEET BUTTON -- #
                img = Image.open(
                    "frontend/images/views/product_sheet/edit.png"
                )
                imgResize = img.resize((25, 25), Image.ANTIALIAS)
                edit_img = ImageTk.PhotoImage(imgResize)

                self.w_edit_button = Button(
                    self.grid.col_frames[1][2],
                    image=edit_img,
                    bg="#ffffff",
                    command=self.display_edit
                )
                self.w_edit_button.image = edit_img
                self.w_edit_button.pack(fill='both', expand=True)

            if self.w_trash_button is None:

                # -- COLUMN 5 : TRASH BUTTON -- #
                img = Image.open(
                    "frontend/images/views/product_sheet/trash.png"
                )
                imgResize = img.resize((25, 25), Image.ANTIALIAS)
                trash_img = ImageTk.PhotoImage(imgResize)

                self.w_trash_button = Button(
                    self.grid.col_frames[1][3],
                    image=trash_img,
                    bg="#ffffff",
                    command=self.trash_product
                )
                self.w_trash_button.image = trash_img
                self.w_trash_button.pack(fill='both', expand=True)

            if self.w_add_button is None:

                img = Image.open(
                    "frontend/images/views/product_sheet/icon_add_{}.png"
                    .format(self.product_nutriscore)
                )
                imgResize = img.resize((25, 25), Image.ANTIALIAS)
                add_img = ImageTk.PhotoImage(imgResize)

                if self.favorite_status is False:
                    # -- COLUMN 6 : ADD BUTTON -- #
                    self.w_add_button = Button(
                        self.grid.col_frames[1][4],
                        image=add_img,
                        bg="#ffffff",
                        command=self.add_product
                    )
                    self.w_add_button.image = add_img
                    self.w_add_button.pack(fill='both', expand=True)
                else:
                    img = Image.open(
                        "frontend/images/views/product_sheet/favorite.png"
                    )
                    imgResize = img.resize((25, 25), Image.ANTIALIAS)
                    add_img = ImageTk.PhotoImage(imgResize)
                    # -- COLUMN 6 : ADD BUTTON -- #
                    self.w_add_button = Button(
                        self.grid.col_frames[1][4],
                        image=add_img,
                        bg="#ffffff",
                        command=self.del_product_to_favorite
                    )
                    self.w_add_button.image = add_img
                    self.w_add_button.pack(fill='both', expand=True)

        elif action == "refresh":

            self.w_best_button.pack_forget()
            self.w_edit_button.pack_forget()
            self.w_trash_button.pack_forget()
            self.w_add_button.pack_forget()

            self.w_best_button = None
            self.w_edit_button = None
            self.w_trash_button = None
            self.w_add_button = None

    def row_2(self, action=None):
        """ Name : SPACE
            cols : 1 """

        if action == "construct":

            # -- CREATE ROW -- #
            self.grid.row(
                width=self.width,
                height=25,
                padx=self.padx,
                pady=self.pady,
                bg="#ffffff"
            )
            # -- CREATE COLS -- #
            self.grid.column(
                span=12,
                row=2,
                width=None,
                height=None,
                padx=None,
                pady=None,
                bg=None
            )

        elif action == "fill":
            pass

        elif action == "refresh":
            pass

    def row_3(self, action=None):
        """ Name : PRODUCT CALORIES
            cols : 3 """

        line = "line_empty"
        line_lenght = 90

        if self.product_kcal == 0:
            line = "line_empty"
            line_lenght = 90
        elif self.product_kcal <= 100:
            line = "line_a"
            line_lenght = 90
        elif self.product_kcal <= 500:
            line = "line_b"
            line_lenght = 180
        elif self.product_kcal <= 1000:
            line = "line_c"
            line_lenght = 270
        elif self.product_kcal <= 1500:
            line = "line_d"
            line_lenght = 360
        elif self.product_kcal > 1501:
            line = "line_e"
            line_lenght = 450

        if action == "construct":

            # -- CREATE ROW -- #
            self.grid.row(
                width=self.width,
                height=55,
                padx=0,
                pady=5,
                bg="#ffffff"
            )
            # -- CREATE COLS -- #
            self.grid.column(
                span=1,
                row=3,
                width=None,
                height=None,
                padx=None,
                pady=None,
                bg=None
            )
            self.grid.column(
                span=2,
                row=3,
                width=None,
                height=None,
                padx=None,
                pady=None,
                bg=None
            )
            self.col = self.grid.column(
                span=9,
                row=3,
                width=None,
                height=None,
                padx=None,
                pady=None,
                bg=None
            )

        elif action == "fill":

            # Get texts for this row
            txt = self.json_script.get("row_3")

            if self.w_calories_img is None:

                # -- COLUMN 1 : CALORIES IMAGE -- #
                img = Image.open(
                    "frontend/images/views/product_sheet/calories.png"
                )
                imgResize = img.resize((30, 30), Image.ANTIALIAS)
                calories_img = ImageTk.PhotoImage(imgResize)

                self.w_calories_img = Label(
                    self.grid.col_frames[3][0],
                    image=calories_img,
                    bg="#ffffff"
                )
                self.w_calories_img.image = calories_img
                self.w_calories_img.pack(fill="both", expand=True)

            if self.w_calories_label is None:

                # -- COLUMN 2 : CALORIES NAME -- #
                self.w_calories_label = Label(
                    self.grid.col_frames[3][1],
                    anchor="w",
                    text=txt.get("calories_label"),
                    bg="#ffffff",
                    font="Helvetica 11 bold"
                )
                self.w_calories_label.pack(fill="both", expand=True)

            if self.canvas_calories is None:

                img = Image.open(
                    "frontend/images/views/product_sheet/{}.png"
                    .format(line)
                )
                imgResize = img.resize((line_lenght, 35), Image.ANTIALIAS)
                kcal_img = ImageTk.PhotoImage(imgResize)

                self.canvas_calories = Canvas(
                    self.grid.col_frames[3][2],
                    width=self.width,
                    height=35,
                    highlightthickness=0,
                    bg="#ffffff"
                    )
                self.canvas_calories.pack(expand=True, fill="both")

                self.canvas_calories.create_image(0, 0, image=kcal_img, anchor="nw")
                self.canvas_calories.image = kcal_img

                self.canvas_calories.create_text(
                    5,
                    9,
                    text=" {} Kcal".format(self.product_kcal),
                    anchor='nw',
                    fill="#ffffff",
                    font="Helvetica 10 bold")

        elif action == "refresh":

            self.canvas_calories.delete("all")
            self.canvas_calories.pack_forget()
            self.w_calories_label.pack_forget()
            self.w_calories_img.pack_forget()

            self.canvas_calories = None
            self.w_calories_label = None
            self.w_calories_img = None

    def row_4(self, action=None):
        """ Name : PRODUCT SUGAR
            cols : 3 """

        line = "line_empty"
        line_lenght = 90

        # ----- ROW 5 : PRODUCT SUGAR ----- #
        if self.product_sugar == 0:
            line = "line_empty"
            line_lenght = 90
        elif self.product_sugar <= 10:
            line = "line_a"
            line_lenght = 90
        elif self.product_sugar <= 50:
            line = "line_b"
            line_lenght = 180
        elif self.product_sugar <= 100:
            line = "line_c"
            line_lenght = 270
        elif self.product_sugar <= 150:
            line = "line_d"
            line_lenght = 360
        elif self.product_sugar > 151:
            line = "line_e"
            line_lenght = 450

        if action == "construct":

            # -- CREATE ROW -- #
            self.grid.row(
                width=self.width,
                height=55,
                padx=self.padx,
                pady=self.pady,
                bg="#ffffff"
            )
            # -- CREATE COLS -- #
            self.grid.column(
                span=1,
                row=4,
                width=None,
                height=None,
                padx=None,
                pady=None,
                bg=None
            )
            self.grid.column(
                span=2,
                row=4,
                width=None,
                height=None,
                padx=None,
                pady=None,
                bg=None
            )
            self.grid.column(
                span=9,
                row=4,
                width=None,
                height=None,
                padx=None,
                pady=None,
                bg=None
            )

        elif action == "fill":

            # Get texts for this row
            txt = self.json_script.get("row_4")

            if self.w_sugar_img is None:

                # -- COLUMN 1 : SUGAR IMAGE -- #
                img = Image.open(
                    "frontend/images/views/product_sheet/sugar.png"
                )
                img_resize = img.resize((30, 30), Image.ANTIALIAS)
                sugar_img = ImageTk.PhotoImage(img_resize)

                self.w_sugar_img = Label(
                    self.grid.col_frames[4][0],
                    image=sugar_img,
                    bg="#ffffff"
                )
                self.w_sugar_img.image = sugar_img
                self.w_sugar_img.pack(side=RIGHT, fill="both", expand=True)

            if self.w_sugar_label is None:

                # -- COLUMN 2 : SUGAR LABEL -- #
                self.w_sugar_label = Label(
                    self.grid.col_frames[4][1],
                    anchor="w",
                    text=txt.get("sugar_label"),
                    bg="#ffffff",
                    font="Helvetica 11 bold"
                )
                self.w_sugar_label.pack(fill="both", expand=True)

            if self.canvas_sugar is None:

                img = Image.open(
                    "frontend/images/views/product_sheet/{}.png"
                    .format(line)
                )
                imgResize = img.resize((line_lenght, 35), Image.ANTIALIAS)
                kcal_img = ImageTk.PhotoImage(imgResize)

                self.canvas_sugar = Canvas(
                    self.grid.col_frames[4][2],
                    width=self.width,
                    height=35,
                    highlightthickness=0,
                    bg="#ffffff"
                    )
                self.canvas_sugar.pack(expand=True, fill="both")

                self.canvas_sugar.create_image(0, 0, image=kcal_img, anchor="nw")
                self.canvas_sugar.image = kcal_img

                self.canvas_sugar.create_text(
                    5,
                    9,
                    text=" {} g".format(self.product_sugar),
                    anchor='nw',
                    fill="#ffffff",
                    font="Helvetica 10 bold")

        elif action == "refresh":

            self.canvas_sugar.delete("all")
            self.canvas_sugar.pack_forget()

            self.w_sugar_img.pack_forget()
            self.w_sugar_label.pack_forget()

            self.w_sugar_img = None
            self.w_sugar_label = None
            self.canvas_sugar = None

    def row_5(self, action=None):
        """ Name : PRODUCT STORES
            cols : 3 """

        if action == "construct":

            # -- CREATE ROW -- #
            self.grid.row(
                width=self.width,
                height=55,
                padx=self.padx,
                pady=self.pady,
                bg="#ffffff"
            )
            # -- CREATE COLS -- #
            self.grid.column(
                span=1,
                row=5,
                width=None,
                height=None,
                padx=None,
                pady=None,
                bg=None
            )
            self.grid.column(
                span=2,
                row=5,
                width=None,
                height=None,
                padx=None,
                pady=None,
                bg=None
            )
            self.grid.column(
                span=9,
                row=5,
                width=None,
                height=None,
                padx=None,
                pady=None,
                bg=None
            )

        elif action == "fill":

            # Get texts for this row
            txt = self.json_script.get("row_5")

            if self.w_stores_img is None:

                # -- COLUMN 1 : STORES IMAGE -- #
                img = Image.open(
                    "frontend/images/views/product_sheet/store.png"
                )
                img_resize = img.resize((30, 30), Image.ANTIALIAS)
                store_img = ImageTk.PhotoImage(img_resize)

                self.w_stores_img = Label(
                    self.grid.col_frames[5][0],
                    image=store_img,
                    bg="#ffffff"
                )
                self.w_stores_img.image = store_img
                self.w_stores_img.pack(side=RIGHT, fill="both", expand=True)

            if self.w_stores_label is None:

                # -- COLUMN 2 : STORES LABEL -- #
                self.w_stores_label = Label(
                    self.grid.col_frames[5][1],
                    anchor="w",
                    text=txt.get("stores_label"),
                    bg="#ffffff",
                    font="Helvetica 11 bold"
                )
                self.w_stores_label.pack(fill="both", expand=True)

            if self.w_stores_value is None:

                # -- COLUMN 3 : STORES VALUE -- #
                self.w_stores_value = Label(
                    self.grid.col_frames[5][2],
                    anchor="w",
                    text=" {}".format(self.product_store),
                    bg="#ffffff"
                )
                self.w_stores_value.pack(fill="both", expand=True)

        elif action == "refresh":

            self.w_stores_img.pack_forget()
            self.w_stores_label.pack_forget()
            self.w_stores_value.pack_forget()

            self.w_stores_img = None
            self.w_stores_label = None
            self.w_stores_value = None

    def row_6(self, action=None):
        """ Name : AUTHOR
            cols : 3 """

        if action == "construct":

            # -- CREATE ROW -- #
            self.grid.row(
                width=self.width,
                height=55,
                padx=self.padx,
                pady=self.pady,
                bg="#ffffff"
            )
            # -- CREATE COLS -- #
            self.grid.column(
                span=1,
                row=6,
                width=None,
                height=None,
                padx=None,
                pady=None,
                bg=None
            )
            self.grid.column(
                span=2,
                row=6,
                width=None,
                height=None,
                padx=None,
                pady=None,
                bg=None
            )
            self.grid.column(
                span=9,
                row=6,
                width=None,
                height=None,
                padx=None,
                pady=None,
                bg=None
            )

        elif action == "fill":

            # Get texts for this row
            txt = self.json_script.get("row_6")

            if self.w_author_img is None:
                # -- COLUMN 1 : AUTHOR IMAGE -- #
                img = Image.open(
                    "frontend/images/views/product_sheet/copyright.png"
                )
                img_resize = img.resize((30, 30), Image.ANTIALIAS)
                store_img = ImageTk.PhotoImage(img_resize)

                self.w_author_img = Label(
                    self.grid.col_frames[6][0],
                    image=store_img,
                    bg="#ffffff"
                )
                self.w_author_img.image = store_img
                self.w_author_img.pack(side=RIGHT, fill="both", expand=True)

            if self.w_author_label is None:
                # -- COLUMN 2 : AUTHOR LABEL -- #
                self.w_author_label = Label(
                    self.grid.col_frames[6][1],
                    anchor="w",
                    text=txt.get("author_label"),
                    bg="#ffffff",
                    font="Helvetica 11 bold"
                )
                self.w_author_label.pack(fill="both", expand=True)

            if self.w_author_value is None:
                # -- COLUMN 3 : AUTHOR VALUE -- #
                self.w_author_value = Label(
                    self.grid.col_frames[6][2],
                    anchor="w",
                    text=" {}".format(self.product_author),
                    bg="#ffffff"
                )
                self.w_author_value.pack(fill="both", expand=True)

        elif action == "refresh":

            self.w_author_img.pack_forget()
            self.w_author_label.pack_forget()
            self.w_author_value.pack_forget()

            self.w_author_img = None
            self.w_author_label = None
            self.w_author_value = None

    def row_7(self, action=None):
        """ Name : SUBMIT BUTTON
            cols : 4 """

        if action == "construct":

            # -- CREATE ROW -- #
            self.grid.row(
                width=self.width,
                height=100,
                padx=self.padx,
                pady=self.pady,
                bg="#ffffff"
            )
            # -- CREATE COLS -- #
            self.grid.column(
                span=4,
                row=7,
                width=None,
                height=None,
                padx=None,
                pady=None,
                bg=None
            )
            self.grid.column(
                span=4,
                row=7,
                width=None,
                height=None,
                padx=None,
                pady=None,
                bg=None
            )
            self.grid.column(
                span=4,
                row=7,
                width=None,
                height=None,
                padx=None,
                pady=None,
                bg=None
            )

        elif action == "fill":

            # Get texts for this row
            txt = self.json_script.get("row_7")

            # -- COLUMN 1 : EMPTY -- #
            if self.w_submit_button is None:
                # -- COLUMN 3 : SUBMIT BUTTON -- #
                self.w_submit_button = Button(
                    self.grid.col_frames[7][1],
                    text=txt.get("submit_button"),
                    fg="#ffffff",
                    bg="#7A57EC",
                    activeforeground="#ffffff",
                    activebackground="#845EFF",
                    command=self.display_search
                )
                self.w_submit_button.pack(side=BOTTOM, fill=X, expand=True)

            # -- COLUMN 4 : EMPTY -- #

        elif action == "refresh":

            self.w_submit_button.pack_forget()
            self.w_submit_button = None
