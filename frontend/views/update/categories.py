""" UPDATE CATEGORIES
PACKAGE 'UPDATE'. """

# -*- coding: utf-8 -*-
# From Python 3
# From Tkinter
from tkinter import StringVar, IntVar
from tkinter import BOTTOM, X
from tkinter import Label, Button, Checkbutton
# From Pillow
from PIL import Image, ImageTk
# From Program
from frontend.framework.grid import Grid


class UpdateCategories():
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

        self.categories = None
        # Paging
        self.page = 0
        self.pages = 0
        self.p_start = None
        self.p_stop = None

        # Tk control variables
        self.var_notification = StringVar()
        self.var_categories = []
        self.var_paging_label = StringVar()

        # Row 0
        self.w_title = None
        # Row 1
        self.w_paging_txt = None
        self.w_paging_previous = None
        self.w_paging_next = None
        # Row 2
        self.w_language_flags = []
        self.w_category_names = []
        self.w_category_products = []
        self.w_category_checks = []
        # Row 3
        self.w_previous_button = None
        self.w_submit_button = None

        self.language = None
        self.paging_categories = None

        # Fill status
        self.fill_status = False

        # -- Displayer initialisation -- #
        self.construct()

    def construct(self, **kwargs):
        """ Construt view.
            'displayer' (Bool): to not create the view \
                during initialization. """

        # 2. Create new grid in page container.
        self.grid = Grid(
            frame=self.f_container,
            width=self.width,
            height=self.height,
            padx=self.padx,
            pady=self.pady,
            bg=self.bg
        )
        # 3. Get view frame for displayer function
        self.m_frame = self.grid.master_frame

        self.row_0(action="construct")
        self.row_1(action="construct")
        self.row_2(action="construct")
        self.row_3(action="construct")

    def fill(self, **kwargs):

        # 1. Get the script.
        self.json_script = self.session.get_script(
            package_name="update",
            file_name="categories"
        )
        self.name = self.json_script.get("view_name")

        for key, value in kwargs.items():

            if key == "language":

                self.language = value
                self.categories = self.session.off_requests(
                    req_type="categories",
                    language=self.language
                )

                # Initialization
                self.page = 0
                self.var_categories = []

                for cat in self.categories:

                    var_category_dict = {}
                    var_category = IntVar()
                    var_category_dict["var_category"] = var_category
                    var_category_dict["category_name"] = cat[
                        "category_name"
                    ]
                    var_category_dict["category_off_id"] = cat[
                        "category_off_id"
                    ]

                    self.var_categories.append(var_category_dict)

                self.pages = int(len(self.categories) / 15)
                self.paging_categories = self.categories[0:15]

            elif key == "p_action":
                self.paging(p_action=value)

        # 3. Refresh rows.
        if self.fill_status is True:
            self.row_0(action="refresh")
            self.row_1(action="refresh")
            self.row_2(action="refresh")
            self.row_3(action="refresh")

        self.row_0(action="fill")
        self.row_1(action="fill")
        self.row_2(action="fill")
        self.row_3(action="fill")
        self.fill_status = True

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
            self.page * 15
        )
        self.p_stop = int(
            self.p_start + 15
        )

        self.paging_categories = self.categories[self.p_start:self.p_stop]

        self.row_0(action="refresh")
        self.row_1(action="refresh")
        self.row_2(action="refresh")
        self.row_0(action="fill")
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

    def display_previous(self):
        """ Display view 'update_language'. """

        self.displayer.display(
            c_view="update_categories",
            f_view="update_languages"
        )

    def display_welcome(self):
        """ Display "welcome" view. """

        self.displayer.display(
            c_view="update_categories",
            f_view="user_welcome"
        )

    def upload(self):

        var_category = None
        category_name = None
        category_off_id = None

        for cat_var in self.var_categories:

            for key, value in cat_var.items():

                if key == "var_category":
                    var_category = value.get()
                elif key == "category_name":
                    category_name = value
                elif key == "category_off_id":
                    category_off_id = value

            if var_category == 1:

                self.session.dbmanager.db_category.create(
                    category_name=cat_var["category_name"],
                    category_off_id=cat_var["category_off_id"],
                    category_products=0
                )

        db_cat = self.session.dbmanager.db_category.read(
             action="*"
        )

        for cat in db_cat:

            products = self.session.dbmanager.offmanager.get_products(
                language=self.language,
                category=cat["category_id_off"]
            )

            for product in products:

                self.session.dbmanager.db_product.create(
                    product_name=product.get("product_name"),
                    product_url=product.get("product_url"),
                    product_creator=product.get("product_creator"),
                    product_stores=product.get("product_stores"),
                    product_nutriscore=product.get("product_nutriscore"),
                    product_image_url=product.get("product_image_url"),
                    product_kcal=product.get("product_kcal"),
                    product_kj=product.get("product_kj"),
                    product_category_id=cat["category_id"],
                    product_sugar=product.get("product_sugar"),
                    product_brands=product.get("product_brands")
                )

            self.session.dbmanager.db_category.update(
                category_id=cat["category_id"],
                category_products=len(products)
            )

        self.display_welcome()

    def row_0(self, action=None):
        """ Name : VIEW TITLE
            cols : 1 """

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
                span=12,
                row=0,
                width=None,
                height=None,
                padx=None,
                pady=None,
                bg=None
            )

        elif action == "fill":

            # Get script
            txt = self.json_script.get("row_0")

            # -- COLUMN 1/1 : VIEW TITLE -- #
            if self.w_title is None:

                self.w_title = Label(
                    self.grid.col_frames[0][0],
                    pady=50,
                    anchor="s",
                    text=txt.get("view_title"),
                    bg="#ffffff",
                    fg="#000000",
                    font="Helvetica 12 bold"
                )
                self.w_title.pack(fill='both', expand=True)

        elif action == "refresh":

            self.w_title.pack_forget()
            self.w_title = None

    def row_1(self, action=None):
        """ Name : PAGING
            cols : 0 """

        if action == "construct":

            # -- CREATE ROW -- #
            self.grid.row(
                width=self.width,
                height=40,
                padx=self.padx,
                pady=self.pady,
                bg="#ffffff"
            )

            self.grid.column(
                span=8,
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

            # Get script
            txt = self.json_script.get("row_1")

            # -- COLUMN 1/3 : EMPTY -- #
            if self.w_paging_txt is None:

                self.var_paging_label.set(
                    "{} {}/{}".format(
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
                    bg="#ffffff",
                    fg="#000000",
                    font="Helvetica 10 bold"
                )
                self.w_paging_txt.pack(fill='both', expand=True)

            # -- COLUMN 2/3 : PAGING BUTTON -- #
            if self.w_paging_previous is None:

                self.w_paging_previous = Button(
                    self.grid.col_frames[1][1],
                    text=txt.get("paging_prev"),
                    fg="#000000",
                    bg="#EDEDED",
                    activeforeground="#000000",
                    activebackground="#EDEDED",
                    command=self.paging_prev
                )
                self.w_paging_previous.pack(side=BOTTOM, fill=X)

            # -- COLUMN 2/3 : PAGING BUTTON -- #
            if self.w_paging_next is None:

                self.w_paging_next = Button(
                    self.grid.col_frames[1][2],
                    text=txt.get("paging_next"),
                    fg="#000000",
                    bg="#EDEDED",
                    activeforeground="#000000",
                    activebackground="#EDEDED",
                    command=self.paging_next
                )
                self.w_paging_next.pack(side=BOTTOM, fill=X)

        elif action == "refresh":

            # Get script
            txt = self.json_script.get("row_1")

            self.var_paging_label.set(
                "{} {}/{}".format(
                    txt.get("paging_label"),
                    self.page,
                    self.pages
                )
            )

            self.w_paging_txt.pack_forget()
            self.w_paging_previous.pack_forget()
            self.w_paging_next.pack_forget()

            self.w_paging_txt = None
            self.w_paging_previous = None
            self.w_paging_next = None

    def row_2(self, action=None):
        """ Name : CATEGORIES
            cols : 3 """

        if action == "construct":

            # -- CREATE ROW -- #
            self.grid.row(
                width=self.width,
                height=400,
                padx=self.padx,
                pady=self.pady,
                bg="#ffffff"
            )

            # -- CREATE COLS -- #
            col_1 = self.grid.column(
                span=2,
                row=2,
                width=None,
                height=None,
                padx=None,
                pady=5,
                bg=None
            )
            col_2 = self.grid.column(
                span=6,
                row=2,
                width=None,
                height=None,
                padx=None,
                pady=5,
                bg=None
            )
            col_3 = self.grid.column(
                span=2,
                row=2,
                width=None,
                height=None,
                padx=None,
                pady=5,
                bg=None
            )
            col_4 = self.grid.column(
                span=2,
                row=2,
                width=None,
                height=None,
                padx=None,
                pady=5,
                bg=None
            )

        elif action == "fill":

            # Get script
            txt = self.json_script.get("row_2")

            count = self.page * 15
            for category in self.paging_categories[0:15]:

                # -- COLUMN 1/5 : CATEGORY LANGUAGE -- #
                img = Image.open(
                    "frontend/images/flags/{}.png"
                    .format(category["language"])
                )
                imgResize = img.resize((20, 20), Image.ANTIALIAS)
                imgTkinter = ImageTk.PhotoImage(imgResize)

                w_language_flag = Label(
                        self.grid.col_frames[2][0],
                        image=imgTkinter,
                        borderwidth=0,
                        bg="#ffffff"
                    )
                w_language_flag.image = imgTkinter
                w_language_flag.pack(fill='both', expand=True)

                w_category_name = Label(
                    self.grid.col_frames[2][1],
                    anchor="w",
                    pady=0,
                    text=category["category_name"],
                    bg="#ffffff",
                    fg="#000000",
                    font="Helvetica 10 bold"
                )
                w_category_name.pack(fill='both', expand=True)

                w_category_product = Label(
                    self.grid.col_frames[2][2],
                    pady=0,
                    text=category["category_products"],
                    bg="#ffffff",
                    fg="#000000",
                    font="Helvetica 10 bold"
                )
                w_category_product.pack(fill='both', expand=True)

                var_cat = self.var_categories[count]["var_category"]

                w_category_check = Checkbutton(
                        self.grid.col_frames[2][3],
                        variable=var_cat,
                        bg="#ffffff"
                    )
                w_category_check.pack(fill='both', expand=True)

                self.w_language_flags.append(w_language_flag)
                self.w_category_names.append(w_category_name)
                self.w_category_products.append(w_category_product)
                self.w_category_checks.append(w_category_check)

                count += 1

        elif action == "refresh":

            if len(self.w_language_flags) != 0:
                for tk_widget in self.w_language_flags:
                    tk_widget.pack_forget()
            if len(self.w_category_names) != 0:
                for tk_widget in self.w_category_names:
                    tk_widget.pack_forget()
            if len(self.w_category_products) != 0:
                for tk_widget in self.w_category_products:
                    tk_widget.pack_forget()
            if len(self.w_category_checks) != 0:
                for tk_widget in self.w_category_checks:
                    tk_widget.pack_forget()

            self.w_language_flags = []
            self.w_category_names = []
            self.w_category_products = []
            self.w_category_checks = []

    def row_3(self, action=None):
        """ Name : SUBMIT BUTTON
            cols : 4 """

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
                span=2,
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

            txt = self.json_script.get("row_3")

            # -- COLUMN 1/4 : EMPTY -- #
            # -- COLUMN 2/4 : SUBMIT BUTTON -- #
            if self.w_previous_button is None:

                self.w_previous_button = Button(
                    self.grid.col_frames[3][1],
                    text=txt.get("previous_button"),
                    fg="#ffffff",
                    bg="#7A57EC",
                    activeforeground="#ffffff",
                    activebackground="#845EFF",
                    command=self.display_previous
                )
                self.w_previous_button.pack(side=BOTTOM, fill=X)

            # -- COLUMN 3/4 : SUBMIT BUTTON -- #
            if self.w_submit_button is None:

                self.w_submit_button = Button(
                    self.grid.col_frames[3][2],
                    text=txt.get("submit_button"),
                    fg="#ffffff",
                    bg="#7A57EC",
                    activeforeground="#ffffff",
                    activebackground="#845EFF",
                    command=self.upload
                )
                self.w_submit_button.pack(side=BOTTOM, fill=X)
            # -- COLUMN 3/3 : EMPTY -- #

        elif action == "refresh":

            self.w_previous_button.pack_forget()
            self.w_submit_button.pack_forget()

            self.w_previous_button = None
            self.w_submit_button = None
