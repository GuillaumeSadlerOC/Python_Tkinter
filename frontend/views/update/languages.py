""" UPDATE LANGUAGES
PACKAGE 'UPDATE'. """

# -*- coding: utf-8 -*-
# From Python 3
# From Tkinter
from tkinter import StringVar
from tkinter import BOTTOM, X
from tkinter import Label, Button, Radiobutton
# From Pillow
from PIL import Image, ImageTk
# From Program
from frontend.framework.grid import Grid


class UpdateLanguages():
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
        self.var_notification = StringVar()
        self.var_language = StringVar()

        # Widgets row 0
        self.w_title = None
        # Widgets row 1
        self.w_en_flag = None
        self.w_en_name = None
        self.w_en_check = None

        self.w_fr_flag = None
        self.w_fr_name = None
        self.w_fr_check = None

        self.w_de_flag = None
        self.w_de_name = None
        self.w_de_check = None
        # Widgets row 2
        self.w_it_flag = None
        self.w_it_name = None
        self.w_it_check = None

        self.w_es_flag = None
        self.w_es_name = None
        self.w_es_check = None

        self.w_nl_flag = None
        self.w_nl_name = None
        self.w_nl_check = None

        # Widgets row 3
        self.w_previous_button = None
        self.w_submit_button = None

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
            file_name="languages"
        )
        self.name = self.json_script.get("view_name")

        self.var_notification.set(" ")

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

    def display_previous(self):
        """ Display view 'update_server_conn'. """

        self.displayer.display(
            c_view="update_languages",
            f_view="update_server_conn"
        )

    def display_step_3(self):
        """ Display view 'update_categories'. """

        self.displayer.display(
            c_view="update_languages",
            f_view="update_categories",
            language=str(self.var_language.get())
        )

    def row_0(self, action=None):
        """ Name : VIEW TITLE
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
        """ Name : LANGAGE 1-3
            cols : 3 """

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
                span=4,
                row=1,
                width=None,
                height=None,
                padx=None,
                pady=20,
                bg=None
            )
            self.grid.column(
                span=4,
                row=1,
                width=None,
                height=None,
                padx=None,
                pady=20,
                bg=None
            )
            self.grid.column(
                span=4,
                row=1,
                width=None,
                height=None,
                padx=None,
                pady=20,
                bg=None
            )

        elif action == "fill":

            # Get script
            txt = self.json_script.get("row_1")

            # -- COLUMN 1/3 : ENGLISH LANGUAGE -- #
            img = Image.open(
                "frontend/images/flags/en.png"
            )
            imgResize = img.resize((30, 30), Image.ANTIALIAS)
            imgTkinter = ImageTk.PhotoImage(imgResize)

            if self.w_en_flag is None:

                self.w_en_flag = Label(
                    self.grid.col_frames[1][0],
                    image=imgTkinter,
                    borderwidth=0,
                    bg="#ffffff"
                )
                self.w_en_flag.image = imgTkinter
                self.w_en_flag.pack(fill='both', expand=True)

            if self.w_en_name is None:

                self.w_en_name = Label(
                    self.grid.col_frames[1][0],
                    pady=0,
                    text=txt.get("english_label"),
                    bg="#ffffff",
                    fg="#000000",
                    font="Helvetica 12 bold"
                )
                self.w_en_name.pack(fill='both', expand=True)

            if self.w_en_check is None:

                self.w_en_check = Radiobutton(
                    self.grid.col_frames[1][0],
                    variable=self.var_language,
                    value="en",
                    bg="#ffffff"
                )
                self.w_en_check.pack(fill='both', expand=True)

                if self.session.gui_language == "en":
                    self.w_en_check.select()

            # -- COLUMN 2/3 : FRENCH LANGUAGE -- #
            img = Image.open(
                "frontend/images/flags/fr.png"
            )
            imgResize = img.resize((30, 30), Image.ANTIALIAS)
            imgTkinter = ImageTk.PhotoImage(imgResize)

            if self.w_fr_flag is None:

                self.w_fr_flag = Label(
                    self.grid.col_frames[1][1],
                    image=imgTkinter,
                    borderwidth=0,
                    bg="#ffffff"
                )
                self.w_fr_flag.image = imgTkinter
                self.w_fr_flag.pack(fill='both', expand=True)

            if self.w_fr_name is None:

                self.w_fr_name = Label(
                    self.grid.col_frames[1][1],
                    pady=0,
                    text=txt.get("french_label"),
                    bg="#ffffff",
                    fg="#000000",
                    font="Helvetica 12 bold"
                )
                self.w_fr_name.pack(fill='both', expand=True)

            if self.w_fr_check is None:

                self.w_fr_check = Radiobutton(
                    self.grid.col_frames[1][1],
                    variable=self.var_language,
                    value="fr",
                    bg="#ffffff"
                )
                self.w_fr_check.pack(fill='both', expand=True)

                if self.session.gui_language == "fr":
                        self.w_fr_check.select()

            # -- COLUMN 3/3 : GERMAN LANGUAGE -- #
            img = Image.open(
                "frontend/images/flags/de.png"
            )
            imgResize = img.resize((30, 30), Image.ANTIALIAS)
            imgTkinter = ImageTk.PhotoImage(imgResize)

            if self.w_de_flag is None:

                self.w_de_flag = Label(
                    self.grid.col_frames[1][2],
                    image=imgTkinter,
                    borderwidth=0,
                    bg="#ffffff"
                )
                self.w_de_flag.image = imgTkinter
                self.w_de_flag.pack(fill='both', expand=True)

            if self.w_de_name is None:

                self.w_de_name = Label(
                    self.grid.col_frames[1][2],
                    pady=0,
                    text=txt.get("german_label"),
                    bg="#ffffff",
                    fg="#000000",
                    font="Helvetica 12 bold"
                )
                self.w_de_name.pack(fill='both', expand=True)

            if self.w_de_check is None:

                self.w_de_check = Radiobutton(
                    self.grid.col_frames[1][2],
                    variable=self.var_language,
                    value="de",
                    bg="#ffffff"
                )
                self.w_de_check.pack(fill='both', expand=True)

        elif action == "refresh":

            self.w_en_flag.pack_forget()
            self.w_en_name.pack_forget()
            self.w_en_check.pack_forget()

            self.w_fr_flag.pack_forget()
            self.w_fr_name.pack_forget()
            self.w_fr_check.pack_forget()

            self.w_de_flag.pack_forget()
            self.w_de_name.pack_forget()
            self.w_de_check.pack_forget()

            self.w_en_flag = None
            self.w_en_name = None
            self.w_en_check = None

            self.w_fr_flag = None
            self.w_fr_name = None
            self.w_fr_check = None

            self.w_de_flag = None
            self.w_de_name = None
            self.w_de_check = None

    def row_2(self, action=None):
        """ Name : LANGAGE 3-6
            cols : 3 """

        if action == "construct":

            # -- CREATE ROW -- #
            self.grid.row(
                width=self.width,
                height=140,
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
                pady=20,
                bg=None
            )
            self.grid.column(
                span=4,
                row=2,
                width=None,
                height=None,
                padx=None,
                pady=20,
                bg=None
            )
            self.grid.column(
                span=4,
                row=2,
                width=None,
                height=None,
                padx=None,
                pady=20,
                bg=None
            )

        elif action == "fill":

            # Get script
            txt = self.json_script.get("row_2")

            # -- COLUMN 1/3 : ITALIAN LANGUAGE -- #
            img = Image.open(
                "frontend/images/flags/it.png"
            )
            imgResize = img.resize((30, 30), Image.ANTIALIAS)
            imgTkinter = ImageTk.PhotoImage(imgResize)

            if self.w_it_flag is None:

                self.w_it_flag = Label(
                    self.grid.col_frames[2][0],
                    image=imgTkinter,
                    borderwidth=0,
                    bg="#ffffff"
                )
                self.w_it_flag.image = imgTkinter
                self.w_it_flag.pack(fill='both', expand=True)

            if self.w_it_name is None:

                self.w_it_name = Label(
                    self.grid.col_frames[2][0],
                    pady=0,
                    text=txt.get("italian_label"),
                    bg="#ffffff",
                    fg="#000000",
                    font="Helvetica 12 bold"
                )
                self.w_it_name.pack(fill='both', expand=True)

            if self.w_it_check is None:

                self.w_it_check = Radiobutton(
                    self.grid.col_frames[2][0],
                    variable=self.var_language,
                    value="it",
                    bg="#ffffff"
                )
                self.w_it_check.pack(fill='both', expand=True)

            # -- COLUMN 2/3 : SPANISH LANGUAGE -- #
            img = Image.open(
                "frontend/images/flags/es.png"
            )
            imgResize = img.resize((30, 30), Image.ANTIALIAS)
            imgTkinter = ImageTk.PhotoImage(imgResize)

            if self.w_es_flag is None:

                self.w_es_flag = Label(
                    self.grid.col_frames[2][1],
                    image=imgTkinter,
                    borderwidth=0,
                    bg="#ffffff"
                )
                self.w_es_flag.image = imgTkinter
                self.w_es_flag.pack(fill='both', expand=True)

            if self.w_es_name is None:

                self.w_es_name = Label(
                    self.grid.col_frames[2][1],
                    pady=0,
                    text=txt.get("spanish_label"),
                    bg="#ffffff",
                    fg="#000000",
                    font="Helvetica 12 bold"
                )
                self.w_es_name.pack(fill='both', expand=True)

            if self.w_es_check is None:

                self.w_es_check = Radiobutton(
                    self.grid.col_frames[2][1],
                    variable=self.var_language,
                    value="es",
                    bg="#ffffff"
                )
                self.w_es_check.pack(fill='both', expand=True)

            # -- COLUMN 3/3 : DUTCH LANGUAGE -- #
            img = Image.open(
                "frontend/images/flags/nl.png"
            )
            imgResize = img.resize((30, 30), Image.ANTIALIAS)
            imgTkinter = ImageTk.PhotoImage(imgResize)

            if self.w_nl_flag is None:

                self.w_nl_flag = Label(
                    self.grid.col_frames[2][2],
                    image=imgTkinter,
                    borderwidth=0,
                    bg="#ffffff"
                )
                self.w_nl_flag.image = imgTkinter
                self.w_nl_flag.pack(fill='both', expand=True)

            if self.w_nl_name is None:

                self.w_nl_name = Label(
                    self.grid.col_frames[2][2],
                    pady=0,
                    text=txt.get("dutch_label"),
                    bg="#ffffff",
                    fg="#000000",
                    font="Helvetica 12 bold"
                )
                self.w_nl_name.pack(fill='both', expand=True)

            if self.w_nl_check is None:

                self.w_nl_check = Radiobutton(
                    self.grid.col_frames[2][2],
                    variable=self.var_language,
                    value="nl",
                    bg="#ffffff"
                )
                self.w_nl_check.pack(fill='both', expand=True)

        elif action == "refresh":

            self.w_it_flag.pack_forget()
            self.w_it_name.pack_forget()
            self.w_it_check.pack_forget()

            self.w_es_flag.pack_forget()
            self.w_es_name.pack_forget()
            self.w_es_check.pack_forget()

            self.w_nl_flag.pack_forget()
            self.w_nl_name.pack_forget()
            self.w_nl_check.pack_forget()

            self.w_it_flag = None
            self.w_it_name = None
            self.w_it_check = None

            self.w_es_flag = None
            self.w_es_name = None
            self.w_es_check = None

            self.w_nl_flag = None
            self.w_nl_name = None
            self.w_nl_check = None

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
                    command=self.display_step_3
                )
                self.w_submit_button.pack(side=BOTTOM, fill=X)
            # -- COLUMN 3/3 : EMPTY -- #

        elif action == "refresh":

            self.w_previous_button.pack_forget()
            self.w_submit_button.pack_forget()

            self.w_previous_button = None
            self.w_submit_button = None
