class Notice():

    def __init__(self, id, title=None, description=None):
        self.id = id
        self.title = title
        self.description = description

    def To_Json(self):
        return {
            'ID':self.id,
            'Título': self.title,
            'Descripción': self.description
        }
