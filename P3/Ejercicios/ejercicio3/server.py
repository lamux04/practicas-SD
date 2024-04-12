import json
from bottle import get, post, put, request, response, run

hotel = []

@get('/habitacion')
def getHabitaciones():
    response.headers['Content-Type'] = 'application/json'
    return json.dumps(hotel)

@post('/habitacion')
def postHabitacion():
    try:
        data = json.load(request.body)
    except:
        raise ValueError

    nuevaHabitacion = {
        'identificador': str(len(hotel)),
        'plazas': data['plazas'],
        'equipamiento': data['equipamiento'],
        'ocupada': False
    }

    hotel.append(nuevaHabitacion)

    response.headers['Content-Type'] = 'application/json'
    return json.dumps(nuevaHabitacion)

@put('/habitacion/<id:int>')
def putHabitacion(id):
    response.headers['Content-Type'] = 'application/json'
    
    try:
        data = json.load(request.body)
    except:
        raise ValueError
    
    for i in hotel:
        if i['identificador'] == str(id):
            i['plazas'] = data['plazas']
            i['equipamiento'] = data['equipamiento']
            return json.dumps(i)
    response.status = 400
    return json.dumps({'error': 'bad request'})
        
@get('/habitacion/<id:int>')
def getHabitacion(id):
    response.headers['Content-Type'] = 'application/json'
    for i in hotel:
        if i['identificador'] == str(id):
            return json.dumps(i)
    response.status = 400
    return json.dumps({'error': 'bad request'})

@get('/habitacion/<ocupada:re:[a-z]+>')
def getHabitacionOcupadaONo(ocupada):
    response.headers['Content-Type'] = 'application/json'
    if ocupada == 'ocupadas':
        habitaciones = []
        for i in hotel:
            if i['ocupada']:
                habitaciones.append(i)
        return json.dumps(habitaciones)
    elif ocupada == 'desocupadas':
        habitaciones = []
        for i in hotel:
            if not i['ocupada']:
                habitaciones.append(i)
        return json.dumps(habitaciones)
    else:
        response.status = 400
        return json.dums({'error': 'bad request'})
    
run(host='localhost', port=65000)