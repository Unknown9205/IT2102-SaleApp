def load_categories():
    return [{
        'id': 1,
        'name': 'Mobile'
    }, {
        'id': 2,
        'name': 'Tablet'
    }]


def load_products(kw):
    products = [{
        "id": 1,
        "name": "iPad Pro 2022",
        "price": 24000000,
        "image": "https://www.popsci.com/uploads/2022/10/25/377A4830.jpg?auto=webp&width=1440&height=960.48"
    }, {
        "id": 2,
        "name": "iPhone 15",
        "price": 24000000,
        "image": "https://www.popsci.com/uploads/2022/10/25/377A4830.jpg?auto=webp&width=1440&height=960.48"
    }, {
        "id": 3,
        "name": "iPad Pro 2022",
        "price": 24000000,
        "image": "https://www.popsci.com/uploads/2022/10/25/377A4830.jpg?auto=webp&width=1440&height=960.48"
    }, {
        "id": 4,
        "name": "iPad Pro 2022",
        "price": 24000000,
        "image": "https://www.popsci.com/uploads/2022/10/25/377A4830.jpg?auto=webp&width=1440&height=960.48"
    }, {
        "id": 5,
        "name": "iPad Pro 2022",
        "price": 24000000,
        "image": "https://www.popsci.com/uploads/2022/10/25/377A4830.jpg?auto=webp&width=1440&height=960.48"
    }, {
        "id": 6,
        "name": "iPad Pro 2022",
        "price": 24000000,
        "image": "https://www.popsci.com/uploads/2022/10/25/377A4830.jpg?auto=webp&width=1440&height=960.48"
    }, {
        "id": 7,
        "name": "iPhone 15 Pro Max",
        "price": 24000000,
        "image": "https://www.popsci.com/uploads/2022/10/25/377A4830.jpg?auto=webp&width=1440&height=960.48"
    }, {
        "id": 8,
        "name": "iPad Pro 2022",
        "price": 24000000,
        "image": "https://www.popsci.com/uploads/2022/10/25/377A4830.jpg?auto=webp&width=1440&height=960.48"
    }]

    if kw:
        products = [p for p in products if p['name'].find(kw) >= 0]

    return products
