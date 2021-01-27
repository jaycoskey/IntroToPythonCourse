#/usr/bin/env python3

import tkinter as tk


def highlight_term_one(txt_widget, phrase, tag_name, bg, fg):
    '''Adding a tag using Text's search function'''
    phrase_len = tk.StringVar()
    posn = text.search(phrase, '1.0', stopindex='end', count=phrase_len)
    print('phrase_len=', phrase_len, phrase_len.get())
    if posn != '':
        txt_widget.tag_add(tag_name, posn, '{0:s} + {1:s}c'.format(posn, phrase_len.get()))
        txt_widget.tag_config(tag_name, background=bg, foreground=fg)


def highlight_term_many(txt_widget, phrase, tag_name, bg, fg):
    '''Adding multiple tags, using Text's search function'''
    phrase_len = tk.StringVar()
    posn = '1.0'  # Start at the beginning
    while True:
        posn = text.search(phrase, posn + '+1c', stopindex='end', count=phrase_len)
        if posn == '':
            break
        txt_widget.tag_add(tag_name, posn, '{0:s} + {1:s}c'.format(posn, phrase_len.get()))
        txt_widget.tag_config(tag_name, background=bg, foreground=fg)


if __name__ == '__main__':
    root = tk.Tk()
    root.title('Highlighting Demo App')
    text = tk.Text(root)
    text.insert(tk.INSERT, 'Hello, world!\n')
    text.insert(tk.END, 'I heard it takes five sheep to make one wool sweater.\n')
    text.insert(tk.END, 'But how long does it take them to learn to knit?')
    text.pack(expand=1, fill=tk.BOTH)

    # Tagging a part of text specified by line and character counts.
    text.tag_add('demo', '1.7', '1.12')
    text.tag_config('demo', background='black', foreground='yellow')

    # Note that the word "it" appears twice in the text, but it's only highlighted once.
    highlight_term_one(text, 'it', 'reut', 'yellow', 'red')
    
    # The word "take" appears twice in the text, and both are highlighted.
    highlight_term_many(text, 'take', 'mimi', 'orange', 'blue')
    root.mainloop()
