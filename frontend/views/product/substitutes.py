""" PRODUCT SUBSTITUTES
PACKAGE 'PRODUCT'. """

# -*- coding: utf-8 -*-
# From Python 3
import requests
from io import BytesIO
# From Tkinter
from tkinter import StringVar, IntVar, PhotoImage
from tkinter import BOTTOM, X
from tkinter import Label, Button, Radiobutton
# From Pillow
from PIL import Image, ImageTk
# From Program
from frontend.framework.grid import Grid


class ProductSubstitutes():
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
        self.var_product_id = IntVar()

        # Widgets row 0
        self.w_title = None
        self.w_spot_left = None
        self.w_product_img = None
        self.w_product_name = None
        self.w_product_brand = None
        self.w_spot_right = None
        # Widgets row 1
        self.var_paging_label = StringVar()
        self.w_paging_txt = None
        self.w_paging_previous = None
        self.w_paging_next = None
        # Widgets row 2
        self.w_product_imgs = []
        self.w_product_names = []
        self.w_product_radios = []
        # Widgets row 3

        # Paging
        self.page = 0
        self.pages = 0
        self.p_start = None
        self.p_stop = None

        # Product to compare
        self.product = None

        self.substitutes_products = []
        self.paging_substitutes = None

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
            file_name="substitutes"
        )
        # 2. Save name of view for displayer.
        self.name = self.json_script.get("view_name")

        # Get products

        self.product = self.session.dbmanager.db_product.read(
                action="id",
                product_id=self.product_id
            )

        self.substitutes_products = self.session.dbmanager.db_product.read(
                action="substitutes",
                product_id=self.product_id
            )

        # Count products
        self.products_count = len(self.substitutes_products)
        self.page = 0
        self.pages = int(self.products_count / 3)
        self.paging_substitutes = self.substitutes_products[0:3]

        # 3. Refresh rows.
        if self.fill_status is True:
            self.row_0(action="refresh")
            self.row_1(action="refresh")
            self.row_2(action="refresh")
            self.row_3(action="refresh")

        # 4. Fill the view rows.
        self.row_0(action="fill")
        self.row_1(action="fill")
        self.row_2(action="fill")
        self.row_3(action="fill")
        self.fill_status = True

        if self.products_count == 0:
            self.display_error_404()
            return 1

    def display_previous(self):
        """ Display previous view. """

        self.displayer.display(
            c_view="product_substitutes",
            f_view=self.previous_view
        )

    def display_error_404(self):
        """ Display "error 404" view. """

        self.displayer.display(
            c_view="product_substitutes",
            f_view="error_404",
            page="search_engine"
        )

    def display_product_sheet(self):
        """ """

        product_id = self.var_product_id.get()

        self.displayer.display(
            c_view="product_substitutes",
            f_view="product_sheet",
            product_id=product_id
        )

    def paging(self, p_action=None):
        """ 'current_page'      (int ): Nunber of current page.
            'action'            (str ): Next or Previous
            'elements_per_page' (int ): Number of element per page.
            'list_start'        (int ):
            'list_stop'         (int ):
            'list'              (list): List to cut.
        """

        # Paging
        if p_action == "next":
            self.page = self.page + 1
        elif p_action == "previous":
            self.page = self.page - 1

        self.p_start = int(
            self.page * 6
        )
        self.p_stop = int(
            self.p_start + 6
        )

        self.paging_substitutes = self.substitutes_products[
            self.p_start:self.p_stop
        ]

        self.row_1(action="refresh")
        self.row_2(action="refresh")
        self.row_1(action="fill")
        self.row_2(action="fill")

    def paging_next(self):
        """ Paging. """

        test = self.page + 1

        if test <= self.pages:
            self.paging(
                p_action="next"
            )

    def paging_prev(self):
        """ Paging. """

        test = self.page - 1

        if test >= 0:

            self.paging(
                p_action="previous"
            )

    def row_0(self, action=None):
        """ Name : TITLE
            cols : 3 """

        if action == "construct":

            # -- CREATE ROW -- #
            self.grid.row(
                width=self.width,
                height=270,
                padx=self.padx,
                pady=self.pady,
                bg="#ffffff"
            )
            # -- CREATE COLS -- #
            self.grid.column(
                span=4,
                row=0,
                width=None,
                height=None,
                padx=None,
                pady=None,
                bg=None
            )
            self.grid.column(
                span=4,
                row=0,
                width=None,
                height=None,
                padx=None,
                pady=None,
                bg=None
            )
            self.grid.column(
                span=4,
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

            # -- COLUMN 1 : SPOTLIGHT LEFT IMAGE -- #
            img = Image.open(
                "frontend/images/views/substitutes/spotlight_left.png"
            )
            img_resize = img.resize((120, 120), Image.ANTIALIAS)
            spotlight_img = ImageTk.PhotoImage(img_resize)

            self.w_spot_left = Label(
                self.grid.col_frames[0][0],
                image=spotlight_img,
                bg="#ffffff"
            )
            self.w_spot_left.image = spotlight_img
            self.w_spot_left.pack(fill="both", expand=True)

            # -- COLUMN 2 : PRODUCT IMAGE -- #
            if self.product[0].get("product_img_url") == "empty":
                img = Image.open("frontend/images/no_image.png")
            else:
                req = requests.get(self.product[0].get("product_img_url"))
                img = Image.open(BytesIO(req.content))

            img_resize = img.resize((150, 200), Image.ANTIALIAS)
            tk_img_product = ImageTk.PhotoImage(img_resize)

            self.w_product_img = Label(
                self.grid.col_frames[0][1],
                image=tk_img_product,
                bg="#ffffff"
            )
            self.w_product_img.image = tk_img_product
            self.w_product_img.pack(fill='both', expand=True, side=BOTTOM)

            # -- COLUMN 2 : PRODUCT NAME -- #
            self.w_product_name = Label(
                self.grid.col_frames[0][1], text="{}".format(
                    self.product[0].get("product_name")
                ),
                bg="#ffffff",
                fg="#000000",
                font="Helvetica 13 normal"
            )
            self.w_product_name.pack(fill='both')

            # -- COLUMN 2 : PRODUCT BRAND -- #
            self.w_product_brand = Label(
                self.grid.col_frames[0][1],
                text="{}".format(self.product[0].get("product_brand")),
                bg="#ffffff",
                fg="#000000",
                font="Helvetica 13 bold"
            )
            self.w_product_brand.pack(fill='both')

            # -- COLUMN 1 : SPOTLIGHT LEFT IMAGE -- #
            img = Image.open(
                "frontend/images/views/substitutes/spotlight_right.png"
            )
            img_resize = img.resize((120, 120), Image.ANTIALIAS)
            spotlight_img = ImageTk.PhotoImage(img_resize)

            self.w_spot_right = Label(
                self.grid.col_frames[0][2],
                image=spotlight_img,
                bg="#ffffff"
            )
            self.w_spot_right.image = spotlight_img
            self.w_spot_right.pack(fill="both", expand=True)

        elif action == "refresh":

            self.w_spot_left.pack_forget()
            self.w_product_img.pack_forget()
            self.w_product_name.pack_forget()
            self.w_product_brand.pack_forget()
            self.w_spot_right.pack_forget()

            self.w_spot_left = None
            self.w_product_img = None
            self.w_product_name = None
            self.w_product_brand = None
            self.w_spot_right = None

    def row_1(self, action=None):
        """ Name : PAGING
            cols : 3 """

        if action == "construct":

            # -- CREATE ROW -- #
            self.grid.row(
                width=self.width,
                height=40,
                padx=self.padx,
                pady=self.pady,
                bg="#E3E9ED"
            )

            self.grid.column(
                span=9,
                row=1,
                width=None,
                height=None,
                padx=None,
                pady=None,
                bg=None
            )

            self.grid.column(
                span=1,
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

            # Get script
            txt = self.json_script.get("row_1")

            # -- COLUMN 1/3 : EMPTY -- #
            if self.w_paging_txt is None:

                self.var_paging_label.set(
                    "{} {} / {}".format(
                        txt.get("paging_label"),
                        self.page,
                        self.pages
                    )
                )
                self.w_paging_txt = Label(
                    self.grid.col_frames[1][0],
                    anchor="w",
                    pady=5,
                    padx=5,
                    textvariable=self.var_paging_label,
                    bg="#E3E9ED",
                    fg="#000000",
                    font="Helvetica 10 bold"
                )
                self.w_paging_txt.pack(fill='both', expand=True)

            # -- COLUMN 2/3 : PAGING BUTTON -- #
            if self.w_paging_previous is None:

                self.w_paging_previous = Button(
                    self.grid.col_frames[1][2],
                    text=txt.get("paging_prev"),
                    fg="#ffffff",
                    bg="#6B7379",
                    activeforeground="#ffffff",
                    activebackground="#6B7379",
                    command=self.paging_prev
                )
                self.w_paging_previous.pack(side="left", expand=True)

            # -- COLUMN 2/3 : PAGING BUTTON -- #
            if self.w_paging_next is None:

                self.w_paging_next = Button(
                    self.grid.col_frames[1][2],
                    text=txt.get("paging_next"),
                    fg="#ffffff",
                    bg="#1D262D",
                    activeforeground="#ffffff",
                    activebackground="#1D262D",
                    command=self.paging_next
                )
                self.w_paging_next.pack(side="right", expand=True)

        elif action == "refresh":

            # Get script
            txt = self.json_script.get("row_1")

            self.var_paging_label.set(
                "{} {} / {}".format(
                    txt.get("paging_label"),
                    self.page,
                    self.pages
                )
            )

    def row_2(self, action=None):
        """ Name : RESULT
            cols : 3 """

        if action == "construct":

            # -- CREATE ROW -- #
            self.grid.row(
                width=self.width,
                height=270,
                padx=self.padx,
                pady=self.pady,
                bg="#ffffff"
            )
            # -- CREATE COLS -- #
            self.grid.column(
                span=4,
                row=2,
                width=None,
                height=None,
                padx=None,
                pady=None,
                bg=None
            )
            self.grid.column(
                span=4,
                row=2,
                width=None,
                height=None,
                padx=None,
                pady=None,
                bg=None
            )
            self.grid.column(
                span=4,
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

            count = 0
            for product in self.paging_substitutes[0:3]:

                # -- COLUMN : SUBSTITUT PRODUCT IMAGE -- #
                if product.get("product_img_url") == "empty":
                    img = Image.open("frontend/images/no_image.png")
                else:
                    req = requests.get(product.get("product_img_url"))
                    img = Image.open(BytesIO(req.content))

                img_resize = img.resize((150, 200), Image.ANTIALIAS)
                tk_img_product = ImageTk.PhotoImage(img_resize)

                self.w_product_img = Label(
                    self.grid.col_frames[2][count],
                    image=tk_img_product,
                    bg="#ffffff"
                )
                self.w_product_img.image = tk_img_product
                self.w_product_img.pack(fill='both', expand=True)

                # -- COLUMN : SUBSTITUT PRODUCT LABEL -- #
                self.w_product_name = Label(
                    self.grid.col_frames[2][count],
                    text="{}".format(product.get("product_name")),
                    bg="#ffffff"
                )
                self.w_product_name.pack()

                # -- COLUMN : SUBSTITUT PRODUCT RADIO -- #
                self.w_product_radio = Radiobutton(
                    self.grid.col_frames[2][count],
                    variable=self.var_product_id,
                    value=product.get("product_id"),
                    bg="#ffffff"
                )
                self.w_product_radio.pack()

                self.w_product_imgs.append(self.w_product_img)
                self.w_product_names.append(self.w_product_name)
                self.w_product_radios.append(self.w_product_radio)

                count += 1

        elif action == "refresh":

            if len(self.w_product_imgs) > 0:
                for w_product_img in self.w_product_imgs:
                    w_product_img.pack_forget()

            if len(self.w_product_names) > 0:
                for w_product_name in self.w_product_names:
                    w_product_name.pack_forget()

            if len(self.w_product_radios) > 0:
                for w_product_radio in self.w_product_radios:
                    w_product_radio.pack_forget()

            self.w_product_imgs = []
            self.w_product_names = []
            self.w_product_radios = []

    def row_3(self, action=None):
        """ Name : SUBMIT BUTTON
            cols : 3 """

        if action == "construct":

            # -- CREATE ROW -- #
            self.grid.row(
                width=self.width,
                height=60,
                padx=self.padx,
                pady=self.pady,
                bg="#ffffff"
            )
            # -- CREATE COLS -- #
            self.grid.column(
                span=4,
                row=3,
                width=None,
                height=None,
                padx=None,
                pady=None,
                bg=None
            )
            self.grid.column(
                span=4,
                row=3,
                width=None,
                height=None,
                padx=None,
                pady=None,
                bg=None
            )
            self.grid.column(
                span=4,
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

            # -- COLUMN 1: SUBMIT BUTTON -- #
            self.w_submit_button = Button(
                self.grid.col_frames[3][1],
                text=txt.get("submit_button"),
                fg="#ffffff",
                bg="#7A57EC",
                activeforeground="#ffffff",
                activebackground="#845EFF",
                command=self.display_product_sheet
            )
            self.w_submit_button.pack(side=BOTTOM, fill=X, expand=True)

        elif action == "refresh":

            self.w_submit_button.pack_forget()
            self.w_submit_button = None
