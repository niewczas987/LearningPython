import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as msg
import yaml
from TextArea import TextArea
from Highlighter import Highlighter
from LineNumbers import LineNumbers
from FindWindow import FindWindow
from tkinter import filedialog
from FontChooser import FontChooser
from ColorChooser import ColorChooser

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Text Editor')
        self.background = 'lightgrey'
        self.foreground = 'black'
        self.text_background = 'lightgrey'
        self.text_foreground = 'black'
        self.configure_ttk_elements()
        self.text_area = TextArea(self, bg='white', fg='black', undo=True)
        self.scrollbar = ttk.Scrollbar(orient='vertical', command=self.scroll_text)
        self.text_area.configure(yscrollcommand=self.scrollbar.set)
        self.highlighter = Highlighter(self.text_area, 'languages/python.yaml')
        self.menu = tk.Menu(self, bg='lightgrey', fg='black')
        sub_menu_items = ['file', 'edit', 'tools', 'help']
        self.right_click_menu = tk.Menu(self, bg="lightgrey", fg="black", tearoff=0)
        self.right_click_menu.add_command(label='Cut', command=self.edit_cut)
        self.right_click_menu.add_command(label='Copy', command=self.edit_copy)
        self.right_click_menu.add_command(label='Paste', command=self.edit_paste)
        self.all_menus = [self.menu, self.right_click_menu]
        self.generate_sub_menu_items(sub_menu_items)
        self.configure(menu=self.menu)
        self.open_file = None
        self.font_family = 'Arial'
        self.font_size = 10
        self.line_number = LineNumbers(self, self.text_area, bg='grey', fg='white', width=1)
        self.bind_events()
        #packing
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.line_number.pack(side=tk.LEFT, fill=tk.Y)
        self.text_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    def generate_sub_menu_items(self, sub_menu_items):
        window_methods = [method_name for method_name in dir(self) if callable(getattr(self, method_name))]
        tkinter_methods = [method_name for method_name in dir(tk.Tk) if callable(getattr(tk.Tk, method_name))]
        my_methods = [method for method in set(window_methods)-set(tkinter_methods)] #list of all available created methods
        my_methods = sorted(my_methods)
        for item in sub_menu_items:
            sub_menu = tk.Menu(self.menu, tearoff=0, bg=self.background, fg=self.foreground)
            matching_methods = []
            for method in my_methods:
                if method.startswith(item):
                    matching_methods.append(method)
            for match in matching_methods:
                actual_method = getattr(self, match)
                method_shortcut = actual_method.__doc__.strip()
                friendly_name = ' '.join(match.split('_')[1:])
                sub_menu.add_command(label=friendly_name.title(), command=actual_method, accelerator=method_shortcut)
            self.menu.add_cascade(label=item.title(), menu=sub_menu)
            self.all_menus.append(sub_menu)

    def show_right_click_menu(self, event):
        x = self.winfo_x() + event.x
        y = self.winfo_y() + event.y
        self.right_click_menu.post(x, y)


    def scroll_text(self,*args):
        if len(args)>1:
            self.line_number.yview_moveto((args[1]))
            self.text_area.yview_moveto(args[1])
        else:
            event = args[0]
            if event.delta:
                move = -1 * (event.delta/120)
            else:
                if event.num == 5:
                    move = 1
                else:
                    move = -1
            self.line_number.yview_moveto(int(move),'units')
            self.text_area.yview_moveto(int(move),'units')

    def bind_events(self):
        self.text_area.bind('<MouseWheel>', self.scroll_text)
        self.text_area.bind('<Button-4>', self.scroll_text)
        self.text_area.bind('<Button-5>', self.scroll_text)
        self.line_number.bind('<MouseWheel>', lambda e: 'break')
        self.line_number.bind('<Button-4>', lambda e: 'break')
        self.line_number.bind('<Button-5>', lambda e: 'break')
        self.text_area.bind('<Control-f>', self.show_find_window)
        self.text_area.bind('<Button-3>', self.show_right_click_menu)
        self.text_area.bind('<Control-m>', self.tools_change_syntax_highlighting)
        self.text_area.bind('<Control-l>', self.tools_change_font)
        self.text_area.bind('<Control-g>', self.tools_change_color_scheme)
        self.text_area.bind('<Control-h>', self.help_about)

    def show_find_window(self, event=None):
        FindWindow(self.text_area)

    def edit_cut(self):
        '''Ctrl+X'''
        self.text_area.event_generate('<Control-x>')
        self.line_number.force_update()

    def edit_paste(self):
        '''Ctrl+V'''
        self.text_area.event_generate('<Control-v>')
        self.line_number.force_update()
        self.highlighter.force_highlight()

    def edit_copy(self):
        '''Ctrl+C'''
        self.text_area.event_generate('<Control-c>')

    def edit_select_all(self):
        '''Ctrl+A'''
        self.text_area.event_generate('<Control-a>')

    def edit_find_and_replace(self):
        '''Ctrl+F'''
        self.show_find_window()

    def file_new(self, event=None):
        '''Ctrl+N'''
        self.text_area.delete(1.0, tk.END)
        self.open_file = None
        self.line_number.force_update()

    def file_open(self, event=None):
        '''Ctrl+O'''
        file_to_open = filedialog.askopenfilename()
        if file_to_open:
            self.open_file = file_to_open
            self.text_area.display_file_contents(file_to_open)
            self.highlighter.force_highlight()
            self.line_number.force_update()

    def file_save(self, event=None):
        '''Ctrl+S'''
        current_file = self.open_file if self.open_file else None
        if not current_file:
            current_file = filedialog.asksaveasfilename()
        if current_file:
            contents = self.text_area.get(1.0, tk.END)
            with open(current_file, 'w') as file:
                file.write(contents)

    def load_syntax_highlighting_file(self):
        syntax_file = filedialog.askopenfilename(filetypes=[('YAML files',('*.yaml','*.yml'))])
        if syntax_file:
            self.highlighter.clear_highlight()
            self.highlighter = Highlighter(self.text_area, syntax_file)
            self.highlighter.force_highlight()

    def tools_change_syntax_highlighting(self, event=None):
        '''Ctrl+M'''
        self.load_syntax_highlighting_file()

    def update_font(self):
        self.load_font_file('schemes/font.yaml')
        self.text_area.configure(font=(self.font_family, self.font_size))

    def load_font_file(self, file_path):
        with open(file_path,'r') as stream:
            try:
                config = yaml.safe_load(stream)
            except yaml.YAMLError as error:
                print(error)
                return
        self.font_family = config['family']
        self.font_size = config['size']

    def change_font(self):
        FontChooser(self)

    def tools_change_font(self, event=None):
        '''Ctrl+L'''
        self.change_font()

    def apply_color_scheme(self, foreground, background, text_foreground, text_background):
        self.background = background
        self.foreground = foreground
        self.text_area.configure(fg=text_foreground, bg=text_background)
        for menu in self.all_menus:
            menu.configure(bg=self.background, fg=self.foreground)
        self.configure_ttk_elements()

    def configure_ttk_elements(self):
        style = ttk.Style()
        style.configure('editor.TLabel', foreground=self.foreground, background=self.background)
        style.configure('editor.TButton', foreground=self.foreground, background=self.background, relief='flat')
        '''
        Ttk button styles have only few predefined styles that's why background stays the same.
        '''

    def change_color_scheme(self):
        ColorChooser(self)

    def tools_change_color_scheme(self, event=None):
        '''Ctrl+G'''
        self.change_color_scheme()

    def show_about_page(self):
        msg.showinfo("About", "My text editor, written in Python3.9 using tkinter! Created by KN with the book"
                              " 'Tkinter GUI Programming by Example'")

    def help_about(self, event=None):
        '''Ctrl+H'''
        self.show_about_page()

if __name__=='__main__':
    mw = MainWindow()
    mw.mainloop()