# -*- coding: utf-8 -*-
import os
import sys

import webview

APP_VERSION = "1.0.0"


def resource(name):
    base = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base, name)


def main():
    win = webview.create_window(
        title="嘴臭模擬器",
        url=resource("index.html"),
        min_size=(420, 640),
        background_color="#0a0a0f",
        text_select=False,
    )
    webview.start()


if __name__ == "__main__":
    main()