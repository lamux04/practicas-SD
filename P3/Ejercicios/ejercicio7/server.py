import json
from bottle import get, post, put, delete, request, response, run

reservas = [
    {
        'id': 0,
        'pista': 3,
        'inicio': 7,
        'fin': 8,
        'jugador': 'Javier'
    }
]

id_reserva = 1

@post('/nuevaReserva')
def nuevaReserva():
    global id_reserva
    response.headers['Content-Type'] = 'application/json'
    try:
        data = json.load(request.body)
    except:
        raise ValueError
    
    if data['inicio'] >= data['fin']:
        response.status = 400
        return json.dumps({'error': 'inicio >= fin'})

    for i in reservas:
        if i['pista'] == int(data['pista']):
            if not (int(data['inicio']) >= 7 and int(data['inicio']) <= 22):
                return json.dumps({'error': 'Pista cerrada a esa hora'})
            if not (int(data['fin']) >= 8 and int(data['fin']) <= 23):
                return json.dumps({'error': 'Pista cerrada a esa hora'})
            if int(data['inicio']) >= i['inicio'] and int(data['inicio']) < i['fin']:
                return json.dumps({'error': 'Pista ya ocupada a esa hora'})
            if int(data['fin']) > i['inicio'] and int(data['fin']) <= i['fin']:
                return json.dumps({'error': 'Pista ya ocupada a esa hora'})
    
    nuevaReserva = {
        'id': id_reserva,
        'pista': int(data['pista']),
        'inicio': int(data['inicio']),
        'fin': int(data['fin']),
        'jugador': data['jugador']
    }


    reservas.append(nuevaReserva)
    print(reservas)
    id_reserva += 1
    return json.dumps(nuevaReserva)

@delete('/cancelar/<id:int>')
def cancelarReserva(id):
    response.headers['Content-Type'] = 'application/json'
    index = 0
    for i in reservas:
        if i['id'] == id:
            reservas.pop(index)
            return json.dumps(reservas)
        index += 1
    response.status = 404
    return json.dumps({'error': 'Not found'})

@get('/mostrar/<num:int>')
def mostrarReservas(num):
    response.headers['Content-Type'] = 'application/json'
    res = []
    for i in reservas:
        if i['pista'] == num:
            res.append(i)
    return json.dumps(res)

run(host='localhost', port=65000)