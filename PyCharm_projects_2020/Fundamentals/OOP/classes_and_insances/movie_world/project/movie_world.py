# from class_and_instance.movie_world.project.dvd import DVD
# from class_and_instance.movie_world.project.customer import Customer

class MovieWorld:
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer):
        if len(self.customers) < MovieWorld.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd):
        if len(self.dvds) < MovieWorld.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id, dvd_id):
        dvd = [d for d in self.dvds if d.id == dvd_id][0]
        customer = [c for c in self.customers if c.id == customer_id][0]
        if dvd.is_rented:
            return "DVD is already rented"
        if dvd.name in customer.rented_dvds:
            return f"{customer.name} has already rented {dvd.name}"
        elif customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"
        else:
            dvd.is_rented = True
            customer.rented_dvds.append(dvd.name)
            return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        dvd = [d for d in self.dvds if d.id == dvd_id][0]
        customer = [c for c in self.customers if c.id == customer_id][0]
        if dvd.name in customer.rented_dvds:
            dvd.is_rented = False
            customer.rented_dvds.remove(dvd.name)
            return f"{customer.name} has successfully returned {dvd.name}"
        else:
            return f"{customer.name} does not have that DVD"

    def __repr__(self):
        customers_list = []
        dvd_list = []
        for c in self.customers:
            customers_list.append(f"{c}")
        for d in self.dvds:
            dvd_list.append(f"{d}")
        return '\n'.join(customers_list) + '\n' + '\n'.join(dvd_list)