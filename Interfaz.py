import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class Application(tk.Tk):
    def __init__(self, api_url, fun_data):
        super().__init__()
        self.api_url = api_url
        self.data_handler = fun_data
        self.initialize_gui()

    def initialize_gui(self):
        self.title("POOII")
        self.geometry("800x600")
        self.configure(bg="#2E2E2E")

        self.title_label = tk.Label(self, text="POOII", font=("Arial", 24, "bold"), fg="#FFFFFF", bg="#2E2E2E")
        self.title_label.pack(pady=20)

        self.load_button = tk.Button(self, text="Cargar Datos", command=self.cargar_datos, font=("Arial", 14), bg="#3A3A3A", fg="#FFFFFF", relief="flat")
        self.load_button.pack(pady=10, padx=20, fill='x')

        self.table = ttk.Treeview(self, columns=(), show='headings')
        self.table.pack(expand=True, fill='both', padx=20, pady=10)
        
        self.configure_styles()

        self.variable_label = tk.Label(self, text="Selecciona la variable numérica:", font=("Arial", 12), fg="#FFFFFF", bg="#2E2E2E")
        self.variable_label.pack(pady=5)
        self.variable_combo = ttk.Combobox(self, font=("Arial", 12))
        self.variable_combo.pack(pady=5, padx=20, fill='x')

        self.algorithm_label = tk.Label(self, text="Selecciona el algoritmo de ordenamiento:", font=("Arial", 12), fg="#FFFFFF", bg="#2E2E2E")
        self.algorithm_label.pack(pady=5)
        self.algorithm_combo = ttk.Combobox(self, values=list(self.data_handler.sorting_algorithms.keys()), font=("Arial", 12))
        self.algorithm_combo.pack(pady=5, padx=20, fill='x')

        self.sort_button = tk.Button(self, text="Ordenar Datos", command=self.organizar_datos, font=("Arial", 14), bg="#3A3A3A", fg="#FFFFFF", relief="flat")
        self.sort_button.pack(pady=10, padx=20, fill='x')

    def configure_styles(self):
        style = ttk.Style()
        style.configure("Treeview",
                        background="#FFFFFF",
                        foreground="#000000",
                        fieldbackground="#FFFFFF")
        style.configure("Treeview.Heading", font=("Arial", 12, "bold"), background="#4A4A4A", foreground="#FFFFFF")
        style.configure("TCombobox", fieldbackground="#3A3A3A", background="#3A3A3A", foreground="#FFFFFF")
        style.configure("TButton", background="#3A3A3A", foreground="#FFFFFF")
        style.map("TButton", background=[("active", "#555555")])

    def cargar_datos(self):
        try:
            from API import APIConsumo  # Importar aquí para evitar dependencias circulares
            consumer = APIConsumo(self.api_url)
            columns = self.data_handler.cargar_datos(consumer)
            self.actualizar_tabla(columns)
            self.variable_combo['values'] = self.data_handler.numeric_columns
        except RuntimeError as e:
            messagebox.showerror("Error", str(e))

    def actualizar_tabla(self, columns):
        self.data_handler.actualizar_tabla(self.table, columns)

    def organizar_datos(self):
        if not self.data_handler.dataset:
            messagebox.showwarning("Advertencia", "No hay datos para ordenar.")
            return

        selected_variable = self.variable_combo.get()
        selected_algorithm = self.algorithm_combo.get()

        try:
            columns = self.data_handler.organizar_datos(selected_variable, selected_algorithm)
            self.actualizar_tabla(columns)
        except ValueError as e:
            messagebox.showwarning("Advertencia", str(e))
        except RuntimeError as e:
            messagebox.showerror("Error", str(e))