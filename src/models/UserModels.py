from database.db import get_connection
from .entities.User import User


class UserModel():

    @classmethod
    def add_user(self, user):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO usuario ("ID", "Nombre Completo", "Correo", "Contraseña", "Dirección", "Teléfono", "Fecha de Nacimiento") 
                VALUES (%s, %s, %s, %s, %s, %s, %s)""", (user.id, user.full_name, user.email, user.password, user.address, user.phone, user.birthdate))

                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as e:
            raise Exception(e)

    @classmethod
    def get_user(self, email, password):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(
                    """SELECT * FROM usuario WHERE "Correo" =%s AND "Contraseña" = %s """, (email,password))
                row = cursor.fetchone()

                user = None
                if row != None:
                    user = User(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                    user = user.to_JSON()

            connection.close()
            return user

        except Exception as e:
            raise Exception(e)
        


    @classmethod
    def get_users(self):
        try:
            connection = get_connection()
            users = []

            with connection.cursor() as cursor:
                cursor.execute("""SELECT * FROM usuario ORDER BY "ID" ASC""")
                resultset = cursor.fetchall()

                for row in resultset:
                    user = User(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                    users.append(user.to_JSON())

            connection.close()
            return users
        except Exception as ex:
            raise Exception(ex)