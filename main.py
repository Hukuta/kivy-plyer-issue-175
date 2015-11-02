#!/usr/bin/env python
# -*- coding: utf-8 -*-
import kivy
from kivy.app import App
from kivy.uix.label import Label
from plyer import notification

__author__ = 'Odarchenko N.D.'
__version__ = "0.2"
kivy.require('1.9.0')


class MyApp(App):

    # russian "Hello World"
    hello_world = u'Привет, Мир'

    def on_pause(self):
        return True

    def build(self):
        notification.notify(title=u'Issue 175', message=MyApp.hello_world)
        return Label(text=MyApp.hello_world)


if __name__ == '__main__':
    MyApp().run()
