""" TK WINDOW """

# -*- coding: utf-8 -*-
# From Python 3
# From Tkinter
from tkinter import Tk, PhotoImage
# From Program


class Window(Tk):
    def __init__(self):
        super().__init__()
        """ 'resizable'     (int): Tk variable.
            'title'         (str): Tk variable.
            'favicon'       (Obj): favicon of app.
            'call'          (   ): Tk variable.
            'width'         (int): window width.
            'height'        (int): window height.
            'screen_width'  (int): screen width.
            'screen_height' (int): screen height.
        """
        self.resizable(width=False, height=False)
        self.title("Pur Beurre")
        self.favicon = PhotoImage(
            file='frontend/images/logos/logo_purbeurre.gif'
        )
        self.call('wm', 'iconphoto', self._w, self.favicon)
        self.width = 640
        self.height = 800
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()

        # Screen informations
        self.geometry("%dx%d+%d+%d" % (self.width, self.height, (
            self.screen_width-self.width)/2, (self.screen_height-self.height)/2
            )
        )
