from bottle import get, post, put, request, response, run
import json

usuarios = []

@post('/nuevoUsuario')
def postUsuario():
    try:
        data = json.load(request.body)
    except:
        raise ValueError
    
    nuevoUsuario = {
        'username': data['username'],
        'clave': data['clave'],
        'activada': False,
        'correo': data['correo'],
        'nombre': data['nombre'],
        'apellidos': data['apellidos']
    }

    response.headers['Content-Type'] = 'application/json'
    for i in usuarios:
        if i['username'] == nuevoUsuario['username'] or i['correo'] == nuevoUsuario['correo']:
            response.status = 400
            return json.dumps({'error': 'bad request'})
        
    usuarios.append(nuevoUsuario)
    return json.dumps(nuevoUsuario)

@put('/activarCuenta/<username>')
def activarCuenta(username):
    response.headers['Content-Type'] = 'application/json'
    for i in usuarios:
        if i['username'] == username:
            i['activada'] = True
            return json.dumps(i)
    response.status = 400
    return json.dumps({'error': 'bad request'})

@get('/busquedaUsuarios/<cad>')
def busquedaUsuarios(cad):
    filtrados = []

    for i in usuarios:
        if cad in i['username'] or cad in i['correo']:
            filtrados.append(i)
    
    response.headers['Content-Type'] = 'application/json'
    return json.dumps(filtrados)
    
run(host='localhost', port=65000)