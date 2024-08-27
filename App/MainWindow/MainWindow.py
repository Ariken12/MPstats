import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog as tkfd 
import MainWindow.Constants as const


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Выгрузка Конкурентов')
        self.frame_first_line = tk.Frame(self)
        self.label_input_filename = tk.Label(self.frame_first_line, text=const.INPUT_FILENAME)
        self.entry_input_filename = tk.Entry(self.frame_first_line, state='disabled')
        self.button_input_filename = tk.Button(self.frame_first_line, text=const.CHOOSE_FILENAME, command=lambda:self.choose_filename('input'))
        self.frame_second_line = tk.Frame(self)
        self.label_output_filename = tk.Label(self.frame_second_line, text=const.OUTPUT_FILENAME)
        self.entry_output_filename = tk.Entry(self.frame_second_line, state='disabled')
        self.button_output_filename = tk.Button(self.frame_second_line, text=const.CHOOSE_FILENAME, command=lambda:self.choose_filename('output'))
        self.frame_third_line = tk.Frame(self)
        self.label_input_num_of_days = tk.Label(self.frame_third_line, text=const.NUM_OF_DAYS_FOR_ANALYSIS)
        self.spinbox_input_num_of_days = ttk.Spinbox(self.frame_third_line, from_=1, to=365)
        self.frame_fourth_line = tk.Frame(self)
        self.label_token = tk.Label(self.frame_fourth_line, text=const.TOKEN)
        self.entry_token = tk.Entry(self.frame_fourth_line)
        self.label_status = tk.Label(self, text=const.STATUS)
        self.text_status = tk.Text(self, height=const.STATUS_HEIGHT)
        self.button_start = tk.Button(self, text=const.START, command=self.start)
        self._pack()

    def _pack(self):   
        '''Функция была написана с помощью AI :DD'''
        # Упаковка первого фрейма
        self.frame_first_line.pack(fill=tk.BOTH, expand=True)
        self.label_input_filename.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.entry_input_filename.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.button_input_filename.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Упаковка второго фрейма
        self.frame_second_line.pack(fill=tk.BOTH, expand=True)
        self.label_output_filename.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.entry_output_filename.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.button_output_filename.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Упаковка третьего фрейма
        self.frame_third_line.pack(fill=tk.BOTH, expand=True)
        self.label_input_num_of_days.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.spinbox_input_num_of_days.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Упаковка четвертого фрейма
        self.frame_fourth_line.pack(fill=tk.BOTH, expand=True)
        self.label_token.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.entry_token.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Упаковка статуса
        self.label_status.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.text_status.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def choose_filename(self, io='input'):
        print(io)
        filename = tkfd.askopenfilename()
        if io == 'input':
            entry = self.entry_input_filename
        elif io == 'output':
            entry = self.entry_output_filename
        entry['state'] = tk.NORMAL
        entry.delete(0, tk.END)
        entry.insert(0, filename)
        entry['state'] = tk.DISABLED        

    def start(self):
        pass