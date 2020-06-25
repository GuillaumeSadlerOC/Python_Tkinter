""" PRODUCT EDIT
PACKAGE 'PRODUCT'. """

# -*- coding: utf-8 -*-
# From Python 3
# From Tkinter
from tkinter import StringVar
from tkinter import BOTTOM, X
from tkinter import Label, Button, Entry
# From Pillow
from PIL import Image, ImageTk
# From Program
from frontend.framework.grid import Grid


class ProductEdit():
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
        self.var_product_store = StringVar()
        self.var_product_nutriscore = StringVar()
        self.var_product_img_url = StringVar()
        self.var_product_kcal = StringVar()
        self.var_product_kj = StringVar()
        self.var_product_sugar = StringVar()
        self.var_product_brand = StringVar()

        self.product_id = None
        self.product_name = None
        self.product_store = None
        self.product_nutriscore = None
        self.product_img_url = None
        self.product_kcal = 0
        self.product_kj = 0
        self.product_sugar = 0
        self.product_brand = None

        # Widgets row 0
        self.w_title = None
        # Widgets row 1
        self.w_product_name_label = None
        self.w_product_name_entry = None
        # Widgets row 2
        self.w_product_store_label = None
        self.w_product_store_entry = None
        # Widgets row 3
        self.w_product_nutriscore_label = None
        self.w_product_nutriscore_entry = None
        # Widgets row 4
        self.w_product_imgurl_label = None
        self.w_product_imgurl_entry = None
        # Widgets row 5
        self.w_product_kcal_label = None
        self.w_product_kcal_entry = None
        # Widgets row 6
        self.w_product_kj_label = None
        self.w_product_kj_entry = None
        # Widgets row 7
        self.w_product_sugar_label = None
        self.w_product_sugar_entry = None
        # Widgets row 8
        self.w_product_brand_label = None
        self.w_product_brand_entry = None
        # Widgets row 9
        self.w_submit_button = None

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
        self.row_8(action="construct")
        self.row_9(action="construct")

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
            file_name="edit"
        )

        # 2. Save name of view for displayer.
        self.name = self.json_script.get("view_name")

        # Get product informations
        self.product = self.session.dbmanager.db_product.read(
            action="id",
            product_id=self.product_id
        )

        self.product_img = self.product[0]["product_img_url"]
        self.product_name = self.product[0]["product_name"]
        self.product_brand = self.product[0]["product_brand"]
        self.product_nutriscore = self.product[0]["product_nutriscore"]
        self.product_img_url = self.product[0]["product_img_url"]
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
            self.row_8(action="refresh")
            self.row_9(action="refresh")

        # 3. Fill the view rows.
        self.row_0(action="fill")
        self.row_1(action="fill")
        self.row_2(action="fill")
        self.row_3(action="fill")
        self.row_4(action="fill")
        self.row_5(action="fill")
        self.row_6(action="fill")
        self.row_7(action="fill")
        self.row_8(action="fill")
        self.row_9(action="fill")
        self.fill_status = True

    def display_previous(self):
        """ Display previous view. """

        self.displayer.display(
            c_view="product_edit",
            f_view=self.previous_view
        )

    def display_product_sheet(self):
        """ Display "product sheet". """

        self.displayer.display(
            c_view="product_edit",
            f_view="product_sheet",
            product_id=self.product_id
        )

    def update_product(self):
        """ Update product in database. """

        self.product_name = self.var_product_name.get()
        self.product_store = self.var_product_store.get()
        self.product_nutriscore = self.var_product_nutriscore.get()
        self.product_img_url = self.var_product_img_url.get()
        self.product_kcal = int(self.var_product_kcal.get())
        self.product_kj = int(self.var_product_kj.get())
        self.product_sugar = int(self.var_product_sugar.get())
        self.product_brand = self.var_product_brand.get()

        self.session.dbmanager.db_product.update(
            product_id=self.product_id,
            product_name=self.product_name,
            product_store=self.product_store,
            product_nutriscore=self.product_nutriscore,
            product_img_url=self.product_img_url,
            product_kcal=self.product_kcal,
            product_kj=self.product_kj,
            product_sugar=self.product_sugar,
            product_brand=self.product_brand
        )

        self.display_product_sheet()

    def row_0(self, action=None):
        """ Name : TITLE
            cols : 1 """

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

            # -- COLUMN 1/1 : TITLE -- #
            if self.w_title is None:
                self.w_title = Label(
                    self.grid.col_frames[0][0],
                    text=txt.get("view_title"),
                    bg="#ffffff",
                    fg="#000000",
                    font="Helvetica 12 bold"
                )
                self.w_title.pack(fill="both", expand=True)

        elif action == "refresh":

            self.w_title.pack_forget()
            self.w_title = None

    def row_1(self, action=None):
        """ Name : PRODUCT NAME
            cols : 3 """

        if action == "construct":

            # -- CREATE ROW -- #
            self.grid.row(
                width=self.width,
                height=50,
                padx=self.padx,
                pady=self.pady,
                bg="#ffffff"
            )
            # -- CREATE COLS -- #
            self.grid.column(
                span=3,
                row=1,
                width=None,
                height=None,
                padx=None,
                pady=None,
                bg=None
            )
            self.grid.column(
                span=7,
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

            if self.w_product_name_label is None:
                # -- COLUMN 1 : PRODUCT NAME LABEL -- #
                self.w_product_name_label = Label(
                    self.grid.col_frames[1][0],
                    anchor="w",
                    text=txt.get("product_name"),
                    bg="#ffffff"
                )
                self.w_product_name_label.pack(fill="both", expand=True)

            if self.w_product_name_entry is None:
                # -- COLUMN 2 : PRODUCT NAME ENTRY -- #
                self.w_product_name_entry = Entry(
                    self.grid.col_frames[1][1],
                    textvariable=self.var_product_name
                )
                self.w_product_name_entry.insert(0, self.product_name)
                self.w_product_name_entry.pack(fill="both", expand=True)

        elif action == "refresh":

            self.w_product_name_label.pack_forget()
            self.w_product_name_entry.delete(0, 1000)
            self.w_product_name_entry.pack_forget()

            self.w_product_name_label = None
            self.w_product_name_entry = None

    def row_2(self, action=None):
        """ Name : PRODUCT STORES
            cols : 3 """

        if action == "construct":

            # -- CREATE ROW -- #
            self.grid.row(
                width=self.width,
                height=50,
                padx=self.padx,
                pady=self.pady,
                bg="#ffffff"
            )
            # -- CREATE COLS -- #
            self.grid.column(
                span=3,
                row=2,
                width=None,
                height=None,
                padx=None,
                pady=None,
                bg=None
            )
            self.grid.column(
                span=7,
                row=2,
                width=None,
                height=None,
                padx=None,
                pady=None,
                bg=None
            )
            self.grid.column(
                span=2,
                row=2,
                width=None,
                height=None,
                padx=None,
                pady=None,
                bg=None
            )

        elif action == "fill":

            # Get texts for this row
            txt = self.json_script.get("row_2")

            if self.w_product_store_label is None:
                # -- COLUMN 1 : PRODUCT STORES LABEL -- #
                self.w_product_store_label = Label(
                    self.grid.col_frames[2][0],
                    anchor="w",
                    text=txt.get("product_stores"),
                    bg="#ffffff"
                )
                self.w_product_store_label.pack(fill="both", expand=True)

            if self.w_product_store_entry is None:
                # -- COLUMN 2 : PRODUCT STORES ENTRY -- #
                self.w_product_store_entry = Entry(
                    self.grid.col_frames[2][1],
                    textvariable=self.var_product_store
                )
                self.w_product_store_entry.insert(0, self.product_store)
                self.w_product_store_entry.pack(fill="both", expand=True)

        elif action == "refresh":

            self.w_product_store_label.pack_forget()
            self.w_product_store_entry.delete(0, 1000)
            self.w_product_store_entry.pack_forget()

            self.w_product_store_label = None
            self.w_product_store_entry = None

    def row_3(self, action=None):
        """ Name : PRODUCT NUTRISCORE
            cols : 3 """

        if action == "construct":

            # -- CREATE ROW -- #
            self.grid.row(
                width=self.width,
                height=50,
                padx=self.padx,
                pady=self.pady,
                bg="#ffffff"
            )
            # -- CREATE COLS -- #
            self.grid.column(
                span=3,
                row=3,
                width=None,
                height=None,
                padx=None,
                pady=None,
                bg=None
            )
            self.grid.column(
                span=7,
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

        elif action == "fill":

            # Get texts for this row
            txt = self.json_script.get("row_3")

            if self.w_product_nutriscore_label is None:
                # -- COLUMN 1 : PRODUCT NUTRISCORE LABEL -- #
                self.w_product_nutriscore_label = Label(
                    self.grid.col_frames[3][0],
                    anchor="w",
                    text=txt.get("product_nutriscore"),
                    bg="#ffffff"
                )
                self.w_product_nutriscore_label.pack(
                    fill="both",
                    expand=True
                )

            if self.w_product_nutriscore_entry is None:
                # -- COLUMN 2 : PRODUCT NUTRISCORE ENTRY -- #
                self.w_product_nutriscore_entry = Entry(
                    self.grid.col_frames[3][1],
                    textvariable=self.var_product_nutriscore
                )
                self.w_product_nutriscore_entry.insert(
                    0,
                    self.product_nutriscore
                )
                self.w_product_nutriscore_entry.pack(
                    fill="both",
                    expand=True
                )

        elif action == "refresh":

            self.w_product_nutriscore_label.pack_forget()
            self.w_product_nutriscore_entry.delete(0, 1000)
            self.w_product_nutriscore_entry.pack_forget()

            self.w_product_nutriscore_label = None
            self.w_product_nutriscore_entry = None

    def row_4(self, action=None):
        """ Name : PRODUCT IMAGE URL
            cols : 1 """

        if action == "construct":

            # -- CREATE ROW -- #
            self.grid.row(
                width=self.width,
                height=50,
                padx=self.padx,
                pady=self.pady,
                bg="#ffffff"
            )
            # -- CREATE COLS -- #
            self.grid.column(
                span=3,
                row=4,
                width=None,
                height=None,
                padx=None,
                pady=None,
                bg=None
            )
            self.grid.column(
                span=7,
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

        elif action == "fill":

            # Get texts for this row
            txt = self.json_script.get("row_4")

            if self.w_product_imgurl_label is None:
                # -- COLUMN 1 : PRODUCT IMAGE URL LABEL -- #
                self.w_product_imgurl_label = Label(
                    self.grid.col_frames[4][0],
                    anchor="w",
                    text=txt.get("product_img_url"),
                    bg="#ffffff"
                )
                self.w_product_imgurl_label.pack(fill="both", expand=True)

            if self.w_product_imgurl_entry is None:
                # -- COLUMN 2 : PRODUCT IMAGE URL ENTRY -- #
                self.w_product_imgurl_entry = Entry(
                    self.grid.col_frames[4][1],
                    textvariable=self.var_product_img_url
                )
                self.w_product_imgurl_entry.insert(0, self.product_img_url)
                self.w_product_imgurl_entry.pack(fill="both", expand=True)

        elif action == "refresh":

            self.w_product_imgurl_label.pack_forget()
            self.w_product_imgurl_entry.delete(0, 1000)
            self.w_product_imgurl_entry.pack_forget()

            self.w_product_imgurl_label = None
            self.w_product_imgurl_entry = None

    def row_5(self, action=None):
        """ Name : PRODUCT KCAL
            cols : 3 """

        if action == "construct":

            # -- CREATE ROW -- #
            self.grid.row(
                width=self.width,
                height=50,
                padx=self.padx,
                pady=self.pady,
                bg="#ffffff"
            )
            # -- CREATE COLS -- #
            self.grid.column(
                span=3,
                row=5,
                width=None,
                height=None,
                padx=None,
                pady=None,
                bg=None
            )
            self.grid.column(
                span=7,
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

        elif action == "fill":

            # Get texts for this row
            txt = self.json_script.get("row_5")

            if self.w_product_kcal_label is None:
                # -- COLUMN 1 : PRODUCT KCAL LABEL -- #
                self.w_product_kcal_label = Label(
                    self.grid.col_frames[5][0],
                    anchor="w",
                    text=txt.get("product_kcal"),
                    bg="#ffffff"
                )
                self.w_product_kcal_label.pack(fill="both", expand=True)

            if self.w_product_kcal_entry is None:
                # -- COLUMN 2 : PRODUCT KCAL ENTRY -- #
                self.w_product_kcal_entry = Entry(
                    self.grid.col_frames[5][1],
                    textvariable=self.var_product_kcal
                )
                self.w_product_kcal_entry.insert(0, self.product_kcal)
                self.w_product_kcal_entry.pack(fill="both", expand=True)

        elif action == "refresh":

            self.w_product_kcal_label.pack_forget()
            self.w_product_kcal_entry.delete(0, 1000)
            self.w_product_kcal_entry.pack_forget()

            self.w_product_kcal_label = None
            self.w_product_kcal_entry = None

    def row_6(self, action=None):
        """ Name : PRODUCT KJ
            cols : 3 """

        if action == "construct":

            # -- CREATE ROW -- #
            self.grid.row(
                width=self.width,
                height=50,
                padx=self.padx,
                pady=self.pady,
                bg="#ffffff"
            )
            # -- CREATE COLS -- #
            self.grid.column(
                span=3,
                row=6,
                width=None,
                height=None,
                padx=None,
                pady=None,
                bg=None
            )
            self.grid.column(
                span=7,
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

        elif action == "fill":

            # Get texts for this row
            txt = self.json_script.get("row_6")

            if self.w_product_kj_label is None:
                # -- COLUMN 1 : PRODUCT KJ LABEL -- #
                self.w_product_kj_label = Label(
                    self.grid.col_frames[6][0],
                    anchor="w",
                    text=txt.get("product_kj"),
                    bg="#ffffff"
                )
                self.w_product_kj_label.pack(fill="both", expand=True)

            if self.w_product_kj_entry is None:
                # -- COLUMN 2 : PRODUCT KJ ENTRY -- #
                self.w_product_kj_entry = Entry(
                    self.grid.col_frames[6][1],
                    textvariable=self.var_product_kj
                )
                self.w_product_kj_entry.insert(0, self.product_kj)
                self.w_product_kj_entry.pack(fill="both", expand=True)

        elif action == "refresh":

            self.w_product_kj_label.pack_forget()
            self.w_product_kj_entry.delete(0, 1000)
            self.w_product_kj_entry.pack_forget()

            self.w_product_kj_label = None
            self.w_product_kj_entry = None

    def row_7(self, action=None):
        """ Name : PRODUCT SUGAR
            cols : 3 """

        if action == "construct":

            # -- CREATE ROW -- #
            self.grid.row(
                width=self.width,
                height=50,
                padx=self.padx,
                pady=self.pady,
                bg="#ffffff"
            )
            # -- CREATE COLS -- #
            self.grid.column(
                span=3,
                row=7,
                width=None,
                height=None,
                padx=None,
                pady=None,
                bg=None
            )
            self.grid.column(
                span=7,
                row=7,
                width=None,
                height=None,
                padx=None,
                pady=None,
                bg=None
            )
            self.grid.column(
                span=2,
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

            if self.w_product_sugar_label is None:
                # -- COLUMN 1 : PRODUCT SUGAR LABEL -- #
                self.w_product_sugar_label = Label(
                    self.grid.col_frames[7][0],
                    anchor="w",
                    text=txt.get("product_sugar"),
                    bg="#ffffff"
                )
                self.w_product_sugar_label.pack(fill="both", expand=True)

            if self.w_product_sugar_entry is None:
                # -- COLUMN 2 : PRODUCT SUGAR ENTRY -- #
                self.w_product_sugar_entry = Entry(
                    self.grid.col_frames[7][1],
                    textvariable=self.var_product_sugar
                )
                self.w_product_sugar_entry.insert(0, self.product_sugar)
                self.w_product_sugar_entry.pack(fill="both", expand=True)

        elif action == "refresh":

            self.w_product_sugar_entry.delete(0, 1000)
            self.w_product_sugar_entry.pack_forget()
            self.w_product_sugar_label.pack_forget()
            self.w_product_sugar_label = None
            self.w_product_sugar_entry = None

    def row_8(self, action=None):
        """ Name : PRODUCT BRAND
            cols : 3 """

        if action == "construct":

            # -- CREATE ROW -- #
            self.grid.row(
                width=self.width,
                height=50,
                padx=self.padx,
                pady=self.pady,
                bg="#ffffff"
            )
            # -- CREATE COLS -- #
            self.grid.column(
                span=3,
                row=8,
                width=None,
                height=None,
                padx=None,
                pady=None,
                bg=None
            )
            self.grid.column(
                span=7,
                row=8,
                width=None,
                height=None,
                padx=None,
                pady=None,
                bg=None
            )
            self.grid.column(
                span=2,
                row=8,
                width=None,
                height=None,
                padx=None,
                pady=None,
                bg=None
            )

        elif action == "fill":

            # Get texts for this row
            txt = self.json_script.get("row_8")

            if self.w_product_brand_label is None:
                # -- COLUMN 1 : PRODUCT BRAND LABEL -- #
                self.w_product_brand_label = Label(
                    self.grid.col_frames[8][0],
                    anchor="w",
                    text=txt.get("product_brand"),
                    bg="#ffffff"
                )
                self.w_product_brand_label.pack(fill="both", expand=True)

            if self.w_product_brand_entry is None:
                # -- COLUMN 2 : PRODUCT BRAND ENTRY -- #
                self.w_product_brand_entry = Entry(
                    self.grid.col_frames[8][1],
                    textvariable=self.var_product_brand
                )
                self.w_product_brand_entry.insert(0, self.product_brand)
                self.w_product_brand_entry.pack(fill="both", expand=True)

        elif action == "refresh":

            self.w_product_brand_label.pack_forget()
            self.w_product_brand_entry.delete(0, 1000)
            self.w_product_brand_entry.pack_forget()

            self.w_product_brand_label = None
            self.w_product_brand_entry = None

    def row_9(self, action=None):
        """ Name : SUBMIT BUTTON
            cols : 3 """

        if action == "construct":

            # -- CREATE ROW -- #
            self.grid.row(
                width=self.width,
                height=50,
                padx=self.padx,
                pady=self.pady,
                bg="#ffffff"
            )
            # -- CREATE COLS -- #
            self.grid.column(
                span=4,
                row=9,
                width=None,
                height=None,
                padx=None,
                pady=None,
                bg=None
            )
            self.grid.column(
                span=4,
                row=9,
                width=None,
                height=None,
                padx=None,
                pady=None,
                bg=None
            )
            self.grid.column(
                span=4,
                row=9,
                width=None,
                height=None,
                padx=None,
                pady=None,
                bg=None
            )

        elif action == "fill":

            # Get texts for this row
            txt = self.json_script.get("row_9")

            if self.w_submit_button is None:
                # -- COLUMN 1 : SUBMIT BUTTON -- #
                self.w_submit_button = Button(
                    self.grid.col_frames[9][1],
                    text=txt.get("submit_button"),
                    fg="#ffffff",
                    bg="#7A57EC",
                    activeforeground="#ffffff",
                    activebackground="#845EFF",
                    command=self.update_product
                )
                self.w_submit_button.pack(side=BOTTOM, fill=X)

        elif action == "refresh":

            self.w_submit_button.pack_forget()
            self.w_submit_button = None
