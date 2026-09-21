def test_room_model(room):
    assert room.id is not None
    assert room.name == "Sala A"
    assert room.description == "Sala de estudio silenciosa"
    assert repr(room) == f'<Room {room.id} - Sala A>'

def test_index(client):
    response = client.get('/room/')
    assert response.status_code == 200
    assert "Lista de Salas".encode('utf-8') in response.data

def test_add_room(client):
    response = client.post('/room/add', data={
        'name': 'Sala B',
        'description': 'Sala de computo'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert "Sala B".encode('utf-8') in response.data

def test_edit_room(client, room):
    response = client.post(f'/room/edit/{room.id}', data={
        'name': 'Sala C',
        'description': 'Sala de conferencias'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert "Sala C".encode('utf-8') in response.data

def test_delete_room(client, room):
    response = client.get(f'/room/delete/{room.id}', follow_redirects=True)
    assert response.status_code == 200
    assert "Lista de Salas".encode('utf-8') in response.data
