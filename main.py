from config.connection import Connection


class Curso:
    def __init__(self, nombre):
        self.nombre = nombre
        # self.insert_curso()
        # self.create_table()

    def create_table(self):
        try:
            conn = Connection("curso")
            query = '''
                CREATE TABLE IF NOT EXISTS mobile(
                    id SERIAL PRIMARY KEY NOT NULL,
                    nombre VARCHAR(50) NOT NULL
                );
            '''
            conn.execute_query(query)
            conn.commit()
        except Exception as e:
            conn.rollback()
            print(e)

    @classmethod
    def all_cursos(cls):
        try:
            conn = Connection('curso')
            records = conn.select([])

            for record in records:
                print(f'ID: {record[0]}')
                print(f'Curso: {record[1]}')
                # print(f'Precio: {record[2]}')
                print('=====================')
            return records
        except Exception as e:
            print(e)

    def insert_curso(self):
        try:
            conn = Connection('curso')
            conn.insert({
                'nombre': self.nombre,
                # 'precio': self.precio
            })
            print(
                f'Se registro el curso: {self.nombre}')
            # print(
            #     f'Se registro el modelo: {self.modelo} con el precio {self.precio}')
        except Exception as e:
            print(e)

    def update_curso(self):
        try:
            conn = Connection('curso')
            conn.update({
                'id': 8,
                'modelo': 'Motorola'
            }, {
                'precio': self.precio,
                'modelo': 'Motorola 2021'
            })
            #print(f'Se registro el modelo: {self.modelo} con el precio {self.precio}')
        except Exception as e:
            print(e)


# curso = Curso('Matemática')
# celular.all_mobiles()
print(Curso.all_cursos())
