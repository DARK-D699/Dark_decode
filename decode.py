import tkinter as tk
from tkinter import messagebox
import base64

class Base64DecoderGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Base64 Decoder")
        self.root.geometry("600x400")

        # Input label and text box
        self.label_input = tk.Label(root, text="Enter Base64 Encoded String:")
        self.label_input.pack(pady=10)
        
        self.input_text = tk.Text(root, height=5, width=50)
        self.input_text.pack(pady=10)

        # Output label and text box
        self.label_output = tk.Label(root, text="Decoded String:")
        self.label_output.pack(pady=10)
        
        self.output_text = tk.Text(root, height=5, width=50)
        self.output_text.pack(pady=10)
        self.output_text.config(state='disabled')  # Make output read-only

        # Buttons
        self.decode_button = tk.Button(root, text="Decode", command=self.decode_base64)
        self.decode_button.pack(pady=5)
        
        self.paste_button = tk.Button(root, text="Paste", command=self.paste_to_input)
        self.paste_button.pack(pady=5)
        
        self.copy_button = tk.Button(root, text="Copy Decoded", command=self.copy_to_clipboard)
        self.copy_button.pack(pady=5)
        
        self.exit_button = tk.Button(root, text="Exit", command=root.quit)
        self.exit_button.pack(pady=5)

    def decode_base64(self):
        try:
            # Get input text
            encoded_str = self.input_text.get("1.0", tk.END).strip()
            # Decode Base64
            decoded_bytes = base64.b64decode(encoded_str)
            decoded_str = decoded_bytes.decode('utf-8')
            
            # Update output text
            self.output_text.config(state='normal')  # Enable editing
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, decoded_str)
            self.output_text.config(state='disabled')  # Disable editing again
        except Exception as e:
            messagebox.showerror("Error", f"Invalid Base64 string: {str(e)}")

    def paste_to_input(self):
        try:
            # Get clipboard content and insert into input text box
            clipboard_content = self.root.clipboard_get()
            self.input_text.delete("1.0", tk.END)
            self.input_text.insert(tk.END, clipboard_content)
        except tk.TclError:
            messagebox.showwarning("Warning", "Clipboard is empty or inaccessible!")

    def copy_to_clipboard(self):
        # Get decoded text and copy to clipboard
        decoded_str = self.output_text.get("1.0", tk.END).strip()
        if decoded_str:
            self.root.clipboard_clear()  # Clear clipboard
            self.root.clipboard_append(decoded_str)  # Append decoded text
            messagebox.showinfo("Success", "Decoded text copied to clipboard!")
        else:
            messagebox.showwarning("Warning", "No decoded text to copy!")

# Create and run the GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = Base64DecoderGUI(root)
    root.mainloop()
