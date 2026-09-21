def test_cloan_model(cloan, computer, user):
    assert cloan.idLoan is not None
    assert cloan.computerId == computer.idComputer
    assert cloan.userId == user.idUser
    assert cloan.status == "Active"
    assert repr(cloan) == f'<ComputerLoan {cloan.idLoan} of Computer {computer.idComputer} to User {user.idUser}>'

def test_index(client):
    response = client.get('/cloans/')
    assert response.status_code == 200
    assert "Lista de Préstamos".encode('utf-8') in response.data

def test_add_cloan(client, computer, user):
    response = client.post('/cloans/add', data={
        'computerId': computer.idComputer,
        'userId': user.idUser,
        'status': 'Active'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert "Lista de Préstamos".encode('utf-8') in response.data

def test_edit_cloan(client, cloan, computer, user):
    response = client.post(f'/cloans/update/{cloan.idLoan}', data={
        'computerId': computer.idComputer,
        'userId': user.idUser,
        'loanDate': '2026-01-01 10:00:00',
        'returnDate': '2026-01-02 10:00:00',
        'status': 'Active'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert "Lista de Préstamos".encode('utf-8') in response.data

def test_delete_cloan(client, cloan):
    response = client.post(f'/cloans/delete/{cloan.idLoan}', follow_redirects=True)
    assert response.status_code == 200
    assert "Lista de Préstamos".encode('utf-8') in response.data

def test_return_cloan(client, cloan):
    response = client.post(f'/cloans/return/{cloan.idLoan}', follow_redirects=True)
    assert response.status_code == 200
    assert "Returned".encode('utf-8') in response.data
