""" Grid
Small framework based on the famous bootstrap framework.
This framework :
- Is composed of 12 columns,
- Is cutable an infinite line,
- One row can be composed between one to 6 'master \
columns' of 2 columns each. """

# -*- coding: utf-8 -*-
# From Python 3
# From Tkinter
from tkinter import Frame
# From Program


class Grid():
    """ Build a grid following the bootstrap model.
    This class can be used to create a grid in a grid. """
    def __init__(
        self,
        frame=None,
        width=None,
        height=None,
        padx=0,
        pady=0,
        bg="#ffffff"
    ):
        """ 'frame'         (Frame): Tkinter frame.
            'width'         (int  ): new frame width.
            'height'        (int  ): new frame height.
            'padx'          (int  ): new frame space (top/bottom).
            'pady'          (int  ): new frame space (right/left).
            'bg'            (str  ): new frame background color.
            'master_frame'  (Frame): new frame.
            'row_frames'    (list ): new frame row frames.
            'row_settings'  (list ): new frame row frames settings.
            'col_frames'    (list ): new frame column frames.
            'col_settings'  (list ): new frame column frames settings. """

        self.frame = frame
        self.width = width - pady
        self.height = height - padx
        self.padx = padx
        self.pady = pady
        self.bg = bg

        self.master_frame = None
        self.row_frames = []
        self.row_settings = []
        self.col_frames = []
        self.col_settings = []

        self.create_master_frame()

    def create_master_frame(self):
        """When an instance of this class is created,\
        we create a main frame on the frame received as a parameter.
        (!) This method should only be called once. """

        self.master_frame = Frame(
            self.frame,
            width=self.width,
            height=self.height,
            padx=self.padx,
            pady=self.pady,
            bg=self.bg
        )

        self.master_frame.grid(
            column=0,
            row=0,
            columnspan=12,
            sticky="nesw",
        )
        self.master_frame.grid_propagate(0)

    def row(
        self,
        width=None,
        height=None,
        padx=None,
        pady=None,
        bg=None
    ):
        """ Create row frame in master_frame.
        This frame represent an row. """

        # 1. Per default
        if width is None:
            width = self.width

        if height is None:
            height = self.height

        if padx is None:
            padx = self.padx

        if pady is None:
            pady = self.pady

        if bg is None:
            bg = self.bg

        # 2. Row frames count
        row_count = len(self.row_frames)

        # 3. Create new frame
        row = Frame(
            self.master_frame,
            width=width,
            height=height,
            padx=padx,
            pady=pady,
            bg=bg
        )
        # 4. Grid in new frame
        row.grid(
            column=0,
            row=row_count,
            columnspan=12,
            sticky="nesw",
        )
        row.grid_propagate(0)
        # 5. Save row frame in list
        self.row_frames.append(row)
        # 6. Create settings
        settings = {}
        settings["width"] = width
        settings["height"] = height
        settings["padx"] = padx
        settings["pady"] = pady
        settings["bg"] = bg
        settings["col_width"] = width / 12
        settings["cols"] = 0
        # 7. Save row settings
        self.row_settings.append(settings)

        bloc_cols = []
        self.col_frames.append(bloc_cols)

        bloc_cols = []
        self.col_settings.append(bloc_cols)

        return row

    def column(
        self,
        span=0,
        row=None,
        width=None,
        height=None,
        padx=None,
        pady=None,
        bg=None
    ):
        """ 'span'  (int):
            'row'   (int): number of row frame.
        """

        row_frame = self.row_frames[row]
        row_settings = self.row_settings[row]

        if height is None:
            height = int(row_settings.get("height"))

        if width is None:
            width = int(row_settings.get("width"))

        if padx is None:
            padx = int(row_settings.get("padx"))

        if pady is None:
            pady = int(row_settings.get("pady"))

        if bg is None:
            bg = row_settings.get("bg")

        row_cols = int(row_settings.get("cols"))

        # 3. Create new frame
        column = Frame(
            row_frame,
            height=height,
            width=width,
            padx=padx,
            pady=pady,
            bg=bg
        )
        # 4. Grid in new frame
        column.grid(
            column=0,
            row=0,
            columnspan=span,
            sticky="nesw"
        )
        column.grid_propagate(0)
        column.pack_propagate(False)
        # 5. Save column frame in list
        self.col_frames[row].append(column)
        # 6. Update number of row columns
        row_count = row_cols + 1
        self.row_settings[row]["cols"] = row_count
        # 7. Create settings
        settings = {}
        settings["row"] = row
        settings["span"] = span
        settings["width"] = width
        settings["height"] = height
        settings["padx"] = padx
        settings["pady"] = pady
        settings["bg"] = bg
        # 8. Save settings
        self.col_settings[row].append(settings)
        # 9.config column
        self.column_config(row=row)

        return column

    def column_config(
        self,
        row=None
    ):
        """ This method comput the size \
        and span of columns. """

        row_width = int(
            self.row_settings[row].get("width")
        )
        row_cols = int(
            self.row_settings[row].get("cols")
        )
        default_col_width = self.row_settings[row].get(
            "col_width"
        )

        cols_frames = self.col_frames[row]
        cols_settings = self.col_settings[row]

        previous_pos = 0
        for i in range(row_cols):

            span = cols_settings[i]["span"]
            if int(span) == 0:
                col_width = row_width // row_cols
                col_span = 12 // row_cols
                col_pos = i * col_span
            else:
                if i == 0:
                    col_pos = 0
                else:
                    col_span_prev = cols_settings[i-1]["span"]
                    col_pos = col_span_prev + previous_pos

                col_span = span
                col_width = default_col_width * span

            cols_settings[i]["width"] = col_width
            cols_settings[i]["span"] = col_span

            cols_frames[i].config(width=col_width)
            cols_frames[i].grid(
                column=col_pos,
                row=0,
                columnspan=col_span,
                sticky="nesw"
            )

            previous_pos = col_pos
