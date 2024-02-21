from datetime import datetime


def calcula_edad(fecha_nacimiento):
    # Convertir la fecha de nacimiento a un objeto datetime
    fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%Y-%m-%d")
    # Obtener la fecha actual
    fecha_actual = datetime.now()

    # Calcular la diferencia de años
    edad = fecha_actual.year - fecha_nacimiento.year

    # Restar un año si la fecha de nacimiento aún no ha ocurrido este año
    if (fecha_actual.month, fecha_actual.day) < (
        fecha_nacimiento.month,
        fecha_nacimiento.day,
    ):
        edad -= 1

    # Sumar un año si la fecha actual es mayor al 20 de junio del año actual
    if (fecha_actual.month, fecha_actual.day) > (6, 20):
        edad += 1

    return edad


def calcular_semestre(fecha_inicio):
    mes = datetime.now().month
    año = datetime.now().year

    fecha_inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d")

    transcurrido = (año - fecha_inicio.year) * 2

    x_semestre = {
        1: "primer",
        2: "segundo",
        3: "tercer",
        4: "cuarto",
        5: "quinto",
        6: "sexto",
        7: "septimo",
        8: "octavo",
        9: "noveno",
        10: "decimo",
    }
    if mes <= 6:
        transcurrido += 1
    else:
        transcurrido += 2

    semestre_actual = x_semestre[transcurrido]
    return semestre_actual
