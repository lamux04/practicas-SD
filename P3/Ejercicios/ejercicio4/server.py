import json
from bottle import get, post, put, request, response, run

personal = []

@get('/miembros')
def getHabitaciones():
    response.headers['Content-Type'] = 'application/json'
    return json.dumps(personal)

@post('/nuevoMiembro')
def postHabitacion():
    try:
        data = json.load(request.body)
    except:
        raise ValueError

    nuevoMiembro = {
        'dni': data['dni'],
        'nombre': data['nombre'],
        'correo': data['correo'],
        'categoria': data['categoria'],
        'asignaturas': data['asignaturas']
    }
    response.headers['Content-Type'] = 'application/json'

    for i in personal:
        if i['dni'] == nuevoMiembro['dni']:
            return json.dumps({'error': 'el dni ya existe'})
    personal.append(nuevoMiembro)

    return json.dumps(nuevoMiembro)

@put('/modificarMiembro/<dni>')
def putHabitacion(dni):
    response.headers['Content-Type'] = 'application/json'
    
    try:
        data = json.load(request.body)
    except:
        raise ValueError
    
    for i in personal:
        if i['dni'] == str(dni):
            i['nombre'] = data['nombre']
            i['correo'] = data['correo']
            i['categoria'] = data['categoria']
            i['asignaturas'] =  data['asignaturas']
            return json.dumps(i)
        
    response.status = 404
    return json.dumps({'error': 'el dni no existe'})
        
@get('/miembro/<dni>')
def getHabitacion(dni):
    response.headers['Content-Type'] = 'application/json'
    for i in personal:
        if i['dni'] == str(dni):
            return json.dumps(i)
    response.status = 404
    return json.dumps({'error': 'not found'})

@get('/miembro/categoria/<categoria>')
def getHabitacionOcupadaONo(categoria):
    response.headers['Content-Type'] = 'application/json'
    
    miembros = []

    for i in personal:
        if i['categoria'] == str(categoria):
            miembros.append(i)

    return json.dumps(miembros)
    
run(host='localhost', port=65000)