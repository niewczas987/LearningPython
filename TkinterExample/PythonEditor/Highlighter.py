import tkinter as tk
import yaml
class Highlighter:
    def __init__(self, text_widget, syntax_file):
        self.text_widget = text_widget
        self.syntax_file = syntax_file
        self.categories = None
        self.numbers_color = 'blue'
        self.keywords_color = 'orange'
        self.disallowed_previous_chars = ['_', '-', '.']
        self.parse_syntax_file()
        self.text_widget.bind('<KeyRelease>', self.on_key_release)

    def on_key_release(self, event=None):
        self.highlight()

    def highlight(self, event=None):
        length = tk.IntVar()
        for category in self.categories:
            matches = self.categories[category]['matches']
            for keyword in matches:
                start = 1.0
                keyword = keyword + '[^A-Za-z_-]'
                idx = self.text_widget.search(keyword, start, stopindex=tk.END, count=length, regexp=1)
                while idx:
                    char_match_found = int(str(idx).split('.')[1])
                    line_match_found = int(str(idx).split('.')[0])
                    if char_match_found > 0:
                        previous_char_index = str(line_match_found) + '.' + str(char_match_found - 1)
                        previous_char = self.text_widget.get(previous_char_index,previous_char_index + '+1c')
                        if previous_char.isalnum() or previous_char in self.disallowed_previous_chars:
                            end = f'{idx}+{length.get() -1}c'
                            start = end
                            idx = self.text_widget.search(keyword, start, stopindex=tk.END, regexp=1)
                        else:
                            end = f'{idx}+{length.get() - 1}c'
                            self.text_widget.tag_add(category, idx, end)
                            start = end
                            idx = self.text_widget.search(keyword, start, stopindex=tk.END, regexp=1)
                    else:
                        end = f'{idx}+{length.get() - 1}c'
                        self.text_widget.tag_add(category, idx, end)
                        start = end
                        idx = self.text_widget.search(keyword, start, stopindex=tk.END, regexp=1)

                '''
                The regular expression used here can be broken down as follows:
                (\d)+: Match one or more numbers
                [.]?: Match zero or one decimal point
                (\d)*: Match zero or more numbers following the decimal point
                '''
                self.highlight_regex(r'(\d)+[.]?(\d)*', 'number')
                '''
                        These regexes can be broken down as follows:
                        [\']: Match the string opening character (')
                        [^\']*: Match any number of characters which are not the string-closing character
                        [\']: Match the string-closing character
                '''
                self.highlight_regex(r'[\'][^\']*[\']', 'string')
                self.highlight_regex(r'[\'][^\']*[\']', 'string')


    def highlight_regex(self, regex, tag):
        length = tk.IntVar()
        start = 1.0
        idx = self.text_widget.search(regex, start, stopindex=tk.END, regexp=1, count=length)
        while idx:
            end = f'{idx}+{length.get()}c'
            self.text_widget.tag_add(tag, idx, end)
            start = end
            idx = self.text_widget.search(regex, start, stopindex=tk.END, regexp=1, count=length)

    def parse_syntax_file(self):
        with open(self.syntax_file, 'r') as stream:
            try:
                config = yaml.safe_load(stream)
                self.categories = config['categories']
                self.numbers_color = config['numbers']['color']
                self.strings_color = config['strings']['color']
                self.configure_tags()
            except yaml.YAMLError as error:
                print(error)
                return

    def configure_tags(self):
        for category in self.categories.keys():
            color = self.categories[category]['color']
            self.text_widget.tag_configure(category, foreground=color)
        self.text_widget.tag_configure('number', foreground=self.numbers_color)
        self.text_widget.tag_configure('string', foreground=self.strings_color)

    def force_highlight(self):
        self.highlight()

    def clear_highlight(self):
        for category in self.categories:
            self.text_widget.tag_remove(category, 1.0, tk.END)

if __name__=='__main__':
    w = tk.Tk()
    t = tk.Text(w, bg='white', fg='black')
    h = Highlighter(t, 'languages/python.yaml')
    t.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    w.mainloop()