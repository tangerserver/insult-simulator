# -*- coding: utf-8 -*-
import os
import sys
import threading
import time

import webview

APP_VERSION = "1.0.0"
WINDOW_TITLE = "嘴臭模擬器"


def resource(name):
    base = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base, name)


def dark_title_bar():
    if sys.platform != "win32":
        return
    import ctypes

    user32 = ctypes.windll.user32
    dwmapi = ctypes.windll.dwmapi
    hwnd = 0
    for _ in range(300):
        hwnd = user32.FindWindowW(None, WINDOW_TITLE)
        if hwnd:
            break
        time.sleep(0.05)
    if not hwnd:
        return
    dark = ctypes.c_int(1)
    caption = ctypes.c_uint(0x00000000)
    text = ctypes.c_uint(0x00F0E8E2)
    for _ in range(20):
        for attr in (20, 19):
            dwmapi.DwmSetWindowAttribute(hwnd, attr, ctypes.byref(dark), ctypes.sizeof(dark))
        dwmapi.DwmSetWindowAttribute(hwnd, 35, ctypes.byref(caption), ctypes.sizeof(caption))
        dwmapi.DwmSetWindowAttribute(hwnd, 36, ctypes.byref(text), ctypes.sizeof(text))
        time.sleep(0.15)


def main():
    win = webview.create_window(
        title=WINDOW_TITLE,
        url=resource("index.html"),
        min_size=(420, 640),
        background_color="#0a0a0f",
        text_select=False,
    )
    threading.Thread(target=dark_title_bar, daemon=True).start()
    webview.start()


if __name__ == "__main__":
    main()
