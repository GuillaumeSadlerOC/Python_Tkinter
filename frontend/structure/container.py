""" CONTAINER
- The program has only one container. """

# -*- coding: utf-8 -*-
# From Python 3
# From Tkinter
# From Program


class Container():
    def __init__(
        self,
        page=None
    ):
        """ 'page'      (obj  ): instance of Grid by Page.
            'container' (frame): frame row of container. """

        # Instances
        self.page = page

        # Frames
        self.f_container = None

        # Style Sheet
        self.width = self.page.width
        self.height = 650
        self.padx = 0
        self.pady = 0
        self.bg = "#ffffff"

        self.f_container = self.page.row(
            width=self.width,
            height=self.height,
            padx=self.padx,
            pady=self.pady,
            bg=self.bg
        )
