def test_loan_model(loan, book, user):
    assert loan.idLoan is not None
    assert loan.bookId == book.idBook
    assert loan.userId == user.idUser
    assert loan.status == "Active"
    assert loan.fine == 0.0
    assert repr(loan) == f'<Loan {loan.idLoan} of Book {book.idBook} to User {user.idUser}>'

def test_index(client):
    response = client.get('/Loan/')
    assert response.status_code == 200
    assert "Lista de Préstamos".encode('utf-8') in response.data

def test_add_loan(client, book, user):
    response = client.post('/Loan/add', data={
        'bookId': book.idBook,
        'userId': user.idUser
    }, follow_redirects=True)
    assert response.status_code == 200
    assert "Lista de Préstamos".encode('utf-8') in response.data

def test_edit_loan(client, loan):
    response = client.post(f'/Loan/edit/{loan.idLoan}', data={
        'returnDate': '2026-12-31',
        'fine': '5.0',
        'status': 'Active'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert "Lista de Préstamos".encode('utf-8') in response.data

def test_delete_loan(client, loan):
    response = client.get(f'/Loan/delete/{loan.idLoan}', follow_redirects=True)
    assert response.status_code == 200
    assert "Lista de Préstamos".encode('utf-8') in response.data

def test_return_loan(client, loan):
    response = client.get(f'/Loan/return/{loan.idLoan}', follow_redirects=True)
    assert response.status_code == 200
    assert "Returned".encode('utf-8') in response.data
