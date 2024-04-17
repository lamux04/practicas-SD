import json
from bottle import get, put, post, request, response, run

vehiculos = [
    {
        'id': 0,
        'marca': 'Ford',
        'modelo': 'Fiesta',
        'alquilado': True,
        'usuario': 0
    }
]

id_vehiculo = 1
id_cliente = 1

clientes = [
    {
        'id': 0,
        'n_veces': 1
    }
]

@get('/')
def getAll():
    response.headers['Content-Type'] = 'application/json'
    return json.dumps({'vehiculos': vehiculos, 'clientes': clientes})

@post('/registroUsuario')
def registroUsuario():
    global id_cliente
    nuevoCliente = {
        'id': id_cliente,
        'n_veces': 0
    }
    id_cliente += 1
    clientes.append(nuevoCliente)
    response.headers['Content-Type'] = 'application/json'
    return json.dumps(nuevoCliente)

@post('/registroVehiculo')
def registroVehiculo():
    global id_vehiculo
    try:
        data = json.load(request.body)
    except:
        raise ValueError
    
    nuevoVehiculo = {
        'id': id_vehiculo,
        'marca': data['marca'],
        'modelo': data['modelo'],
        'alquilado': False,
        'usuario': 0
    }

    id_vehiculo += 1
    
    vehiculos.append(nuevoVehiculo)
    response.headers['Content-Type'] = 'application/json'
    return json.dumps(nuevoVehiculo)

@put('/alquilarVehiculoLibre/<id_usuario:int>')
def alquilarVehiculoLibre(id_usuario):
    response.headers['Content-Type'] = 'application/json'
    # Buscamos vehiculo libre
    vehiculoLibre = None
    for i in vehiculos:
        if not i['alquilado']:
            vehiculoLibre = i
    if vehiculoLibre == None:
        return json.dumps({'error': 'No hay vehiculos libres'})
    
    for i in clientes:
        if i['id'] == id_usuario:
            vehiculoLibre['alquilado'] = True
            vehiculoLibre['usuario'] += 1
            i['n_veces'] += 1
            return json.dumps({'usuario': i, 'vehiculo': vehiculoLibre})
        
    response.status = 404
    return json.dumps({'error': 'Usuario no encontrado'})

@put('/alquilarVehiculo/<id_usuario:int>/<id_vehiculo:int>')
def alquilarVehiculoLibre(id_usuario, id_vehiculo):
    response.headers['Content-Type'] = 'application/json'
    # Buscamos vehiculo libre
    vehiculoLibre = None
    for i in vehiculos:
        if i['id'] == id_vehiculo:
            vehiculoLibre = i
    if vehiculoLibre == None:
        response.status = 404
        return json.dumps({'error': 'El vehiculo no existe'})
    
    if vehiculoLibre['alquilado']:
        return json.dumps({'error': 'El vehiculo no esta libre'})

    for i in clientes:
        if i['id'] == id_usuario:
            vehiculoLibre['alquilado'] = True
            vehiculoLibre['usuario'] += 1
            i['n_veces'] += 1
            return json.dumps({'usuario': i, 'vehiculo': vehiculoLibre})
        
    response.status = 404
    return json.dumps({'error': 'Usuario no encontrado'})
    
run(host='localhost', port=65000)