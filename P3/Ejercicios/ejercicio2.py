import json
from bottle import post, request, response, run

mis_elementos = []

@post('/inserta')
def post():
    try:
        data = json.load(request.body)
        print(data)
    except:
        raise ValueError
    
    response.headers['Content-Type'] = 'application/json'
    
    if not 'elemento' in data.keys():
        response.status = 400
        return json.dumps({ 'Error': 'Elemento no encontrada' })

    numero = int(data['elemento'])
    if (not numero in mis_elementos):
        mis_elementos.append(numero)
    
    return json.dumps({
        'mis_elementos': mis_elementos
    })

run(host='localhost', port=8084)