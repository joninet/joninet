from fastapi import APIRouter, Query, Path
from models.product import Product

router = APIRouter()

products = [
    {
        "id": 1,
        "name": "producto 1",
        "price": 20,
        "stock": 10
    },
    {
        "id": 2,
        "name": "producto 2",
        "price": 30,
        "stock": 20
    }
]

@router.get('/products')
def getProducts():
    return products

@router.get('/products/{id}')
def getProduct(id: int = Path(gt=0)):
    return list(filter(lambda item: item['id'] == id, products))

#products/?stock=10&price=20
@router.get('/products/')
def getProductsByStock(stock: int, price: float = Query(gt=0)):
    return list(filter(lambda item: item['stock'] == stock and item['price'] == price, products))

@router.post('/products')
def createProduct(product: Product):
    products.append(product)
    return products

@router.put('/products/{id}')
def updateProduct(id: int, product: Product):
    for index, item in enumerate(products):
        if item['id'] == id:
            products[index]['name'] = product.name
            products[index]['stock'] = product.stock
            products[index]['price'] = product.price
    return products

@router.delete('/products/{id}')
def deleteProduct(id: int):
    for item in products:
        if item['id'] == id:
            products.remove(item)
    return products
