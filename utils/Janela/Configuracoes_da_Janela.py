from ctypes import windll
from utils.Janela.Abrir_Janela_Fechar_Janela import fechar_janela


def ConfiguracoesJanela(root):
    root.title("League Lobby Clicker - Saralapa")
    root.iconbitmap("Images/icon.ico")
    root.config(bg="#191919")
    root.overrideredirect(True)
    root.resizable(False, False)
    root.protocol("WM_DELETE_WINDOW", lambda: fechar_janela(root))
    HWND = windll.user32.GetParent(root.winfo_id())

    windll.user32.SetWindowLongW(
        HWND, -20, windll.user32.GetWindowLongW(HWND, -20) & ~0x00000080 | 0x00040000
    )
    root.wm_withdraw()
    root.after(10, lambda: root.wm_deiconify())


def centralizar_janela(root, width, height):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    root.geometry(f"{width}x{height}+{x}+{y}")
    root.update()
