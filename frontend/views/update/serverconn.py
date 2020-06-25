""" UPDATE SERVER CONNECTION
PACKAGE 'UPDATE'. """

# -*- coding: utf-8 -*-
# From Python 3
# From Tkinter
from tkinter import StringVar
from tkinter import BOTTOM, X
from tkinter import Label, Button, Entry
# From Pillow
# From Program
from frontend.framework.grid import Grid


class UpdateServerConn():
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
        self.var_server_user = StringVar()
        self.var_server_pass = StringVar()
        self.var_server_host = StringVar()
        self.var_notification = StringVar()

        self.server_user = ""
        self.server_pass = ""
        self.server_host = ""

        # Widgets row 0
        self.w_title = None
        # Widgets row 1
        self.w_user_name_title = None
        self.w_user_name_entry = None
        # Widgets row 2
        self.w_server_pass_title = None
        self.w_server_pass_entry = None
        # Widgets row 3
        self.w_server_host_title = None
        self.w_server_host_entry = None
        # Widgets row 4
        self.w_submit_button = None
        # Widgets row 5
        self.w_notification = None

        # Fill status
        self.fill_status = False

        # -- Displayer initialisation -- #
        self.construct()

    def construct(self, **kwargs):
        """ Construt view. """

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

        # 3. Construct rows
        self.row_0(action="construct")
        self.row_1(action="construct")
        self.row_2(action="construct")
        self.row_3(action="construct")
        self.row_4(action="construct")
        self.row_5(action="construct")

    def fill(self, **kwargs):
        """ Fill rows. """

        # 1. Get the script.
        self.json_script = self.session.get_script(
            package_name="update",
            file_name="serverconn"
        )
        self.name = self.json_script.get("view_name")

        # 4. Kwargs recovery
        """for key, value in kwargs.items():

            if key == "display":
                self.display = value"""

        # 5. Initialisation of Tk controle variables.
        self.var_notification.set(" ")

        # 6. if we want to display the view
        if self.fill_status is True:
            self.row_0(action="refresh")
            self.row_1(action="refresh")
            self.row_2(action="refresh")
            self.row_3(action="refresh")
            self.row_4(action="refresh")
            self.row_5(action="refresh")

        self.row_0(action="fill")
        self.row_1(action="fill")
        self.row_2(action="fill")
        self.row_3(action="fill")
        self.row_4(action="fill")
        self.row_5(action="fill")
        self.fill_status = True

    def display_step_3(self):
        """ Display view 'update_languages'. """

        # 1. Informations recovery
        self.server_user = self.var_server_user.get()
        self.server_pass = self.var_server_pass.get()
        self.server_host = self.var_server_host.get()

        # 2. Check connection
        result = self.session.dbmanager.db_connection.connection(
            server_user=self.server_user,
            server_pass=self.server_pass,
            server_host=self.server_host
        )

        # 3. Get script
        txt = self.json_script.get("row_5")

        if result == 0:
            # 4. Print notification
            self.var_notification.set(txt.get("err"))
        elif result == 2:
            # 4. Display
            self.displayer.display(
                c_view="update_server_conn",
                f_view="update_languages"
            )

    def row_0(self, action=None):
        """ Name : ASSOCIATION TITLE
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

            # Get script
            txt = self.json_script.get("row_0")

            # -- ROW 2 - COLUMN 1/1 : ASSOCIATION TITLE -- #
            if self.w_title is None:

                self.w_title = Label(
                    self.grid.col_frames[0][0],
                    pady=50,
                    anchor="s",
                    text=txt.get("association_title"),
                    bg="#ffffff",
                    fg="#000000",
                    font="Helvetica 12 bold"
                )
                self.w_title.pack(fill='both', expand=True)

        elif action == "refresh":

            self.w_title.pack_forget()
            self.w_title = None

    def row_1(self, action=None):
        """ Name : USER NAME ENTRY
            cols : 3 """

        if action == "construct":

            # -- CREATE ROW -- #
            self.grid.row(
                width=self.width,
                height=40,
                padx=self.padx,
                pady=self.pady,
                bg="#ffffff"
            )
            # -- CREATE COLS -- #
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
                span=4,
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

        elif action == "fill":

            txt = self.json_script.get("row_1")

            # -- COLUMN 1/3 : SERVER NAME LABEL -- #

            if self.w_user_name_title is None:

                self.w_user_name_title = Label(
                    self.grid.col_frames[1][0],
                    padx=10,
                    anchor="w",
                    text=txt.get("server_name_user_title"),
                    bg="#ffffff",
                    fg="#000000",
                    font="Helvetica 12 bold"
                )
                self.w_user_name_title.pack(
                    fill='both',
                    expand=True
                )

            if self.w_user_name_entry is None:

                # -- COLUMN 2/3 : SERVER NAME ENTRY -- #
                self.w_user_name_entry = Entry(
                    self.grid.col_frames[1][1],
                    textvariable=self.var_server_user
                )

                self.w_user_name_entry.insert(
                    0,
                    self.server_user
                )

                self.w_user_name_entry.pack(
                    fill='both',
                    expand=True
                )
            # -- COLUMN 3/3 : EMPTY -- #

        elif action == "refresh":

            self.w_user_name_title.pack_forget()
            self.w_user_name_entry.delete(0, 1000)
            self.w_user_name_entry.pack_forget()

            self.w_user_name_title = None
            self.w_user_name_entry = None

    def row_2(self, action=None):
        """ Name : USER PASS ENTRY
            cols : 3 """

        if action == "construct":

            # -- CREATE ROW -- #
            self.grid.row(
                width=self.width,
                height=40,
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

            txt = self.json_script.get("row_2")

            # -- COLUMN 1/3 : SERVER PASS LABEL -- #
            if self.w_server_pass_title is None:

                self.w_server_pass_title = Label(
                    self.grid.col_frames[2][0],
                    padx=10,
                    anchor="w",
                    text=txt.get("server_name_pass_title"),
                    bg="#ffffff",
                    fg="#000000",
                    font="Helvetica 12 bold"
                )
                self.w_server_pass_title.pack(
                    fill='both',
                    expand=True
                )

            # -- COLUMN 2/3 : SERVER PASS ENTRY -- #
            if self.w_server_pass_entry is None:

                self.w_server_pass_entry = Entry(
                    self.grid.col_frames[2][1],
                    show="*",
                    textvariable=self.var_server_pass
                )
                self.w_server_pass_entry.insert(
                    0,
                    self.server_pass
                )
                self.w_server_pass_entry.pack(
                    fill='both',
                    expand=True
                )

            # -- COLUMN 3/3 : EMPTY -- #

        elif action == "refresh":

            self.w_server_pass_title.pack_forget()
            self.w_server_pass_entry.delete(0, 1000)
            self.w_server_pass_entry.pack_forget()

            self.w_server_pass_title = None
            self.w_server_pass_entry = None

    def row_3(self, action=None):
        """ Name : HOST ENTRY
            cols : 3 """

        if action == "construct":

            # -- CREATE ROW -- #
            self.grid.row(
                width=self.width,
                height=40,
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

            txt = self.json_script.get("row_3")

            # -- COLUMN 1/3 : HOST LABEL -- #
            if self.w_server_host_title is None:

                self.w_server_host_title = Label(
                    self.grid.col_frames[3][0],
                    padx=10,
                    anchor="w",
                    text=txt.get("server_host_title"),
                    bg="#ffffff",
                    fg="#000000",
                    font="Helvetica 12 bold"
                )
                self.w_server_host_title.pack(
                    fill='both',
                    expand=True
                )

            # -- COLUMN 2/3 : HOST ENTRY -- #
            if self.w_server_host_entry is None:

                self.w_server_host_entry = Entry(
                    self.grid.col_frames[3][1],
                    textvariable=self.var_server_host
                )
                self.w_server_host_entry.insert(
                    0,
                    self.server_host
                )
                self.w_server_host_entry.pack(
                    fill='both',
                    expand=True
                )
            # -- COLUMN 3/3 : EMPTY -- #

        elif action == "refresh":

            self.w_server_host_title.pack_forget()
            self.w_server_host_entry.delete(0, 1000)
            self.w_server_host_entry.pack_forget()

            self.w_server_host_title = None
            self.w_server_host_entry = None

    def row_4(self, action=None):
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
                row=4,
                width=None,
                height=None,
                padx=None,
                pady=None,
                bg=None
            )
            self.grid.column(
                span=4,
                row=4,
                width=None,
                height=None,
                padx=None,
                pady=None,
                bg=None
            )
            self.grid.column(
                span=4,
                row=4,
                width=None,
                height=None,
                padx=None,
                pady=None,
                bg=None
            )

        elif action == "fill":

            txt = self.json_script.get("row_4")

            # -- COLUMN 1/3 : EMPTY -- #
            # -- COLUMN 2/3 : SUBMIT BUTTON -- #
            if self.w_submit_button is None:

                self.w_submit_button = Button(
                    self.grid.col_frames[4][1],
                    text=txt.get("submit_button"),
                    fg="#ffffff",
                    bg="#7A57EC",
                    activeforeground="#ffffff",
                    activebackground="#845EFF",
                    command=self.display_step_3
                )
                self.w_submit_button.pack(side=BOTTOM, fill=X)
            # -- COLUMN 3/3 : EMPTY -- #

        elif action == "refresh":

            self.w_submit_button.pack_forget()
            self.w_submit_button = None

    def row_5(self, action=None):
        """ Name : NOTIFICATIONS
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
                span=12,
                row=5,
                width=None,
                height=None,
                padx=None,
                pady=None,
                bg=None
            )

        elif action == "fill":

            # -- COLUMN 1/1 : NOTIFICATION -- #
            if self.w_notification is None:

                self.w_notification = Label(
                    self.grid.col_frames[5][0],
                    pady=10,
                    anchor="s",
                    textvariable=self.var_notification,
                    bg="#ffffff",
                    fg="red",
                    font="Helvetica 12 bold"
                )
                self.w_notification.pack(fill='both', expand=True)

        elif action == "refresh":

            self.w_notification.pack_forget()
            self.w_notification = None
