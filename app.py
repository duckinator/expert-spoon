#!/usr/bin/env python3

import tkinter

class Element:
    def __init__(self, name=None, children=None):
        self.name = name
        if children is None:
            self.children = []
        else:
            self.children = children

        self.left_of(None)
        self.right_of(None)
        self.above(None)
        self.below(None)

    def add_child(self, child):
        self.children += [child]

    def add_children(self, children):
        self.children += children

    def right_of(self, obj):
        self.is_right_of = obj

    def below(self, obj):
        self.is_below = obj


class List(Element):
    def draw(self):
        print("[List.draw       ] List with {} elements.".format(len(self.children)))


class Button(Element):
    def __init__(self, text, on_activate=None, **kwargs):
        self.text = text
        self.on_activate = on_activate
        super().__init__(**kwargs)

    def activate(self, *args, **kwargs):
        if self.on_activate is not None:
            self.on_activate(*args, **kwargs)

    def draw(self):
        print("[Button.draw     ] Button({}, name={}, on_activate={})".format(self.text, self.name, self.on_activate))

class Label(Element):
    def __init__(self, text, **kwargs):
        self.text = text
        super().__init__(**kwargs)

    def set_text(self, text):
        self.text = text

    def draw(self):
        print("[Label.draw      ] Label({})".format(self.text))

class Scrollable(Element):
    def draw(self):
        print("[Scrollable.draw ] Scrollable() with {} children.".format(len(self.children)))

class TextBox(Element):
    def __init__(self, start_text=None, placeholder=None, **kwargs):
        self.start_text = start_text
        self.placeholder = placeholder
        super().__init__(**kwargs)

    def draw(self, x, y, width, height):
        pass

class Window(Element):
    def __init__(self, x=None, y=None, width=None, height=None, **kwargs):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.items = []
        super().__init__(**kwargs)

    def draw(self):
        cols = 80
        rows = 24
        screen = [" "] * cols * rows

        left_side = filter(lambda x: x.is_right_of == None, self.children)
        top_left = filter(lambda x: x.is_above == None, left_side)
        for child in self.children.keys():
            child.draw(screen, x, y, width, height)

servers     = List()
channels    = List()
scrollback  = Scrollable()
handle      = Label("")
message     = TextBox()

servers.right_of(None)
servers.below(None)

channels.right_of(servers)
channels.below(None)

scrollback.right_of(channels)
scrollback.below(None)

handle.right_of(channels)
handle.below(scrollback)

message.right_of(handle)
message.below(scrollback)

window = Window(name="test", x=10, y=20, width=500, height=200)
window.children([servers, channels, scrollback, handle, message])
window.draw()
