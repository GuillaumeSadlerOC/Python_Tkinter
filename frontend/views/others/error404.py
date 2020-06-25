""" ERROR 404
PACKAGE 'OTHER'. """

# -*- coding: utf-8 -*-
# From Python 3
# From Tkinter
from tkinter import PhotoImage
from tkinter import Label, Button
# From Pillow
from PIL import Image, ImageTk
# From Program
from frontend.framework.grid import Grid


class Error404():
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
        self.w_error404_img = None
        self.w_error404_button = None

        self.page_to_display = None

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

    def fill(self, **kwargs):
        """ Fill the view rows.
            'json_script'   (dict): texts for view.
            'name'          (str): view name. """

        for key, value in kwargs.items():

            if key == "view":
                self.previous_view = value
            elif key == "page":
                self.page_to_display = value

        # 1. Get the script.
        self.json_script = self.session.get_script(
            package_name="others",
            file_name="error404"
        )
        # 2. Save name of view for displayer.
        self.name = self.json_script.get("view_name")

        # 3. Refresh rows.
        if self.fill_status is True:
            self.row_0(action="refresh")

        # 3. Fill the view rows.
        self.row_0(action="fill")

        self.fill_status = True

    def display_page(self):
        """ Display previous view. """

        self.displayer.display(
            c_view="error_404",
            f_view=self.page_to_display
        )

    def row_0(self, action=None):
        """ Name : ERROR
            cols : 0 """

        if action == "construct":

            # -- CREATE ROW -- #
            self.grid.row(
                width=self.width,
                height=500,
                padx=self.padx,
                pady=self.pady,
                bg="#ffffff"
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

            self.grid.column(
                span=8,
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

            # -- COLUMN 2/3 : ERROR 404 IMG -- #
            if self.w_error404_img is None:

                img = Image.open(
                    "frontend/images/views/search/error_404.png"
                )
                imgResize = img.resize((300, 300), Image.ANTIALIAS)
                imgTkinter = ImageTk.PhotoImage(imgResize)

                self.w_error404_img = Label(
                    self.grid.col_frames[0][1],
                    image=imgTkinter,
                    borderwidth=5,
                    bg="#ffffff"
                )
                self.w_error404_img.image = imgTkinter
                self.w_error404_img.pack(fill="both", expand=True)

            # -- COLUMN 3/3 : ERROR 404 IMG -- #
            if self.w_error404_button is None:

                self.w_error404_button = Button(
                    self.grid.col_frames[0][1],
                    text=txt.get("error_button"),
                    fg="#ffffff",
                    bg="#6B7379",
                    activeforeground="#ffffff",
                    activebackground="#6B7379",
                    command=self.display_page
                )
                self.w_error404_button.pack(expand=True)

        elif action == "refresh":

            self.w_error404_img.pack_forget()
            self.w_error404_button.pack_forget()
            self.w_error404_img = None
            self.w_error404_button = None
