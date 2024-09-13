from Transformacion import Datos_Trans
from Ordenamientos import Algoritmos

class Funcionamientos:
    def __init__(self):
        self.dataset = []
        self.numeric_columns = []
        self.sorting_algorithms = {
            'QuickSort': Algoritmos.quicksort,
            'MergeSort': Algoritmos.mergesort
        }

    def cargar_datos(self, consumer):
        try:
            self.dataset = consumer.Consumo()
            if not self.dataset or not isinstance(self.dataset, list):
                raise ValueError("No se han cargado datos de la API o los datos no están en formato de lista.")

            if not self.dataset:
                raise ValueError("El conjunto de datos está vacío.")

            columns = list(self.dataset[0].keys())
            self.numeric_columns = [col for col in columns if self.es_numero(self.dataset[0][col])]
            self.dataset = Datos_Trans.convierte_a_numero(self.dataset, self.numeric_columns)
            return columns

        except Exception as e:
            raise RuntimeError(f"Error al cargar los datos: {e}")

    def es_numero(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False

    def actualizar_tabla(self, table, columns):
        table["columns"] = columns
        table.heading("#0", text="")

        for col in columns:
            table.heading(col, text=col)
            table.column(col, width=100, anchor='w')

        table.delete(*table.get_children())

        for row in self.dataset:
            table.insert('', 'end', values=[row.get(col, '') for col in columns])

    def organizar_datos(self, selected_variable, selected_algorithm):
        if not self.dataset:
            raise ValueError("No hay datos para ordenar.")

        if selected_variable not in self.numeric_columns:
            raise ValueError("La variable seleccionada no es numérica.")

        if selected_algorithm not in self.sorting_algorithms:
            raise ValueError("El algoritmo seleccionado no es reconocido.")

        key_func = lambda item: float(item.get(selected_variable, 0))

        try:
            sorting_algorithm = self.sorting_algorithms[selected_algorithm]
            self.dataset = sorting_algorithm(self.dataset, key_func)
            return list(self.dataset[0].keys())  # Retornar columnas actualizadas
        except Exception as e:
            raise RuntimeError(f"Falló la ordenación: {e}")