from datetime import datetime

def normalizador_fechas(fecha, patron_in, patron_out='%d-%m-%Y'):
    objeto_fecha = datetime.strptime(fecha, patron_in)
    fecha_normalizada = datetime.strftime(objeto_fecha, patron_out)
    print(fecha, '-->', objeto_fecha, '-->', fecha_normalizada)
    return fecha_normalizada

def constructorFecha(fecha):
    meses = ['ENERO','FEBRERO','MARZO','ABRIL','MAYO','JUNIO','JULIO','AGOSTO','SEPTIEMBRE','OCTUBRE','NOVIEMBRE','DICIEMBRE']
    lista = fecha.split('/')
    mes = lista[1].upper()
    nro_mes = meses.index(mes) + 1
    fecha_aux = lista[0] + str(nro_mes) + lista[2]
    return fecha_aux
###Acá empieza el programa en sí mismo###
fecha = '13 days after 2019'
try:
    fecha_normalizada = normalizador_fechas(fecha, '%Y%d%m')
except:
    try:
        fecha_normalizada = normalizador_fechas(fecha, '%Y-%d-%m')
    except:
        try:
            fecha_normalizada = normalizador_fechas(fecha, '%d/%b/%Y')
        except:
            fecha_normalizada ='N/A'
            print(fecha_normalizada)

