import datetime
from itertools import starmap


class Tarea:
    def __init__(self, nombre: str):
        self.nombre = nombre

    def __str__(self):
        return "{}".format(self.nombre)


class Recordatorio:

    def __init__(self, nombre: str, hora, fecha):
        self.nombre = nombre
        self.hora = hora
        self.fecha = fecha
        self.tareas = []

    def agregar_tarea(self, nombre_tarea: str):
        tarea: Tarea(nombre_tarea)
        self.tareas.append(tarea)

    def eliminar_tarea(self, numero: int):
        self.tareas.pop(numero)

    def __str__(self):
        return "{} {} {} {}".format(self.nombre, self.fecha, self.hora, self.mostrar_tareas())

    def mostrar_tareas(self):
        return "\ntareas:\n".join(starmap('{}: {}'.format, enumerate(self.tareas)))


def crear_recordatorio(recordatorios:list):
    nombre: input("Ingrese el nombre del recordatotio")
    fecha: input("ingrese la fecha del recordatorio")
    hora: input("ingrese la hora del recordatorio")
    recordatorio = Recordatorio(nombre, hora, fecha)
    while True:
        agregar_tarea(recordatorio)
        opcion = input("Desea agregar otra tarea (y/n").lower()
        while opcion != 'y' and opcion != 'n':
            opcion = input("Opción inválida. Desea agregar otra tarea (y/n").lower()
        if opcion == 'n':
            break
    recordatorios.append(recordatorio)


def mostrar_lista_recordatorios(recordatorios):
    print("\nrecordatorios:\n".join(starmap('{}: {}'.format, enumerate(recordatorios))))


def eliminar_recordatorio_manual(recordatorios: list):
    mostrar_lista_recordatorios(recordatorios)
    indice = int(input("Indique el recordatorio que desea eliminar"))
    recordatorios.pop(indice)
    # validar indice


def agregar_tarea(recordatorio):
    nombre_tarea = input("Ingrese el nombre de la tarea")
    recordatorio.agregar_tarea(nombre_tarea)

def eliminar_tarea(recordatorio):
    print(recordatorio.mostrar_tareas())
    indice = int(input("Indique el recordatorio que desea eliminar"))
    recordatorio.eliminar_tarea(indice)


def ver_recordatorios(recordatorios):
    print ("\nrecordatorios:\n".join(starmap('{}: {}'.format, enumerate(recordatorios))))

def actualizar_recordatorio(recordatorios):
    mostrar_lista_recordatorios(recordatorios)
    indice = int(input("Indique el recordatorio que desea modificar"))
    nombre: input("Ingrese el nuevo nombre del recordatotio")
    fecha: input("ingrese la nueva fecha del recordatorio")
    hora: input("ingrese la nueva hora del recordatorio")
    recordatorio = recordatorios[indice]
    recordatorio.nombre = nombre
    recordatorio.fecha = fecha
    recordatorio.hora = hora
    while True:
        opcion = int(input("seleccione:\n1 para agregar tarea\n2 para eliminar tarea\n3 para salir"))
        while opcion > 3 and opcion < 2:
            opcion = input(
                "opcion invalida. Seleccione:\n1 para agregar tarea\n2 para eliminar tarea\n3 para salir").lower()
        if opcion == '3':
            break
        elif opcion == 1:
            agregar_tarea(recordatorio)
        elif opcion == 2:
            eliminar_tarea(recordatorio)


def main():
    fecha = datetime.datetime.now()
    year = fecha.year
    month = fecha.month
    day = fecha.day
    recordatorios = []

    opcion = 0
    continuar = 0
    while continuar == 0:
        opcion = int(input('''***MENU***\nIngrese:===>\n
                        1. Crear recordatorio
                        2. Eliminar recordatorios manual
                        3. Actualizar recordatorios
                        4. Ver lista de recordatorios
                        5.Desplegar dia siguiente.
                        ===>'''))
        # SU CODIGO VA AQUI
        if opcion == 1:
            crear_recordatorio(recordatorios)
        elif opcion == 2:
            eliminar_recordatorio_manual(recordatorios)
        elif opcion == 3:
            actualizar_recordatorio(recordatorios)
        elif opcion == 4:
            mostrar_lista_recordatorios(recordatorios)

        while opcion == 5:

            # SU CODIGO VA AQUI

            if month == 2:
                # print('febrero')
                if day + 1 == 29:
                    day = 1
                    month = month + 1
                else:
                    day += 1

            elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
                # print('enero,marzo,mayo,julio,agosto,octubre,diciembre')
                if day + 1 == 32:
                    day = 1

                    if month + 1 == 13:
                        month = 1
                        year = year + 1
                    else:
                        month = month + 1
                else:
                    day += 1

            elif month == 4 or month == 6 or month == 9 or month == 11:
                # print('abril, junio,septiembre,noviembre')
                if day + 1 == 31:
                    day = 1
                    month = month + 1
                else:
                    day += 1
            print(datetime.datetime(year, month, day))
            opcion = int(input(
                '"Ingresa 5 para pasar al siguiente dia, de lo contrario ingresa cualquier otro numero.\n ===> '))

        continuar = int(input(
            "Ingresa 0 para escoger otra opcion del menu, de lo contrario ingresa cualquier otro numero.\n ===> "))
main ()