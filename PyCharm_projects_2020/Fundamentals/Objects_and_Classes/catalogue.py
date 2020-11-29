class Catalogue:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def get_by_letter(self, first_letter):
        _new_list = [p for p in self.products if ord(p[0]) == ord(first_letter)]
        return _new_list

    def __repr__(self):
        text = f'Items in the {self.name} catalogue:\n'
        text += '\n'.join(sorted(self.products))
        return text


catalogue = Catalogue('Furniture')
catalogue.add_product('Sofa')
catalogue.add_product('Mirror')
catalogue.add_product('Desk')
catalogue.add_product('Chair')
catalogue.add_product('Carpet')
print(catalogue.get_by_letter('C'))
print(catalogue)
