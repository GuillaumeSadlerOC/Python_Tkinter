""" FOOTER
- The program has only one footer. """

# -*- coding: utf-8 -*-
# From Python 3
# From Tkinter
from tkinter import Label
# From Pillow
from PIL import Image, ImageTk
# From Program


class Footer():
    def __init__(self, page=None):
        """ 'page' (obj): instance of Grid by Page. """

        # Instances
        self.page = page

        # Frames
        self.f_footer = None

        # Style Sheet
        self.width = self.page.width
        self.height = 85
        self.padx = 0
        self.pady = 0
        self.bg = "#EDEDED"

        # ----- ROWS ----- #
        self.f_footer = self.page.row(
            width=self.width,
            height=self.height,
            padx=self.padx,
            pady=self.pady,
            bg=self.bg
        )

        # ----- COLS ----- #
        self.page.column(
            span=2,
            row=2,
            width=None,
            height=None,
            padx=None,
            pady=None,
            bg=self.bg
        )

        self.page.column(
            span=8,
            row=2,
            width=None,
            height=None,
            padx=None,
            pady=None,
            bg=self.bg
        )

        self.page.column(
            span=2,
            row=2,
            width=None,
            height=None,
            padx=None,
            pady=None,
            bg=self.bg
        )

        # -- ROW 0 - COLUMN 1/3 : OC LOGO -- #
        img = Image.open(
            "frontend/images/logos/logo_OC2.png"
        )
        resize_img = img.resize((100, 60), Image.ANTIALIAS)
        img_logo_OC = ImageTk.PhotoImage(resize_img)

        logo_OC = Label(
            self.page.col_frames[2][0],
            bg="#EDEDED",
            image=img_logo_OC,
            borderwidth=0
        )
        logo_OC.image = img_logo_OC
        logo_OC.pack(fill="both", expand=True)

        # -- ROW 0 - COLUMN 2/3 : DATE -- #
        date = Label(
            self.page.col_frames[2][1],
            text="2018 - 2019",
            bg="#EDEDED"
        )
        date.pack(fill="both", expand=True)

        # -- ROW 0 - COLUMN 3/3 : OFF LOGO -- #
        img = Image.open(
            "frontend/images/logos/logo_off.png"
        )
        resize_img = img.resize((55, 55), Image.ANTIALIAS)
        img_logo_off = ImageTk.PhotoImage(resize_img)

        logo_off = Label(
            self.page.col_frames[2][2],
            bg="#EDEDED",
            image=img_logo_off,
            borderwidth=0
        )
        logo_off.image = img_logo_off
        logo_off.pack(fill="both", expand=True)
