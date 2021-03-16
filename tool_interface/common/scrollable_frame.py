'''
Author: Desmond Goh
Date: 2021-03-14 19:34:30
LastEditTime: 2021-03-15 20:26:48
LastEditors: Desmond Goh
FilePath: /Combination_Generator_Tool/tool_interface/common/scrollable_frame.py
'''
import tkinter as tk

class ScrollableFrame:

    def __init__(self, parent_frame):
        self.parent_frame = parent_frame
        self.canvas = tk.Canvas(parent_frame)
        self.scrollable_frame = tk.Frame(self.canvas)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.canvas.create_window(
            (0,0),
            window=self.scrollable_frame,
            anchor='nw'
        )

        self.x_scrollbar = None
        self.y_scrollbar = None
        self.scroll_x = False
        self.scroll_y = False
        self.scrollable_frame.bind(
            '<Configure>',
            self.validate_scrollbar
        )
        self.bind_scroll()
        
    def add_horizontal_scrollbar(self):
        self.x_scrollbar = tk.Scrollbar(
            self.parent_frame,
            orient=tk.HORIZONTAL,
            command=self.canvas.xview)
        self.canvas.configure(xscrollcommand=self.x_scrollbar.set)

    def add_vertical_scrollbar(self):
        self.y_scrollbar = tk.Scrollbar(
            self.parent_frame,
            orient=tk.VERTICAL,
            command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.y_scrollbar.set)

    def validate_scrollbar(self, event):
        parent_width = self.parent_frame.winfo_width()
        parent_height = self.parent_frame.winfo_height()
        scrollable_width = self.scrollable_frame.winfo_width()
        scrollable_height = self.scrollable_frame.winfo_height()
        if scrollable_width < parent_width:
            if self.x_scrollbar != None: 
                self.scroll_x = False
                self.x_scrollbar.forget()
        if scrollable_height < parent_height:
            if self.y_scrollbar != None:
                self.scroll_y = False
                self.y_scrollbar.forget()
        if scrollable_width > parent_width:
            if self.x_scrollbar != None:
                self.x_scrollbar.pack(side=tk.BOTTOM, fill=tk.X, before=self.canvas)
                self.scroll_x = True
                self.canvas.configure(
                scrollregion=self.canvas.bbox('all'))
        if scrollable_height > parent_height:
            if self.y_scrollbar != None:
                self.y_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)     
                self.scroll_y = True
                self.canvas.configure(
                scrollregion=self.canvas.bbox('all'))

    def bind_scroll(self, *args):
        '''
        *args to take in event for event bind 
        '''
        self.parent_frame.bind('<MouseWheel>', self.mouse_scroll)
        #for Linux
        self.parent_frame.bind('<Button-4>', self.mouse_scroll)
        self.parent_frame.bind('<Button-5>', self.mouse_scroll)

    def unbind_scroll(self, *args):
        '''
        *args to take in event for event bind
        '''
        self.parent_frame.unbind('<MouseWheel>')
        #for Linux
        self.parent_frame.unbind('<Button-4>')
        self.parent_frame.unbind('<Button-5>')

    def mouse_scroll(self, event):
        shift = (event.state & 0x1) != 0
        scroll = -1 if event.delta > 0 else 1
        if shift and self.scroll_x:
            self.canvas.xview_scroll(scroll, "units")
        elif self.scroll_y:
            self.canvas.yview_scroll(scroll, "units")

    def unbind_scroll_for_widget(self, target_widget):
        target_widget.bind('<Enter>', self.unbind_scroll)
        target_widget.bind('<Leave>', self.bind_scroll)
        