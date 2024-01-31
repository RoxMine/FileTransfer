import shutil
import os
from customtkinter import CTk, CTkEntry, CTkLabel, CTkButton, filedialog

def move_file():
    try:
        source_path = source_entry.get()
        destination_path = destination_entry.get()

        shutil.copy2(source_path, destination_path)
        os.remove(source_path)
    except Exception as e:
        print(f"{e}")

def select_source_file():
    file_path = filedialog.askopenfilename(title="Choose Source Data")
    if file_path:
        source_entry.delete(0, 'end')
        source_entry.insert(0, file_path)

def select_destination_folder():
    folder_path = filedialog.askdirectory(title="Choose Destination Folder")
    if folder_path:
        destination_entry.delete(0, 'end')
        destination_entry.insert(0, folder_path)

root = CTk()
root.title(" ")
root.geometry("200x235")

source_entry = CTkEntry(root, width=150, placeholder_text="Source Path...")
source_entry.pack(pady=5)
source_button = CTkButton(root, text="Choose", command=select_source_file)
source_button.pack(pady=5)

empty_label = CTkLabel(root, text=" ", height=1)
empty_label.pack()

destination_entry = CTkEntry(root, width=150, placeholder_text="Destination Path...")
destination_entry.pack(pady=5)
destination_button = CTkButton(root, text="Choose", command=select_destination_folder)
destination_button.pack(pady=5)

move_button = CTkButton(root, text="Move File", width=175, command=move_file)
move_button.pack(pady=20)

root.mainloop()