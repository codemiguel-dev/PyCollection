import tkinter as tk
from tkinter import filedialog, messagebox

import pdfplumber
from reportlab.pdfgen import canvas


class PDFEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Editor de PDF")

        self.pdf_text = tk.Text(self.root, wrap="word", width=60, height=20)
        self.pdf_text.pack(padx=10, pady=10)

        self.open_button = tk.Button(self.root, text="Abrir PDF", command=self.open_pdf)
        self.open_button.pack(pady=5)

        self.save_button = tk.Button(
            self.root, text="Guardar como PDF", command=self.save_pdf
        )
        self.save_button.pack(pady=5)

        self.pdf_file_path = ""

    def open_pdf(self):
        file_path = filedialog.askopenfilename(filetypes=[("Archivos PDF", "*.pdf")])
        if file_path:
            self.pdf_file_path = file_path
            self.load_pdf(file_path)

    def load_pdf(self, file_path):
        try:
            with pdfplumber.open(file_path) as pdf:
                text = "\n".join(page.extract_text() or "" for page in pdf.pages)

            if text.strip():
                self.pdf_text.delete(1.0, tk.END)
                self.pdf_text.insert(tk.END, text)
            else:
                messagebox.showerror("Error", "No se pudo extraer el texto del PDF.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo abrir el PDF: {e}")

    def save_pdf(self):
        output_path = filedialog.asksaveasfilename(
            defaultextension=".pdf", filetypes=[("Archivos PDF", "*.pdf")]
        )
        if output_path:
            try:
                c = canvas.Canvas(output_path)
                text = self.pdf_text.get(1.0, tk.END)

                lines = text.split("\n")
                y_position = 800  # Posición inicial en el PDF

                for line in lines:
                    c.drawString(50, y_position, line)
                    y_position -= 15  # Espaciado entre líneas

                c.save()
                messagebox.showinfo("Éxito", "PDF guardado correctamente.")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo guardar el PDF: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = PDFEditor(root)
    root.mainloop()
