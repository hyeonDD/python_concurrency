from odmantic import  Model


class BookModel(Model):
    keyword: str
    publisher: str
    price: int
    image: str

    class Config:
        collection = "books"

# db(practice) -> collection(books) -> document {
# keyword: 파이썬
# publisher ... 
# }