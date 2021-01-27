#!/usr/bin/env python3

import tkinter as tk


class ChatApp(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.initialize()

    def initialize(self):
        self.menubar = tk.Menu(root, tearoff=0)
        self.filemenu = tk.Menu(self.menubar)
        self.filemenu.add_command(label='Exit', command=root.quit)
        self.menubar.grid(column=0, row=0, columnspan=2)

        self.chat_frame = Frame(root)
        self.chat_frame.grid(column=0, row=1)
        self.lchat = ChatFrame(chat_frame, side='left')
        self.cchat = ChatFrame(chat_frame, side='center')
        self.rchat = ChatFrame(chat_frame, side='right')
        
        self.hscroll = tk.Scrollbar(self)
        self.main_frame.grid(column=0, row=2)
        
        self.vscroll = tk.Scrollbar(self)
        self.main_frame.grid(column=1, row=1)


class ChatFrame(tk.Frame):
    def __init__(self, master=None):
        self.name_frame = Frame(master, side='top')
        self.name_label = tk.Label(name_frame, text='Sender:', side='left')
        self.name_entry = tk.Entry(name_frame, side='right')

        self.msg_frame = Frame(master, side='top')
        self.msg_label = tk.Label(msg_frame, text='Message:', side='left')
        self.msg_entry = tk.Entry(msg_frame, side='right')

        self.to_frame = Frame(master, side='top')
        self.to_label = tk.Label(to_frame, text='Recipient:', side='left')
        self.to_entry = tk.Entry(to_frame, side='right')

        self.exit_frame = Frame(master, side='top')
        self.exit = tk.Button(root, text='Exit', side='top',
            command=root.destroy)


if __name__ == '__main__':
    root = tk.Tk()
    app = ChatApp(master=root)
    app.mainloop()
