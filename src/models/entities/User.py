from utils.DateFormats import DateFormat

class User():

    def __init__(self, id, full_name=None, email=None, password=None, address=None, phone=None, birthdate=None):
        self.id = id
        self.full_name = full_name
        self.email = email
        self.password = password
        self.address = address
        self.phone = phone
        self.birthdate = birthdate

    def to_JSON(self):
        return {
            'ID': self.id,
            'Nombre Completo': self.full_name,
            'Email': self.email,
            'Contraseña': self.password,
            'Dirección': self.address,
            'Teléfono': self.phone,
            'Fecha de nacimiento': DateFormat.convert_date(self.birthdate)
        }
