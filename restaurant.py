class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print('Name of restaurant: ' + self.name + ' ' + 'Type of restaurant: ' + self.type)

    def open_restaurant(self):
        print(self.name + ' ' + 'is open now!')

    def update_restaurant(self):
        if self.number_served > 55:
            print('We are full now!')
        else:
            print('We have ' + str(self.number_served) + ' hosts right now.')

    def increment_hosts(self, hosts):
        self.number_served += hosts


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)

    def describe_flavors(self):
        flavors = ['Chocolate', 'Strawberry', 'Vannila', 'Russian\n']
        print('Today we have this flavors: ')
        for i in flavors:
            print(i)


icecream_stand = IceCreamStand('Billy ice,', 'Ice cream stand')
icecream_stand.describe_restaurant()
icecream_stand.describe_flavors()

restaurant = Restaurant('China Petrohrad,', 'China')


restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant.number_served = 10
restaurant.update_restaurant()

restaurant.number_served = 56
restaurant.update_restaurant()

