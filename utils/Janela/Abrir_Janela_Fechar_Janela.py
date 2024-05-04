import pygetwindow as gw

def AbrirJanela():
        from utils.Janela.Janela import root
        [window for window in gw.getWindowsWithTitle(root.title()) if window.title == root.title()][0].minimize()
        [window for window in gw.getWindowsWithTitle(root.title()) if window.title == root.title()][0].restore()
        [window for window in gw.getWindowsWithTitle(root.title()) if window.title == root.title()][0].activate()
        
def fechar_janela(root):
    root.destroy()
    exit()