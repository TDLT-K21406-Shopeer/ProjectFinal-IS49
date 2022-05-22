def center(win):
    """
    Used to make Tkinter GUI window in the screen center
    :param win: the main window or Toplevel window to center
    """
    win.update_idletasks()
    width = win.winfo_width()
    height = win.winfo_height()
    x = (win.winfo_screenwidth() //4 )- (width // 2)
    y = (win.winfo_screenheight() // 4) - (height // 2)
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    # win.deiconify()