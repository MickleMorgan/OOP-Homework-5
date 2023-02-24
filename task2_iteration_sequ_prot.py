class Negative_price(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return f'Price can\'t be negative or zero'


class Products:
    def __init__(self, name, price):
        if price <= 0:
            raise Negative_price
        self.price = price
        self.name = name

    def __str__(self):
        return f'{self.name}, cost {self.price} $'


class Customer:
    def __init__(self, name, surname, phone):
        self.name = name
        self.surname = surname
        self.phone = phone

    def __str__(self):
        return f'{self.name}, {self.surname}, Phone: {self.phone}'


class Order:
    def __init__(self, customer):
        self.customer = customer
        self.cart = {}

    def __len__(self):
        return len(self.cart)

    def __getitem__(self, index):
        products = list(self.cart.keys())
        return products[index]

    def __iter__(self):
        self.products = list(self.cart.keys())
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.products):
            product = self.products[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration

    def add_product(self, product, quantities):
        self.cart.update({product: quantities})

    def summa_of_order(self):
        summa = 0
        for item in self.cart:
            summa += item.price * self.cart[item]
        return summa

    def __str__(self):
        result = f'{self.customer.name}, {self.customer.surname}\nPhone: {self.customer.phone}\n'
        for item in self.cart:
            result += f'Product - {item}, quantities {self.cart[item]}\n'
        result += f'Total price {str(self.summa_of_order())} $\n'
        return result



headphones = Products('Headphones', 10)
phone = Products('Phone', 100)
laptop = Products('Laptop', 300)
cable = Products('Cable', 5)
connector = Products('Connector', 1)

customer_1 = Customer('Andrew', 'Garfield', '380962431562')
customer_2 = Customer('Steve', 'Jonson', '38096345454')
customer_3 = Customer('Karol', 'Gerbel', '38096341254')

order_1 = Order(customer_1)
order_1.add_product(headphones, 1)
order_1.add_product(cable, 2)
order_1.add_product(connector, 2)

order_2 = Order(customer_2)
order_2.add_product(laptop, 1)

order_3 = Order(customer_3)
order_3.add_product(phone, 1)

# for product in order_1:
#     print(product)

print(len(order_1))  # Output: 2
print(order_1[1])