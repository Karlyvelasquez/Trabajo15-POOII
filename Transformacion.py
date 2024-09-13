class Datos_Trans:
    @staticmethod
    def convierte_a_numero(dato, numeri_column):
        for item in dato:
            for column in numeri_column:
                try:
                    item[column] = int(item[column])
                except ValueError:
                    pass  
        return dato