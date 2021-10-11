class Person():
    def __init__(self, id, first_name, last_name, client_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.client_name = client_name

    def __repr__(self):
        rep = 'Person(' + self.first_name + ' ' + self.last_name + ')'
        return rep

    