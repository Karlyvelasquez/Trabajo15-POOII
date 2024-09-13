from Interfaz import Application
from Funcionamiento import Funcionamientos

def main():
    api_url = "https://www.datos.gov.co/resource/s87b-tjcc.json"
    Data_fun = Funcionamientos()
    app = Application(api_url=api_url, fun_data= Data_fun)
    app.mainloop()

if __name__ == "__main__":
    main()