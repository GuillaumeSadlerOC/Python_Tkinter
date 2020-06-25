""" HEADER
- The program has only one header.
- Page width = 640
- Page height = 800 """

# -*- coding: utf-8 -*-
# From Python 3
# From Tkinter
from tkinter import StringVar
from tkinter import Label
# From Program


class Header():
    def __init__(
        self,
        page=None
    ):
        """ 'page'     (obj): instance of Grid by Page. """

        # Instances
        self.page = page

        # Frames
        self.f_header = None

        # Style Sheet
        self.width = self.page.width
        self.height = 65
        self.padx = 0
        self.pady = 0
        self.bg = "#7A57EC"

        # Tk variables
        self.var_title = StringVar()

        self.f_header = self.page.row(
            width=self.width,
            height=self.height,
            padx=self.padx,
            pady=self.pady,
            bg=self.bg
        )

        col_1 = self.page.column(
            span=12,
            row=0,
            width=None,
            height=None,
            padx=None,
            pady=None,
            bg=self.bg
        )

        # -- COLUMN 1/1 : TITLE -- #
        view_title = Label(
            col_1,
            padx=10,
            anchor="w",
            textvariable=self.var_title,
            bg=self.bg,
            fg="#ffffff",
            font="Helvetica 12 bold"
        )
        view_title.pack(fill='both', expand=True)
