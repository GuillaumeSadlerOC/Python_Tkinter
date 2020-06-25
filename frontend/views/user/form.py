""" USER FORM
PACKAGE 'USER'. """

# -*- coding: utf-8 -*-
# From Python 3
# From Tkinter
from tkinter import StringVar, PhotoImage
from tkinter import BOTTOM, X
from tkinter import Label, Button, Entry
# From Pillow
from PIL import Image, ImageTk
# From Program
from frontend.framework.grid import Grid


class UserForm():
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
        self.var_name = StringVar()

        self.user = None
        self.user_name = None
        self.user_avatar_name = "empty"

        # Widgets row 0
        self.w_title = None
        # Widgets row 1
        self.w_name_title = None
        self.w_name_entry = None
        # Widgets row 2
        self.w_avatar_title = None
        self.w_avatar_name = None
        self.w_user_avatar = None
        self.w_avatar_button = None
        # Widgets row 3
        self.w_previous_button = None
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

    def fill(self, **kwargs):
        """ Fill the view rows.
            'json_script'   (dict): texts for view.
            'name'          (str): view name. """

        for key, value in kwargs.items():

            if key == "view":
                self.previous_view = value
            elif key == "avatar_name":
                self.user_avatar_name = value

        # 1. Get the script.
        self.json_script = self.session.get_script(
            package_name="user",
            file_name="form"
        )
        # 2. Save name of view for displayer.
        self.name = self.json_script.get("view_name")

        # 3. Refresh rows.
        if self.fill_status is True:
            self.row_0(action="refresh")
            self.row_1(action="refresh")
            self.row_2(action="refresh")
            self.row_3(action="refresh")

        # 3. Fill the view rows.
        self.row_0(action="fill")
        self.row_1(action="fill")
        self.row_2(action="fill")
        self.row_3(action="fill")
        self.fill_status = True

    def display_previous(self):
        """ Display previous view. """

        self.displayer.display(
            c_view="user_form",
            f_view=self.previous_view
        )

    def display_avatars(self):
        """ Display view user_avatars.
            Package "USER" """

        self.displayer.display(
            c_view="user_form",
            f_view="user_avatars"
        )

    def create_user(self):
        """ Update user."""

        self.user_name = self.var_name.get()

        self.session.dbmanager.db_user.create(
            user_name=self.user_name,
            avatar_name=self.user_avatar_name
        )

        self.displayer.display(
            c_view="user_form",
            f_view="user_welcome"
        )

        self.user = None
        self.user_name = None
        self.user_avatar_name = "empty"
        self.w_name_entry.delete(0, 1000)

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
            """ Refresh this row. """

            self.w_title.pack_forget()
            self.w_title = None

    def row_1(self, action=None):
        """ Name : USER NAME
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
                row=1,
                width=None,
                height=None,
                padx=None,
                pady=None,
                bg=None
            )
            self.grid.column(
                span=4,
                row=1,
                width=None,
                height=None,
                padx=None,
                pady=None,
                bg=None
            )
            self.grid.column(
                span=5,
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

            # -- COLUMN 1/1 : TITLE -- #
            if self.w_name_title is None:

                self.w_name_title = Label(
                    self.grid.col_frames[1][0],
                    padx=10,
                    anchor="w",
                    text=txt.get("user_name"),
                    bg="#ffffff",
                    fg="#000000",
                    font="Helvetica 12 bold"
                )
                self.w_name_title.pack(side=BOTTOM, fill=X)

            if self.w_name_entry is None:

                # -- COLUMN 2 : USER NAME ENTRY -- #
                self.w_name_entry = Entry(
                    self.grid.col_frames[1][1],
                    textvariable=self.var_name
                )
                self.w_name_entry.insert(0, "")
                self.w_name_entry.pack(side=BOTTOM, fill=X)

        elif action == "refresh":
            """ Refresh this row. """

            self.w_name_title.pack_forget()
            self.w_name_entry.pack_forget()

            self.w_name_title = None
            self.w_name_entry = None

    def row_2(self, action=None):
        """ Name : USER AVATAR
            cols : 3 """

        if action == "construct":

            # -- CREATE ROW -- #
            self.grid.row(
                width=self.width,
                height=200,
                padx=0,
                pady=30,
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

        elif action == "fill":

            # Get texts for this row
            txt = self.json_script.get("row_2")

            # -- COLUMN 1 : USER AVATAR TITLE -- #
            if self.w_avatar_title is None:
                self.w_avatar_title = Label(
                    self.grid.col_frames[2][0],
                    padx=10,
                    anchor="w",
                    text=txt.get("user_avatar"),
                    bg="#ffffff",
                    fg="#000000",
                    font="Helvetica 12 bold"
                )
                self.w_avatar_title.pack(fill="both", expand=True)

            # -- COLUMN 2 : USER AVATAR IMAGE -- #
            if self.w_user_avatar is None:
                img = Image.open(
                    "frontend/images/avatars/{}.png".format(
                        self.user_avatar_name
                    )
                )
                imgResize = img.resize((90, 90), Image.ANTIALIAS)
                imgTkinter = ImageTk.PhotoImage(imgResize)
                self.w_user_avatar = Label(
                    self.grid.col_frames[2][1],
                    image=imgTkinter,
                    borderwidth=0,
                    bg="#ffffff"
                )
                self.w_user_avatar.image = imgTkinter
                self.w_user_avatar.pack(fill=X)

            # -- COLUMN 2 : USER AVATAR NAME -- #
            if self.w_avatar_name is None:
                self.w_avatar_name = Label(
                    self.grid.col_frames[2][1],
                    text="{}".format(self.user_avatar_name),
                    bg="#ffffff",
                    fg="#000000",
                    font="Helvetica 12 bold"
                )
                self.w_avatar_name.pack(fill=X)

            if self.w_avatar_button is None:

                self.w_avatar_button = Button(
                    self.grid.col_frames[2][1],
                    text=txt.get("avatars_button"),
                    fg="#ffffff",
                    bg="#1C51FF",
                    activeforeground="#ffffff",
                    activebackground="#1269FF",
                    command=self.display_avatars
                )
                self.w_avatar_button.pack()

        elif action == "refresh":
            """ Refresh this row. """

            self.w_avatar_title.pack_forget()
            self.w_user_avatar.pack_forget()
            self.w_avatar_name.pack_forget()
            self.w_avatar_button.pack_forget()

            self.w_avatar_title = None
            self.w_user_avatar = None
            self.w_avatar_name = None
            self.w_avatar_button = None

    def row_3(self, action=None):
        """ Name : SUBMIT BUTTON
            cols : 4 """

        if action == "construct":

            # -- CREATE ROW -- #
            self.grid.row(
                width=self.width,
                height=100,
                padx=0,
                pady=0,
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
                    command=self.create_user
                )
                self.w_submit_button.pack(side=BOTTOM, fill=X)
            # -- COLUMN 4/4 : EMPTY -- #

        elif action == "refresh":
            """ Refresh this row. """

            self.w_previous_button.pack_forget()
            self.w_submit_button.pack_forget()

            self.w_previous_button = None
            self.w_submit_button = None
