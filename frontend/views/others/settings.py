""" SETTINGS
PACKAGE 'OTHERS' """

# -*- coding: utf-8 -*-
# From Python 3
import sys
# From Tkinter
from tkinter import BOTTOM, X
from tkinter import Label, Button, Canvas
# From Pillow
from PIL import Image, ImageTk
# From Program
from frontend.framework.grid import Grid


class Settings():
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
        self.w_delete_title = None
        self.w_delete_button = None

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

    def fill(self, **kwargs):
        """ Fill the view rows.
            'json_script'   (dict): texts for view.
            'name'          (str): view name. """

        # 1. Get the script.
        self.json_script = self.session.get_script(
            package_name="others",
            file_name="settings"
        )
        # 2. Save name of view for displayer.
        self.name = self.json_script.get("view_name")

        # 3. Refresh rows.
        if self.fill_status is True:
            self.row_0(action="refresh")
            self.row_1(action="refresh")

        # 4. Fill the view rows.
        self.row_0(action="fill")
        self.row_1(action="fill")
        self.fill_status = True

    def delete_program(self):
        """ Delete the program. """
        self.session.dbmanager.remove()
        sys.exit()

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
                        "frontend/images/views/settings/background.jpg"
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

        elif action == "refresh":

            self.canvas.delete("all")
            self.canvas.pack_forget()
            self.canvas = None

    def row_1(self, action=None):
        """ Name : DELETE PROGRAM
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

            # -- COLUMN 1 : USER DELETE TITLE -- #
            if self.w_delete_title is None:
                self.w_delete_title = Label(
                    self.grid.col_frames[1][0],
                    padx=10,
                    anchor="w",
                    text=txt.get("delete"),
                    bg="#ffffff",
                    fg="#000000",
                    font="Helvetica 12 bold"
                )
                self.w_delete_title.pack(side=BOTTOM, fill=X)

            # -- COLUMN 2 : USER DELETE BUTTON -- #
            if self.w_delete_button is None:

                self.w_delete_button = Button(
                    self.grid.col_frames[1][1],
                    text=txt.get("delete_button"),
                    fg="#ffffff",
                    bg="#f12d32",
                    activeforeground="#ffffff",
                    activebackground="#f12d32",
                    command=self.delete_program
                )
                self.w_delete_button.pack(fill="x", side="bottom")

        elif action == "refresh":
            """ Refresh this row. """
            self.w_delete_title.pack_forget()
            self.w_delete_button.pack_forget()

            self.w_delete_title = None
            self.w_delete_button = None
