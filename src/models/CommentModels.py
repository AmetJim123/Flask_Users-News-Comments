from database.db import get_connection
from .entities.Comment import FullNotice


class CommentModels():

    @classmethod
    def add_comment(self, commentary):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO comentarios ("ID", "Comentario")
                VALUES (%s, %s) """, (commentary.id, commentary.comment))

                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as e:
            return Exception(e)

    @classmethod
    def get_comments(self):
        try:
            connection = get_connection()
            full_notices = []
            with connection.cursor() as cursor:
                cursor.execute(
                    """SELECT "noticias"."ID", "Título", "Descripción", "Comentario" 
                    FROM noticias LEFT JOIN comentarios
                    ON "comentarios"."ID" = "noticias"."ID" """
                )
                resultset = cursor.fetchall()

                for row in resultset:
                    Notice_comment = FullNotice(row[0], row[1], row[2], row[3])
                    full_notices.append(Notice_comment.to_json())

            connection.close()
            return full_notices
        except Exception as e:
            raise Exception(e)
