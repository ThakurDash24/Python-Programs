class Product:
    def __init__(self, product_id, name, price, discount_percentage):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__discount_percentage = discount_percentage

    def get_product_id(self):
        return self.__product_id

    def set_product_id(self, product_id):
        self.__product_id = product_id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def get_discount_percentage(self):
        return self.__discount_percentage

    def set_discount_percentage(self, discount_percentage):
        self.__discount_percentage = discount_percentage

    def _calculate_final_price(self):
        return self.__price * (1 - self.__discount_percentage / 100)


class Electronics(Product):
    def __init__(self, product_id, name, price, discount_percentage, warranty_period):
        super().__init__(product_id, name, price, discount_percentage)
        self.__warranty_period = warranty_period

    def get_warranty_period(self):
        return self.__warranty_period

    def set_warranty_period(self, warranty_period):
        self.__warranty_period = warranty_period


class Clothing(Product):
    def __init__(self, product_id, name, price, discount_percentage, size, material):
        super().__init__(product_id, name, price, discount_percentage)
        self.__size = size
        self.__material = material

    def get_size(self):
        return self.__size

    def set_size(self, size):
        self.__size = size

    def get_material(self):
        return self.__material

    def set_material(self, material):
        self.__material = material


products = []

def add_electronic_item(product_id, name, price, discount_percentage, warranty_period):
    electronic = Electronics(product_id, name, price, discount_percentage, warranty_period)
    products.append(electronic)

def add_clothing_item(product_id, name, price, discount_percentage, size, material):
    clothing = Clothing(product_id, name, price, discount_percentage, size, material)
    products.append(clothing)

def display_all_products():
    for product in products:
        if isinstance(product, Electronics):
            print(f"Electronic - ID: {product.get_product_id()}, Name: {product.get_name()}, Price: {product.get_price()}, Discount: {product.get_discount_percentage()}%, Warranty: {product.get_warranty_period()}")
        elif isinstance(product, Clothing):
            print(f"Clothing - ID: {product.get_product_id()}, Name: {product.get_name()}, Price: {product.get_price()}, Discount: {product.get_discount_percentage()}%, Size: {product.get_size()}, Material: {product.get_material()}")

def calculate_total_price_with_tax():
    total = sum(product._calculate_final_price() for product in products)
    total_with_tax = total * 1.1
    print(f"Total price with tax: {total_with_tax}")

# Example usage
add_electronic_item("E001", "Smartphone", 699.99, 10, "2 years")
add_clothing_item("C001", "T-Shirt", 19.99, 5, "L", "Cotton")

display_all_products()
calculate_total_price_with_tax()
