""" PAGE
- The program has only one page.
- Only views in the container are modified. """

# -*- coding: utf-8 -*-
# From Python 3
# From Tkinter
# From Program
from frontend.framework.grid import Grid
from frontend.structure.menubar import MenuBar
from frontend.structure.header import Header
from frontend.structure.container import Container
from frontend.structure.footer import Footer


class Page(Grid):
    def __init__(
        self,
        window=None,
        displayer=None
    ):
        """ 'window'        (obj  ): Tk window.
            'displayer'     (obj  ): instance of Displayer.
            'header'        (Frame): instance of Header.
            'container'     (Frame): instance of Container.
            'footer'        (Frame): instance of Footer.
            'f_header'      (Frame): master frame of header.
            'f_container'   (Frame): master frame of container.
            'f_footer'      (Frame): master frame of footer. """

        # Instances
        self.menubar = None
        self.header = None
        self.container = None
        self.footer = None
        self.displayer = displayer

        # Frames
        self.f_header = None
        self.f_container = None
        self.f_footer = None

        # Style Sheet
        self.width = window.width
        self.height = window.height
        self.padx = 0
        self.pady = 0
        self.bg = "#ffffff"

        super().__init__(
            frame=window,
            width=self.width,
            height=self.height,
            padx=self.padx,
            pady=self.pady,
            bg=self.bg
        )

        self.menu_bar()

        # 1. Construct header
        self.header = Header(
            page=self
        )
        self.f_header = self.header.f_header

        # 2. Construct container
        self.container = Container(
            page=self
        )
        self.f_container = self.container.f_container

        # 3. Construct footer
        self.footer = Footer(
            page=self
        )
        self.f_footer = self.footer.f_footer

    def menu_bar(self):
        """ Display and refresh menubar. """

        self.menubar = MenuBar(displayer=self.displayer)
