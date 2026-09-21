def test_author_model(author):
    assert author.idAuthor is not None
    assert author.nameAuthor == "Gabriel Garcia Marquez"
    assert author.nationalityAuthor == "Colombian"
    assert repr(author) == "<Author Gabriel Garcia Marquez>"

def test_index(client):
    response = client.get('/Author/')
    assert response.status_code == 200
    assert "Lista de Autores".encode('utf-8') in response.data

def test_add_author(client):
    response = client.post('/Author/add', data={
        'nameAuthor': 'Mario Vargas Llosa',
        'nationalityAuthor': 'Peruvian'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert "Mario Vargas Llosa".encode('utf-8') in response.data

def test_edit_author(client, author):
    response = client.post(f'/Author/edit/{author.idAuthor}', data={
        'nameAuthor': 'Updated Author',
        'nationalityAuthor': 'Colombian'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert "Updated Author".encode('utf-8') in response.data

def test_delete_author(client, author):
    response = client.get(f'/Author/delete/{author.idAuthor}', follow_redirects=True)
    assert response.status_code == 200
    assert "Lista de Autores".encode('utf-8') in response.data
