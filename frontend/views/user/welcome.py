""" USER WELCOME
PACKAGE 'USER'. """

# -*- coding: utf-8 -*-
# From Python 3
# From Tkinter
from tkinter import IntVar
from tkinter import BOTTOM, X
from tkinter import Label, Button, Radiobutton
# From Pillow
from PIL import Image, ImageTk
# From Program
from frontend.framework.grid import Grid


class UserWelcome():
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
        self.var_user_id = IntVar()

        self.w_avatars_fill = False

        # For fill this view
        self.users = None

        # Widgets row 0
        self.w_title = None
        # widgets row 1
        self.w_avatar_icons = []
        self.w_avatar_names = []
        self.w_user_radios = []
        self.w_subscribe_buttons = []
        # Widgets row 2
        self.w_avatar_button = None

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
            package_name="user",
            file_name="welcome"
        )
        # 2. Save name of view for displayer.
        self.name = self.json_script.get("view_name")

        # 3. Get users
        self.users = self.session.dbmanager.db_user.read(
            action="*"
        )

        if self.w_avatars_fill is True:
            self.row_1(action="refresh")

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

    def display_previous(self):
        """ Display previous view. """

        self.displayer.display(
            c_view="user_welcome",
            f_view=self.previous_view
        )

    def display_create_user(self):
        """ Display view user_form.
            Package "USER" """

        self.displayer.display(
            c_view="user_welcome",
            f_view="user_form",
        )

    def display_home(self):
        """ Display view user_form.
            Package "USER" """

        if len(self.users) != 0:
            self.session.user_id = self.var_user_id.get()

            self.displayer.display(
                c_view="user_welcome",
                f_view="home"
            )
        else:
            self.display_create_user()

    def row_0(self, action=None):
        """ Name : TITLE
            cols : 1 """

        if action == "construct":

            # -- CREATE ROW -- #
            self.grid.row(
                width=self.width,
                height=150,
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

            # -- COLUMN 1/1 : TITLE -- #
            if self.w_title is None:
                self.w_title = Label(
                    self.grid.col_frames[0][0],
                    padx=5,
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
        """ Name : USERS
            cols : 1 """

        if action == "construct":

            # -- CREATE ROW -- #
            self.grid.row(
                width=self.width,
                height=150,
                padx=0,
                pady=0,
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

            if self.w_avatars_fill is not True:

                # Get texts for this row
                txt = self.json_script.get("row_1")

                user_counter = 0
                free_space = 0

                while user_counter != len(self.users):

                    user = self.users[user_counter]

                    # -- COLUMN 1 : USER AVATAR IMAGE -- #
                    img = Image.open(
                        "frontend/images/avatars/{}.png".format(
                            user.get("user_avatar_name")
                        )
                    )
                    img_resize = img.resize((75, 75), Image.ANTIALIAS)
                    img_tkinter = ImageTk.PhotoImage(img_resize)

                    w_avatar_icon = Label(
                        self.grid.col_frames[1][user_counter],
                        image=img_tkinter,
                        borderwidth=0,
                        bg="#ffffff"
                        )

                    w_avatar_icon.image = img_tkinter

                    w_avatar_icon.pack(
                        fill='both',
                        expand=True
                    )

                    # -- COLUMN 1 : USER AVATAR NAME -- #
                    w_avatar_name = Label(
                        self.grid.col_frames[1][user_counter],
                        text="{}".format(user.get("user_name")),
                        anchor="n",
                        bg="#ffffff",
                        pady=10,
                        )

                    w_avatar_name.pack(fill='both', expand=True)

                    # -- COLUMN 1 : USER AVATAR RADIO -- #
                    w_user_radio = Radiobutton(
                        self.grid.col_frames[1][user_counter],
                        variable=self.var_user_id,
                        value=user.get("user_id"),
                        bg="#ffffff"
                        )

                    w_user_radio.pack(fill='both', expand=True)

                    if user_counter == 0:
                        w_user_radio.select()

                    self.w_avatar_icons.append(w_avatar_icon)
                    self.w_avatar_names.append(w_avatar_name)
                    self.w_user_radios.append(w_user_radio)

                    user_counter += 1

                free_space = 6 - user_counter

                free_counter = 0
                while free_counter != free_space:

                    # -- COLUMN 1 : USER AVATAR IMAGE -- #
                    img = Image.open(
                        "frontend/images/avatars/empty.png"
                    ).convert("RGBA")
                    img_resize = img.resize((75, 75), Image.ANTIALIAS)
                    img_tkinter = ImageTk.PhotoImage(img_resize)

                    w_avatar_icon = Label(
                        self.grid.col_frames[1][user_counter],
                        image=img_tkinter,
                        bg="#ffffff"
                        )

                    w_avatar_icon.image = img_tkinter

                    w_avatar_icon.pack(
                        fill="both",
                        expand=True
                    )

                    # -- COLUMN 1 : USER AVATAR NAME -- #
                    w_avatar_name = Label(
                        self.grid.col_frames[1][user_counter],
                        text=txt.get("user_empty"),
                        anchor="n",
                        bg="#ffffff",
                        pady=10,
                        )

                    w_avatar_name.pack(fill='both', expand=True)

                    # -- COLUMN 1 : FREE USER SUBSCRIBE BUTTON -- #
                    w_subscribe_button = Button(
                        self.grid.col_frames[1][user_counter],
                        text=txt.get("user_empty_button"),
                        borderwidth=0,
                        font="Helvetica 8 bold",
                        bg="#7dd2f0",
                        fg="#ffffff",
                        activebackground="#71bdd8",
                        activeforeground="#ffffff",
                        command=self.display_create_user
                        )

                    w_subscribe_button.pack(fill='both', expand=True)

                    self.w_avatar_icons.append(w_avatar_icon)
                    self.w_avatar_names.append(w_avatar_name)
                    self.w_subscribe_buttons.append(w_subscribe_button)

                    user_counter += 1
                    free_counter += 1

            self.w_avatars_fill = True

        elif action == "refresh":
            """ Refresh this row. """

            for w_avatar_icon in self.w_avatar_icons:
                w_avatar_icon.pack_forget()

            for w_avatar_name in self.w_avatar_names:
                w_avatar_name.pack_forget()

            for w_user_radio in self.w_user_radios:
                w_user_radio.pack_forget()

            for w_subscribe_button in self.w_subscribe_buttons:
                w_subscribe_button.pack_forget()

            self.w_subscribe_buttons = []
            self.w_avatar_icons = []
            self.w_avatar_names = []
            self.w_user_radios = []

            self.w_avatars_fill = False

    def row_2(self, action=None):
        """ Name : SUBMIT BUTTON
            cols : 3 """

        if action == "construct":

            # -- CREATE ROW -- #
            self.grid.row(
                width=self.width,
                height=225,
                padx=0,
                pady=0,
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

            if self.w_avatar_button is None:

                # -- COLUMN 1 : AVATAR BUTTON -- #
                self.w_avatar_button = Button(
                    self.grid.col_frames[2][1],
                    text=txt.get("submit_button"),
                    fg="#ffffff",
                    bg="#7A57EC",
                    activeforeground="#ffffff",
                    activebackground="#845EFF",
                    command=self.display_home
                )

                self.w_avatar_button.pack(fill="x", side="bottom", expand=True)

        elif action == "refresh":
            """ Refresh this row. """

            self.w_avatar_button.pack_forget()
            self.w_avatar_button = None
