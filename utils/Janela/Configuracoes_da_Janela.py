from ctypes import windll
from utils.Janela.Fechar_Janela import fechar_janela
def ConfiguracoesJanela(root):
    root.title("League Lobby Clicker - Saralapa")
    root.iconbitmap('Images/icon.ico')
    root.config(bg="#191919")
    root.overrideredirect(True)
    root.resizable(False, False)
    root.protocol("WM_DELETE_WINDOW", lambda: fechar_janela(root))
    HWND = windll.user32.GetParent(root.winfo_id())
    
    windll.user32.SetWindowLongW(HWND, -20, windll.user32.GetWindowLongW(HWND, -20) & ~0x00000080 | 0x00040000)
    root.wm_withdraw()
    root.after(10, lambda: root.wm_deiconify())