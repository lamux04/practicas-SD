from bottle import run, post, put, get, request, response
import json

aviones = [
    {
        'matricula': '123456',
        'fecha llegada': '23/04/2024',
        'hora llegada': '23:45',
        'pista llegada': 10,
        'fecha salida': '20/05/2024',
        'hora llegada': '12:00',
        'pista salida': 10
    }
]

def calcularPista():
    veces = {
        '10': 0,
        '30': 0
    }
    
    for avion in aviones:
        if avion['fecha salida'] == None:
            veces[avion['pista llegada']] += 1

    if veces['10'] > veces['30']:
        return 30
    else:
        return 10


@post('/registrarAterrizaje')
def registrarAterrizaje():
    try:
        data = json.load(request.body)
    except:
        raise ValueError
    
    nuevoAvion = {
        'matricula': data['matricula'],
        'fecha llegada': data['fecha llegada'],
        'hora llegada': data['hora llegada'],
        'pista llegada': calcularPista(),
        'fecha salida': None,
        'hora llegada': None,
        'pista salida': None
    }

    aviones.append(nuevoAvion)

    response.headers['Content-Type'] = 'application/json'

    return json.dumps(nuevoAvion)


@put('/despegue/<matricula>')
def despegarAvion(matricula):
    try:
        data = json.load(request.body)
    except:
        raise ValueError
    
    encontrado = False

    
    for avion in aviones:
        if str(avion['matricula']) == str(matricula) and avion['fecha salida'] == None:
            navion = avion
            encontrado = True
            break

    response.headers['Content-Type'] = 'application/json'

    if not encontrado:
        response.status_code = 404
        return json.dumps({'error': 'El avion no existe'})
    
    navion['fecha salida'] = data['fecha salida']
    navion['hora salida'] = data['hora salida']
    navion['pista salida'] = calcularPista()

    return json.dumps(navion)

@get('/getAviones')
def getAviones():
    response.headers['Content-Type'] = 'application/json'
    return json.dumps(aviones)

run(host='localhost', port=65000)
