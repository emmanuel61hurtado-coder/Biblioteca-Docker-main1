def test_book_model(book, author):
    assert book.idBook is not None
    assert book.titleBook == "Cien Anos de Soledad"
    assert book.authorId == author.idAuthor
    assert book.author.nameAuthor == "Gabriel Garcia Marquez"
    assert repr(book) == "<Book Cien Anos de Soledad>"

def test_index(client):
    response = client.get('/Book/')
    assert response.status_code == 200
    assert "Lista de Libros".encode('utf-8') in response.data

def test_add_book(client, author):
    response = client.post('/Book/add', data={
        'titleBook': 'Don Quijote de la Mancha',
        'authorId': author.idAuthor
    }, follow_redirects=True)
    assert response.status_code == 200
    assert "Don Quijote de la Mancha".encode('utf-8') in response.data

def test_edit_book(client, book, author):
    response = client.post(f'/Book/edit/{book.idBook}', data={
        'titleBook': 'Updated Book Title',
        'authorId': author.idAuthor
    }, follow_redirects=True)
    assert response.status_code == 200
    assert "Updated Book Title".encode('utf-8') in response.data

def test_delete_book(client, book):
    response = client.get(f'/Book/delete/{book.idBook}', follow_redirects=True)
    assert response.status_code == 200
    assert "Lista de Libros".encode('utf-8') in response.data
