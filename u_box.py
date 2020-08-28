#!/usr/bin/python
# box.py
# Tekin-Miz (WorldMoZara)

import urwid

class uListBox():
    def __init__(self, title: str, ilist: list):
        main = urwid.AttrMap(urwid.Padding(self._menu(title, ilist), left=1, right=1), 'win')
        top = urwid.Overlay(main, urwid.SolidFill(u' '),
                align='center', width=('relative', 60), valign='middle',
                height=('relative', 80), min_width=40, min_height=14)
        self._attrd = urwid.AttrMap(top, 'bg')
    def _menu(self, title, choices):
        body = [urwid.AttrMap(urwid.Text(title), 'title'), urwid.Divider()]
        for c in choices:
            button = urwid.Button(c)
            urwid.connect_signal(button, 'click', self._item_chosen, c)
            body.append(urwid.AttrMap(button, None, focus_map='reversed'))
        return urwid.LineBox(urwid.ListBox(urwid.SimpleFocusListWalker(body)))
    def _item_chosen(self, button, choice):
        self.result = choice
        self._exit_program(button)
    def _exit_program(self, button):
        raise urwid.ExitMainLoop()
    def show(self):
        urwid.MainLoop(self._attrd, palette).run()

class uMsgBox():
    def __init__(self, title: str, msg: str = '', button_name: str = 'OK'):
        main = urwid.AttrMap(urwid.Padding(self._menu(title, msg, button_name), left=1, right=1), 'win')
        top = urwid.Overlay(main, urwid.SolidFill(u' '), align='center',
                width=('relative', 60),valign='middle', height=('relative', 60),
                min_width=20, min_height=9)
        self._attrd = urwid.AttrMap(top, 'bg')
    def _menu(self, title, msg, bname):
        body = [urwid.Divider(), urwid.AttrMap(urwid.Text(title), 'title'), urwid.Divider(), urwid.AttrMap(urwid.Text(msg), 'msg'), urwid.Divider()]
        button = urwid.Button(bname)
        urwid.connect_signal(button, 'click', self._item_chosen, None)
        body.append(button)
        return urwid.LineBox(urwid.ListBox(urwid.SimpleFocusListWalker(body)))
    def _item_chosen(self, button):
        raise urwid.ExitMainLoop()
    def show(self):
        urwid.MainLoop(self._attrd, palette).run()

urwid.set_encoding("UTF-8")
palette = [
        ('reversed', 'standout', ''),
        ('win', 'black', 'light gray'),
        ('bg', 'black', 'dark blue'),
        ('title', 'yellow', 'light blue'),
        ('msg', 'white', 'dark gray'),
        ]

