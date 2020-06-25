""" HOME
PACKAGE 'OTHERS' """

# -*- coding: utf-8 -*-
# From Python 3
# From Tkinter
from tkinter import PhotoImage
from tkinter import X
from tkinter import Label, Button, Canvas
# From Pillow
from PIL import Image, ImageTk
# From Program
from frontend.framework.grid import Grid


class Home():
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
        self.canvas = None
        # Widgets row 1
        self.w_search_label = None
        self.w_search_button = None
        # Widgets row 2
        self.w_favorite_label = None
        self.w_favorite_button = None
        # Widgets row 3
        self.w_settings_label = None
        self.w_settings_button = None
        # Widgets row 4
        self.w_user_label = None
        self.w_user_button = None

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

    def fill(self, **kwargs):
        """ Fill the view rows.
            'json_script'   (dict): texts for view.
            'name'          (str): view name. """

        # 1. Get the script.
        self.json_script = self.session.get_script(
            package_name="others",
            file_name="home"
        )
        # 2. Save name of view for displayer.
        self.name = self.json_script.get("view_name")

        # 3. Refresh rows.
        if self.fill_status is True:
            self.row_0(action="refresh")
            self.row_1(action="refresh")
            self.row_2(action="refresh")
            self.row_3(action="refresh")
            self.row_4(action="refresh")

        # 4. Fill the view rows.
        self.row_0(action="fill")
        self.row_1(action="fill")
        self.row_2(action="fill")
        self.row_3(action="fill")
        self.row_4(action="fill")
        self.fill_status = True

    def display_previous(self):
        """ Display previous view. """

        self.displayer.display(
            c_view="home",
            f_view=self.previous_view
        )

    def display_search_engine(self):
        """ Display view "search_engine".
            Package "SEARCH". """

        self.displayer.display(
            c_view="home",
            f_view="search_engine"
        )

    def display_product_favorite(self):
        """ Display view "product_favorite".
            Package "SEARCH". """

        self.displayer.display(
            c_view="home",
            f_view="product_favorite"
        )

    def display_settings(self):
        """ Display view "settings".
            Package "OTHERS". """

        self.displayer.display(
            c_view="home",
            f_view="settings"
        )

    def display_user_profil(self):
        """ Display view "user_profil".
            Package "USER". """

        self.displayer.display(
            c_view="home",
            f_view="user_profil"
        )

    def row_0(self, action=None):
        """ Name : TITLE
            cols : 1 """

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
                        "frontend/images/views/home/background.jpg"
                    )
                imgResize = img.resize((640, 500), Image.ANTIALIAS)
                imgTkinter = ImageTk.PhotoImage(imgResize)

                self.canvas = Canvas(
                    self.grid.col_frames[0][0],
                    width=self.width,
                    height=250,
                    highlightthickness=0
                    )
                self.canvas.pack(expand=True, fill="both")

                self.canvas.create_image(0, 0, image=imgTkinter, anchor="nw")
                self.canvas.image = imgTkinter

                self.canvas.create_text(
                    120,
                    100,
                    text=txt.get("view_title"),
                    anchor='nw',
                    fill="#ffffff",
                    font="Helvetica 20 bold"
                )

        elif action == "refresh":
            """ Refresh this row. """

            self.canvas.delete("all")
            self.canvas.pack_forget()
            self.canvas = None

    def row_1(self, action=None):
        """ Name : SEARCH
            cols : 4 """

        if action == "construct":

            # -- CREATE ROW -- #
            self.grid.row(
                width=self.width,
                height=100,
                padx=self.padx,
                pady=self.pady,
                bg="#84dbff"
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
                span=6,
                row=1,
                width=None,
                height=None,
                padx=None,
                pady=None,
                bg=None
            )
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
                span=1,
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

            if self.w_search_label is None:
                # -- COLUMN 1 : IMAGE SEARCH -- #
                img = Image.open("frontend/images/views/home/search.png")
                img_resize = img.resize((70, 70), Image.ANTIALIAS)
                search_img = ImageTk.PhotoImage(img_resize)
                self.w_search_label = Label(
                    self.grid.col_frames[1][0],
                    image=search_img,
                    bg="#84dbff"
                )
                self.w_search_label.image = search_img
                self.w_search_label.pack(fill="both", expand=True)

            if self.w_search_button is None:
                # -- COLUMN 2 : SEARCH BUTTON -- #
                self.w_search_button = Button(
                    self.grid.col_frames[1][2],
                    text=txt.get("button"),
                    fg="#000000",
                    bg="#ededed",
                    activeforeground="#000000",
                    activebackground="#ffffff",
                    borderwidth=0,
                    command=self.display_search_engine
                )
                self.w_search_button.pack(fill="x", expand=True)

        elif action == "refresh":
            """ Refresh this row. """

            self.w_search_label.pack_forget()
            self.w_search_button.pack_forget()

            self.w_search_label = None
            self.w_search_button = None

    def row_2(self, action=None):
        """ Name : FAVORITE PRODUCT
            cols : 4 """

        if action == "construct":

            # -- CREATE ROW -- #
            self.grid.row(
                width=self.width,
                height=100,
                padx=self.padx,
                pady=self.pady,
                bg="#26b16b"
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
                span=6,
                row=2,
                width=None,
                height=None,
                padx=None,
                pady=None,
                bg=None
            )
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
                span=1,
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

            if self.w_favorite_label is None:
                # -- COLUMN 1 : IMAGE FAVORITE -- #
                img = Image.open("frontend/images/views/home/favorite.png")
                img_resize = img.resize((70, 70), Image.ANTIALIAS)
                favorite_img = ImageTk.PhotoImage(img_resize)
                self.w_favorite_label = Label(
                    self.grid.col_frames[2][0],
                    image=favorite_img,
                    bg="#26b16b"
                )
                self.w_favorite_label.image = favorite_img
                self.w_favorite_label.pack(fill="both", expand=True)

            if self.w_favorite_button is None:
                # -- COLUMN 2 : SEARCH BUTTON -- #
                self.w_favorite_button = Button(
                    self.grid.col_frames[2][2],
                    text=txt.get("button"),
                    fg="#000000",
                    bg="#ededed",
                    activeforeground="#000000",
                    activebackground="#ffffff",
                    borderwidth=0,
                    command=self.display_product_favorite
                )
                self.w_favorite_button.pack(fill="x", expand=True)

        elif action == "refresh":

            self.w_favorite_label.pack_forget()
            self.w_favorite_button.pack_forget()

            self.w_favorite_label = None
            self.w_favorite_button = None

    def row_3(self, action=None):
        """ Name : UPDATE
            cols : 4 """

        if action == "construct":

            # -- CREATE ROW -- #
            self.grid.row(
                width=self.width,
                height=100,
                padx=self.padx,
                pady=self.pady,
                bg="#ffe399"
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
                span=6,
                row=3,
                width=None,
                height=None,
                padx=None,
                pady=None,
                bg=None
            )
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
                span=1,
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

            if self.w_settings_label is None:
                # -- COLUMN 1 : SETTINGS IMAGE -- #
                img = Image.open("frontend/images/views/home/settings.png")
                img_resize = img.resize((70, 70), Image.ANTIALIAS)
                settings_img = ImageTk.PhotoImage(img_resize)
                self.w_settings_label = Label(
                    self.grid.col_frames[3][0],
                    image=settings_img,
                    bg="#ffe399"
                )
                self.w_settings_label.image = settings_img
                self.w_settings_label.pack(fill="both", expand=True)

            if self.w_settings_button is None:
                # -- COLUMN 2 : SETTINGS BUTTON -- #
                self.w_settings_button = Button(
                    self.grid.col_frames[3][2],
                    text=txt.get("button"),
                    fg="#000000",
                    bg="#ededed",
                    activeforeground="#000000",
                    activebackground="#ffffff",
                    borderwidth=0,
                    command=self.display_settings
                )
                self.w_settings_button.pack(fill="x", expand=True)

        elif action == "refresh":

            self.w_settings_label.pack_forget()
            self.w_settings_button.pack_forget()

            self.w_settings_label = None
            self.w_settings_button = None

    def row_4(self, action=None):
        """ Name : USER PROFIL
            cols : 4 """

        if action == "construct":

            # -- CREATE ROW -- #
            self.grid.row(
                width=self.width,
                height=100,
                padx=self.padx,
                pady=self.pady,
                bg="#ff4347"
            )
            # -- CREATE COLS -- #
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
                span=6,
                row=4,
                width=None,
                height=None,
                padx=None,
                pady=None,
                bg=None
            )
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
                span=1,
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

            if self.w_user_label is None:
                # -- COLUMN 1 : IMAGE USER -- #
                img = Image.open("frontend/images/views/home/user.png")
                img_resize = img.resize((70, 70), Image.ANTIALIAS)
                user_img = ImageTk.PhotoImage(img_resize)
                self.w_user_label = Label(
                    self.grid.col_frames[4][0],
                    image=user_img,
                    bg="#ff4347"
                )
                self.w_user_label.image = user_img
                self.w_user_label.pack(fill="both", expand=True)

            if self.w_user_button is None:
                # -- COLUMN 2 : USER BUTTON -- #
                self.w_user_button = Button(
                    self.grid.col_frames[4][2],
                    text=txt.get("button"),
                    fg="#000000",
                    bg="#ededed",
                    activeforeground="#000000",
                    activebackground="#ffffff",
                    anchor="w",
                    borderwidth=0,
                    command=self.display_user_profil
                )
                self.w_user_button.pack(fill="x", expand=True)

        elif action == "refresh":

            self.w_user_label.pack_forget()
            self.w_user_button.pack_forget()

            self.w_user_label = None
            self.w_user_button = None
