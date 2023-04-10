import random
import tkinter as tk
from tkinter import filedialog

def count_lines(file_path):
    with open(file_path, mode="r") as file:

        for index, line in enumerate(file):
            pass

        # print("Total lines: {}".format(index+1,))
        return index+1

def read_line(file_path, line_no):
    with open(file_path, 'r') as fp:
        # lines to read

        # To store lines
        lines = []
        for i, line in enumerate(fp):
            # read line 4 and 7
            if i == line_no:
                lines.append(line.strip())
    # print(lines)
    return lines

def random_line_read(file_path, lines_count):
    random.seed()
    random_line_no = random.randint(0, lines_count-1) 
    random_line = read_line("events1.txt", random_line_no)
    return random_line_no, random_line


def browseFiles(inputtxt):
    import os
    filename = filedialog.askopenfilename(initialdir = os.getcwd(),
                                          title = "Select a File",
                                          filetypes = (("Text files",
                                                        "*.txt*"),
                                                       ("all files",
                                                        "*.*")))
      
    # Change label contents
    inputtxt.insert('end', filename)

def get_random_event(filename, output_label):
    filename = filename.replace('\n', '')
    lines_count = count_lines(filename)
    random_line_no, random_line = random_line_read(filename, lines_count)
    print('random_line {}: {}'.format(random_line_no+1, random_line[0]))

    output_label.delete('1.0', 'end')
    output_label.insert('end', random_line[0])

def main(): 


    root = tk.Tk()
    root.title("D&D event randomizer")
    message = tk.Label(root, text="D&D event randomizer")
   

    file_path_input_text = tk.Text(root, height = 1,
            width = 50,
            bg = "light yellow")

    event_input_text = tk.Text(root, height = 1,
            width = 50,
            bg = "light yellow")

    open_file_button = tk.Button(root, height = 1,
                 width = 20,
                 text ="Otwórz plik ze zdarzeniami",
                 command = lambda:browseFiles(file_path_input_text))

    randomize_button = tk.Button(root, height = 1,
                 width = 20,
                 text ="Losuj!",
                 command = lambda:get_random_event(file_path_input_text.get(1.0, 'end'), event_input_text))

    message.pack()
    open_file_button.pack()
    file_path_input_text.pack()
    randomize_button.pack()
    event_input_text.pack()


    
    root.mainloop()

if __name__ == '__main__':
    main()