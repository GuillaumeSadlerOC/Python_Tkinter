""" USER AVATARS
PACKAGE 'USER'. """

# -*- coding: utf-8 -*-
# From Python 3
# From Tkinter
from tkinter import StringVar, PhotoImage
from tkinter import BOTTOM, X
from tkinter import Label, Button, Radiobutton
# From Pillow
from PIL import Image, ImageTk
# From Program
from frontend.framework.grid import Grid


class UserAvatars():
    def __init__(
        self,
        container=None,
        displayer=None,
        session=None
    ):
        """ 'container'     (obj  ): instance of Container.
            'displayer'     (obj  ): instance of Displayer.
            'session,'      (obj  ): instance of Session.
            'grid'          (obj  ): instance of Grid.

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
        self.var_avatar = StringVar()

        self.avatars = [
            "artist",
            "astronaut",
            "clown",
            "nurse",
            "police",
            "reporter",
            "santa",
            "scientist",
            "sheriff",
            "worker",
            "cashier",
            "doctor",
            "fireman"]
        self.avatar_name = ""

        self.w_avatar_fill = False
        # Widgets row 0
        self.w_title = None
        # widgets row 1 & 2
        self.w_img_avatars = []
        self.w_avatar_names = []
        self.w_avatar_radios = []
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

        # 1. Get the script.
        self.json_script = self.session.get_script(
            package_name="user",
            file_name="avatars"
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

        self.avatar_name = self.var_avatar.get()

        self.displayer.display(
            c_view="user_avatars",
            f_view=self.previous_view,
            avatar_name=self.avatar_name
        )

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
            pass

    def row_1(self, action=None):
        """ Name : AVATAR LIST 0 -6
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

            if self.w_avatar_fill is not True:

                # -- COLUMN 1/1 : TITLE -- #
                count = 0
                for avatar in self.avatars[0:6]:

                    # -- COLUMN 1 : AVATAR IMAGE -- #
                    img = Image.open(
                        "frontend/images/avatars/{}.png".format(
                            avatar
                        )
                    )
                    img_resize = img.resize((50, 50), Image.ANTIALIAS)
                    img_tkinter = ImageTk.PhotoImage(img_resize)

                    w_img_avatar = Label(
                        self.grid.col_frames[1][count],
                        image=img_tkinter,
                        borderwidth=0,
                        bg="#ffffff"
                    )
                    w_img_avatar.image = img_tkinter
                    w_img_avatar.pack(fill='both', expand=True)

                    # -- COLUMN 1 : AVATAR NAME -- #
                    w_avatar_name = Label(
                        self.grid.col_frames[1][count],
                        text=avatar,
                        bg="#ffffff"
                    )
                    w_avatar_name.pack()

                    # -- COLUMN 1 : AVATAR RADIO -- #
                    w_avatar_radio = Radiobutton(
                        self.grid.col_frames[1][count],
                        variable=self.var_avatar,
                        value=avatar,
                        bg="#ffffff"
                    )
                    w_avatar_radio.pack()

                    if count == 0:
                        w_avatar_radio.select()

                    self.w_img_avatars.append(w_img_avatar)
                    self.w_avatar_names.append(w_avatar_name)
                    self.w_avatar_radios.append(w_avatar_radio)
                    count += 1

        elif action == "refresh":
            pass

    def row_2(self, action=None):
        """ Name : AVATAR LIST 6 - 12
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
                span=2,
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

            if self.w_avatar_fill is not True:

                # -- COLUMN 1/1 : TITLE -- #
                count = 0
                for avatar in self.avatars[6:12]:

                    # -- COLUMN 1 : AVATAR IMAGE -- #
                    img = Image.open(
                        "frontend/images/avatars/{}.png".format(
                            avatar
                        )
                    )
                    img_resize = img.resize((50, 50), Image.ANTIALIAS)
                    img_tkinter = ImageTk.PhotoImage(img_resize)

                    w_img_avatar = Label(
                        self.grid.col_frames[2][count],
                        image=img_tkinter,
                        borderwidth=0,
                        bg="#ffffff"
                    )
                    w_img_avatar.image = img_tkinter
                    w_img_avatar.pack(fill='both', expand=True)

                    # -- COLUMN 1 : AVATAR NAME -- #
                    w_avatar_name = Label(
                        self.grid.col_frames[2][count],
                        text=avatar,
                        bg="#ffffff"
                    )
                    w_avatar_name.pack()

                    # -- COLUMN 1 : AVATAR RADIO -- #
                    w_avatar_radio = Radiobutton(
                        self.grid.col_frames[2][count],
                        variable=self.var_avatar,
                        value=avatar,
                        bg="#ffffff"
                    )
                    w_avatar_radio.pack()

                    count += 1

                self.w_avatar_fill = True

        elif action == "refresh":
            pass

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
                    command=self.display_previous
                )
                self.w_submit_button.pack(side=BOTTOM, fill=X)
            # -- COLUMN 4/4 : EMPTY -- #

        elif action == "refresh":
            """ Refresh this row. """

            self.w_previous_button.pack_forget()
            self.w_submit_button.pack_forget()

            self.w_previous_button = None
            self.w_submit_button = None
