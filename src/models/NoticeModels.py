from database.db import get_connection
from .entities.Notice import Notice


class NoticeModel():

    @classmethod
    def add_notice(self, notice):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO noticias ("ID", "Título", "Descripción")
                VALUES (%s, %s, %s)""", (notice.id, notice.title, notice.description))

                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as e:
            raise Exception(e)

    @classmethod
    def get_notices(self):
        try:
            connection = get_connection()
            notices = []

            with connection.cursor() as cursor:
                cursor.execute(
                    """SELECT * FROM noticias ORDER BY "Título" ASC""")
                resultset = cursor.fetchall()

                for row in resultset:
                    notice = Notice(row[0], row[1], row[2])
                    notices.append(notice.To_Json())

            connection.close()
            return notices
        except Exception as e:
            raise Exception(e)

    @classmethod
    def get_notice(self, id):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(
                    """SELECT * FROM noticias WHERE "ID" =%s """, (id,))

                row = cursor.fetchone()

                notice = None
                if row != None:
                    notice = Notice(row[0], row[1], row[2])
                    notice = notice.To_Json()

            connection.close()
            return notice

        except Exception as e:
            raise Exception(e)

    @classmethod
    def update_notice(self, notice):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""UPDATE noticias SET "Título" = %s, "Descripción" = %s
                WHERE "ID" = %s""", (notice.title, notice.description, notice.id))

                affected_rows = cursor.rowcount
                connection.commit()

            connection.close
            return affected_rows

        except Exception as e:
            raise Exception(e)

    @classmethod
    def delete_notice(self, notice):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(
                    """DELETE FROM noticias WHERE "ID" = %s""", (notice.id,))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as e:
            raise Exception(e)
