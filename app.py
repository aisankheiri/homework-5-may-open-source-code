from flask import Flask, jsonify, request

app = Flask(__name__)

# Kitap verilerini depolamak için geçici bir liste kullanıyoruz
books = []

@app.route('/')
def home():
    return 'Merhaba benim adım Aisan Kheiri (170420995) ve bu açık kaynak ödevidir! Kitaplara erişim için ./book kullanarak erişim sağlayabilirsin.'

# Tüm kitapları listele
@app.route('/books', methods=['GET'])
def list_books():
    return jsonify(books)

# Yeni bir kitap oluştur
@app.route('/books', methods=['POST'])
def create_book():
    new_book = request.json
    books.append(new_book)
    return jsonify(new_book), 201

# Belirli bir kitabı getir
@app.route('/books/<string:id>', methods=['GET'])
def get_book_by_id(id):
    for book in books:
        if book['id'] == id:
            return jsonify(book)
    return jsonify({'message': 'Kitap bulunamadı'}), 404

# Belirli bir kitabı güncelle
@app.route('/books/<string:id>', methods=['PUT'])
def update_book(id):
    for book in books:
        if book['id'] == id:
            book.update(request.json)
            return jsonify(book)
    return jsonify({'message': 'Kitap bulunamadı'}), 404

# Belirli bir kitabı sil
@app.route('/books/<string:id>', methods=['DELETE'])
def delete_book(id):
    for book in books:
        if book['id'] == id:
            books.remove(book)
            return '', 204
    return jsonify({'message': 'Kitap bulunamadı'}), 404

if __name__ == '__main__':
    app.run()
