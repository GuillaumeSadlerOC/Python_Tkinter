""" SEARCH CATEGORIES
PACKAGE 'CATEGORIES'. """

# -*- coding: utf-8 -*-
# From Python 3
# From Tkinter
from tkinter import StringVar, IntVar, PhotoImage
from tkinter import BOTTOM, X
from tkinter import Label, Button, Radiobutton
# From Pillow
from PIL import Image, ImageTk
# From Program
from frontend.framework.grid import Grid


class SearchCategories():
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
        self.var_category = IntVar()

        # Widgets row 0
        self.var_paging_label = StringVar()
        self.w_paging_txt = None
        self.w_paging_previous = None
        self.w_paging_next = None
        # Row 1
        self.w_language_flags = []
        self.w_category_names = []
        self.w_category_products = []
        self.w_category_radios = []
        # Row 2
        self.w_previous_button = None
        self.w_submit_button = None

        # Paging
        self.page = 0
        self.pages = 0
        self.p_start = None
        self.p_stop = None

        self.paging_categories = None

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

    def fill(self, **kwargs):
        """ Fill the view rows.
            'json_script'   (dict): texts for view.
            'name'          (str): view name. """

        for key, value in kwargs.items():

            if key == "view":
                self.previous_view = value

        # 1. Get the script.
        self.json_script = self.session.get_script(
            package_name="search",
            file_name="categories"
        )
        # 2. Save name of view for displayer.
        self.name = self.json_script.get("view_name")

        self.categories = self.session.dbmanager.db_category.read(
            action="*"
        )

        # Count categories
        self.categories_count = len(self.categories)
        self.page = 0
        self.pages = int(self.categories_count / 15)
        self.paging_categories = self.categories[0:15]

        # 3. Refresh rows.
        if self.fill_status is True:
            self.row_0(action="refresh")
            self.row_1(action="refresh")
            self.row_2(action="refresh")

        # 4. Fill the view rows.
        self.row_0(action="fill")
        self.row_1(action="fill")
        self.row_2(action="fill")
        self.fill_status = True

        if self.categories_count == 0:
            self.display_empty()
            return 1

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
        """ Display previous view. """

        self.displayer.display(
            c_view="search_categories",
            f_view=self.previous_view
        )

    def display_search_result(self):
        """ Display search result. """

        category_id = self.var_category.get()

        self.displayer.display(
            c_view="search_categories",
            f_view="search_result",
            search_action="cat_id",
            search_value=category_id
        )

    def display_empty(self):
        """ Display search result. """

        self.displayer.display(
            c_view="search_categories",
            f_view="empty",
            page="categories"
        )

    def row_0(self, action=None):
        """ Name : PAGING
            cols : 0 """

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
                row=0,
                width=None,
                height=None,
                padx=None,
                pady=None,
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

            self.grid.column(
                span=2,
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
                    self.grid.col_frames[0][0],
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
                    self.grid.col_frames[0][2],
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
                    self.grid.col_frames[0][2],
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
            txt = self.json_script.get("row_0")

            self.var_paging_label.set(
                "{} {} / {}".format(
                    txt.get("paging_label"),
                    self.page,
                    self.pages
                )
            )

    def row_1(self, action=None):
        """ Name : CATEGORIES
            cols : 3 """

        if action == "construct":

            # -- CREATE ROW -- #
            self.grid.row(
                width=self.width,
                height=500,
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
                pady=5,
                bg=None
            )
            self.grid.column(
                span=6,
                row=1,
                width=None,
                height=None,
                padx=None,
                pady=5,
                bg=None
            )
            self.grid.column(
                span=2,
                row=1,
                width=None,
                height=None,
                padx=None,
                pady=5,
                bg=None
            )
            self.grid.column(
                span=2,
                row=1,
                width=None,
                height=None,
                padx=None,
                pady=5,
                bg=None
            )

        elif action == "fill":

            # Get script
            txt = self.json_script.get("row_1")

            count = 0
            for category in self.paging_categories[0:15]:

                """# -- COLUMN 1/5 : CATEGORY LANGUAGE -- #
                img = Image.open(
                    "v2/frontend/resources/images/flags/{}.png"
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
                w_language_flag.pack(fill='both', expand=True)"""

                w_category_name = Label(
                    self.grid.col_frames[1][1],
                    anchor="w",
                    pady=0,
                    text=category["category_name"],
                    bg="#ffffff",
                    fg="#000000",
                    font="Helvetica 10 bold"
                )
                w_category_name.pack(fill='both', expand=True)

                w_category_product = Label(
                    self.grid.col_frames[1][2],
                    pady=0,
                    text=category["category_products"],
                    bg="#ffffff",
                    fg="#000000",
                    font="Helvetica 10 bold"
                )
                w_category_product.pack(fill='both', expand=True)

                w_category_radio = Radiobutton(
                        self.grid.col_frames[1][3],
                        variable=self.var_category,
                        value=category["category_id"],
                        bg="#ffffff"
                    )
                w_category_radio.pack(fill='both', expand=True)

                # For UX DESIGN
                if count == 0:
                    w_category_radio.select()

                count += 1
                # self.w_language_flags.append(w_language_flag)
                self.w_category_names.append(w_category_name)
                self.w_category_products.append(w_category_product)
                self.w_category_radios.append(w_category_radio)

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
            if len(self.w_category_radios) != 0:
                for tk_widget in self.w_category_radios:
                    tk_widget.pack_forget()

    def row_2(self, action=None):
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

            txt = self.json_script.get("row_2")

            # -- COLUMN 1/4 : EMPTY -- #
            # -- COLUMN 2/4 : SUBMIT BUTTON -- #
            if self.w_previous_button is None:

                self.w_previous_button = Button(
                    self.grid.col_frames[2][1],
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
                    self.grid.col_frames[2][2],
                    text=txt.get("submit_button"),
                    fg="#ffffff",
                    bg="#7A57EC",
                    activeforeground="#ffffff",
                    activebackground="#845EFF",
                    command=self.display_search_result
                )
                self.w_submit_button.pack(side=BOTTOM, fill=X)
            # -- COLUMN 3/3 : EMPTY -- #

        elif action == "refresh":
            pass
