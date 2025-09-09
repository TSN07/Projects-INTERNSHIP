import tkinter as tk
from tkinter import filedialog, messagebox
from stegano import lsb

def hide_message():
    img_path = filedialog.askopenfilename(title="Select Image")
    if not img_path:
        return
    msg = message_entry.get()
    if not msg:
        messagebox.showwarning("Warning", "Please enter a secret message!")
        return
    output_path = filedialog.asksaveasfilename(defaultextension=".png", title="Save Hidden Image As")
    if not output_path:
        return
    lsb.hide(img_path, message=msg).save(output_path)
    messagebox.showinfo("Success", f"Message hidden and saved to {output_path}")

def reveal_message():
    img_path = filedialog.askopenfilename(title="Select Image with Hidden Message")
    if not img_path:
        return
    secret_msg = lsb.reveal(img_path)
    if secret_msg:
        messagebox.showinfo("Hidden Message", secret_msg)
    else:
        messagebox.showinfo("Hidden Message", "No hidden message found.")

root = tk.Tk()
root.title("Steganography GUI")

tk.Label(root, text="Enter secret message to hide:").pack()
message_entry = tk.Entry(root, width=50)
message_entry.pack()

tk.Button(root, text="Hide Message", command=hide_message).pack(pady=10)
tk.Button(root, text="Reveal Message", command=reveal_message).pack(pady=10)

root.mainloop()
