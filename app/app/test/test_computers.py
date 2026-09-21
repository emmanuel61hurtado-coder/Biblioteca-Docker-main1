def test_computer_model(computer):
    assert computer.idComputer is not None
    assert computer.brandComputer == "Dell"
    assert computer.modelComputer == "Latitude 5420"
    assert computer.statusComputer == "Active"
    assert repr(computer) == f'<Computer {computer.idComputer} - Dell Latitude 5420>'

def test_index(client):
    response = client.get('/computers/')
    assert response.status_code == 200
    assert "Lista de Computadoras".encode('utf-8') in response.data

def test_add_computer(client):
    response = client.post('/computers/add', data={
        'brandComputer': 'HP',
        'modelComputer': 'ProBook',
        'statusComputer': 'Active'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert "HP".encode('utf-8') in response.data

def test_edit_computer(client, computer):
    response = client.post(f'/computers/update/{computer.idComputer}', data={
        'brandComputer': 'Lenovo',
        'modelComputer': 'ThinkPad',
        'statusComputer': 'Active'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert "Lenovo".encode('utf-8') in response.data

def test_delete_computer(client, computer):
    response = client.post(f'/computers/delete/{computer.idComputer}', follow_redirects=True)
    assert response.status_code == 200
    assert "Lista de Computadoras".encode('utf-8') in response.data
