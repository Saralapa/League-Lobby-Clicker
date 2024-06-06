import pygetwindow as gw
import tkinter as tk


def AbrirJanela(title: str) -> None:
    """
    Opens a window with the specified title, minimizes it, restores it, and activates it.

    Parameters:
    title (str): The title of the window to be opened.

    Returns:
    None
    """
    [window for window in gw.getWindowsWithTitle(title) if window.title == title][
        0
    ].minimize()
    [window for window in gw.getWindowsWithTitle(title) if window.title == title][
        0
    ].restore()
    [window for window in gw.getWindowsWithTitle(title) if window.title == title][
        0
    ].activate()


def fechar_janela(root: tk.Tk) -> None:
    """
    Closes the specified Tkinter window and exits the application.

    Parameters:
    root (tk.Tk): The Tkinter window to be closed.

    Returns:
    None
    """
    root.destroy()
    exit()
