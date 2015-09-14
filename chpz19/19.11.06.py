"""Use Tkinter to write a basic web browser. It should have a Text widget where
the user can enter a URL and a Canvas to display the contents of the page.
You can use the urllib module to download files (see Exercise 6) and the HTMLParser
module to parse the HTML tags (see http://docs.python.org/2/library/htmlparser.html).

At a minimum your browser should handle plain text and hyperlinks. As a challenge you
could handle background colors, text formatting tags and images."""

import Tkinter
import requests
from HTMLParser import HTMLParser


class Web_Browser(Tkinter.Tk):
    def __init__(self, parent):
        Tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.canvas = Tkinter.Canvas(width=300, height=200, background='white')
        self.canvas.grid(row=0,column=2)

        self.entryVariable = Tkinter.StringVar()
        self.entry = Tkinter.Entry(self, textvariable=self.entryVariable)
        self.entry.grid(column=0, row=0, sticky="EW")
        self.entry.bind("<Return>", self.OnPressEnter)
        self.entryVariable.set(u"Enter URL here")

        button = Tkinter.Button(self, text="Get URL text", command=self.OnButtonClick)
        button.grid(column=1, row=0)

        self.labelVariable = Tkinter.StringVar()
        label = Tkinter.Label(self, textvariable=self.labelVariable, anchor="w", fg="white", bg="blue")
        label.grid(column=0, row=1, columnspan=2, sticky="EW")
        self.labelVariable.set(u"Hello !")

        self.grid_columnconfigure(0, weight=1)
        self.resizable(True, False)
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)



    def OnButtonClick(self):
        url = self.entryVariable.get()
        html_text = get_HTML_text(url)

        self.labelVariable.set(self.entryVariable.get())

        self.canvas.delete("all")
        canvas_id = self.canvas.create_text(10, 10, anchor="nw")
        self.canvas.itemconfig(canvas_id, text=html_text)
        self.canvas.insert(canvas_id, 12, " ")

        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)


    def OnPressEnter(self, event):

        url = self.entryVariable.get()
        html_text = get_HTML_text(url)

        self.labelVariable.set(self.entryVariable.get())
        self.canvas.delete("all")
        canvas_id = self.canvas.create_text(10, 10, anchor="nw")
        self.canvas.itemconfig(canvas_id, text=html_text)
        self.canvas.insert(canvas_id, 12, " ")

        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)


class PaigeHtmlParser(HTMLParser):
    def __init__(self):
        self.parsed_text = ""
        HTMLParser.__init__(self)

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            self.parsed_text += 'Encountered a link to: ' + dict(attrs)['href'] + "\n"
            self.parsed_text += 'The link text is: ' + "\n"
        else:
            self.parsed_text += "Encounted tag " + tag + "\n"

    def handle_data(self, data):
        self.parsed_text += "Encounted some data: " + data + "\n"


def get_HTML_text(url):
    p = PaigeHtmlParser()
    html_text = requests.get(url).content
    p.feed(html_text)
    p.close()
    return p.parsed_text


if __name__ == "__main__":
    web_browser = Web_Browser(None)
    web_browser.title('my application')
    web_browser.mainloop()

