from config.connection import Connection


class Aescolar:
    def __init__(self, nombre):
        self.nombre = nombre
        # self.insert_curso()
        # self.create_table()

    def create_table(self):
        try:
            conn = Connection("aescolar")
            query = '''
                CREATE TABLE IF NOT EXISTS aescolar(
                    id SERIAL PRIMARY KEY NOT NULL,
                    nombre integer NOT NULL
                );
            '''
            conn.execute_query(query)
            conn.commit()
        except Exception as e:
            conn.rollback()
            print(e)

    @classmethod
    def all_aescolar(cls):
        try:
            conn = Connection('aescolar')
            records = conn.select([])

            for record in records:
                print(f'ID: {record[0]}')
                print(f'Año: {record[1]}')
                # print(f'Precio: {record[2]}')
                print('=====================')
            return records
        except Exception as e:
            print(e)

    def insert_aescolar(self):
        try:
            conn = Connection('aescolar')
            conn.insert({
                'nombre': self.nombre
                # 'precio': self.precio
            })
            print(
                f'Se registro el aescolar: {self.nombre}')
            # print(
            #     f'Se registro el modelo: {self.modelo} con el precio {self.precio}')
        except Exception as e:
            print(e)

    def update_aescolar(self):
        try:
            conn = Connection('aescolar')
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
    def all_curso(cls):
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


class Profesor:
    def __init__(self, nombre, dni, edad, correo, curso_id):
        self.nombre = nombre
        self.dni = dni
        self.edad = edad
        self.correo = correo
        self.curso_id = curso_id
        # self.insert_curso()
        # self.create_table()

    def create_table(self):
        try:
            conn = Connection("profesor")
            query = '''
                CREATE TABLE IF NOT EXISTS profesor(
                    id SERIAL PRIMARY KEY NOT NULL,
                    nombre VARCHAR(50) NOT NULL,
                    edad INTEGER NOT NULL,
                    correo VARCHAR(50) NOT NULL,
                    curso_id INTEGER FOREIGN KEY NOT NULL
                );
            '''
            conn.execute_query(query)
            conn.commit()
        except Exception as e:
            conn.rollback()
            print(e)

    @classmethod
    def all_profesor(cls, data=[]):
        try:
            conn = Connection('profesor')
            records = conn.select(data)

            # for record in records:
            #     print(f'ID: {record[0]}')
            #     print(f'Nombre: {record[1]}')
            #     print(f'DNI: {record[2]}')
            #     print(f'Edad: {record[3]}')
            #     print(f'Correo: {record[4]}')
            #     print(f'CursoID: {record[5]}')
            #     # print(f'Precio: {record[2]}')
            #     print('=====================')
            return records
        except Exception as e:
            print(e)

    def insert_profesor(self):
        try:
            conn = Connection('profesor')
            conn.insert({
                'nombre': self.nombre,
                'dni': self.dni,
                'edad': self.edad,
                'correo': self.correo,
                'curso_id': self.curso_id,
                # 'precio': self.precio
            })
            print(
                f'Se registro el profesor: {self.nombre}')
            # print(
            #     f'Se registro el modelo: {self.modelo} con el precio {self.precio}')
        except Exception as e:
            print(e)

    def update_profesor(self):
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


class Salon:
    def __init__(self, nombre, aescolar_id):
        self.nombre = nombre
        self.aescolar_id = aescolar_id
        # self.insert_curso()
        # self.create_table()

    def create_table(self):
        try:
            conn = Connection("salon")
            query = '''
                CREATE TABLE IF NOT EXISTS salon(
                    id SERIAL PRIMARY KEY NOT NULL,
                    nombre VARCHAR(50) NOT NULL,
                    aescolar_id INTEGER FOREIGN KEY NOT NULL
                );
            '''
            conn.execute_query(query)
            conn.commit()
        except Exception as e:
            conn.rollback()
            print(e)

    @classmethod
    def all_salon(cls, data=[]):
        try:
            conn = Connection('salon')
            records = conn.select(data)

            for record in records:
                print(f'ID: {record[2]}')
                print(f'Nombre: {record[0]}')
            #     print(f'DNI: {record[2]}')
            #     print(f'Edad: {record[3]}')
            #     print(f'Correo: {record[4]}')
            #     print(f'CursoID: {record[5]}')
            #     # print(f'Precio: {record[2]}')
            #     print('=====================')
            return records
        except Exception as e:
            print(e)

    def insert_salon(self):
        try:
            conn = Connection('salon')
            conn.insert({
                'nombre': self.nombre,
                'aescolar_id': self.aescolar_id
                # 'precio': self.precio
            })
            print(
                f'Se registro el salon: {self.nombre}')
            # print(
            #     f'Se registro el modelo: {self.modelo} con el precio {self.precio}')
        except Exception as e:
            print(e)

    def update_salon(self):
        try:
            conn = Connection('salon')
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


class Alumno:
    def __init__(self, nombre, edad, correo, salon_id):
        self.nombre = nombre
        self.edad = edad
        self.correo = correo
        self.salon_id = salon_id
        # self.insert_curso()
        # self.create_table()

    def create_table(self):
        try:
            conn = Connection("alumno")
            query = '''
                CREATE TABLE IF NOT EXISTS alumno(
                    id SERIAL PRIMARY KEY NOT NULL,
                    nombre VARCHAR(50) NOT NULL,
                    edad INTEGER NOT NULL,
                    correo VARCHAR(50) NOT NULL,
                    salon_id INTEGER FOREIGN KEY NOT NULL
                );
            '''
            conn.execute_query(query)
            conn.commit()
        except Exception as e:
            conn.rollback()
            print(e)

    @classmethod
    def all_alumno(cls, data=[]):
        try:
            conn = Connection('alumno')
            records = conn.select(data)

            for record in records:
                print(f'ID: {record[0]}')
                print(f'Nombre: {record[1]}')
                print(f'Edad: {record[2]}')
                print(f'Correo: {record[3]}')
                print(f'SalonID: {record[4]}')
                # print(f'Precio: {record[2]}')
                print('=====================')
            return records
        except Exception as e:
            print(e)

    def insert_alumno(self):
        try:
            conn = Connection('alumno')
            conn.insert({
                'nombre': self.nombre,
                'edad': self.edad,
                'correo': self.correo,
                'salon_id': self.salon_id,
                # 'precio': self.precio
            })
            print(
                f'Se registro el alumno: {self.nombre}')
            # print(
            #     f'Se registro el modelo: {self.modelo} con el precio {self.precio}')
        except Exception as e:
            print(e)

    def update_alumno(self):
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


class Curso_Salon:
    def __init__(self, salon_id, curso_id):
        self.salon_id = salon_id
        self.curso_id = curso_id
        # self.insert_curso()
        # self.create_table()

    def create_table(self):
        try:
            conn = Connection("self")
            query = '''
                CREATE TABLE IF NOT EXISTS curso_salon(
                    id SERIAL PRIMARY KEY NOT NULL,
                    salon_id INTEGER FOREIGN KEY NOT NULL
                    curso_id INTEGER FOREIGN KEY NOT NULL
                );
            '''
            conn.execute_query(query)
            conn.commit()
        except Exception as e:
            conn.rollback()
            print(e)

    @classmethod
    def all_curso_salon(cls, data=[]):
        try:
            conn = Connection('curso_salon')
            # records = conn.select(data)

            # for record in records:
            #     print(f'ID: {record[0]}')
            #     print(f'Curso: {record[1]}')
            #     print(f'Salon: {record[2]}')
            #     ID, Salon, CursoNombre
            query = '''
                SELECT curso.id, curso.nombre
                FROM curso
                INNER JOIN curso_salon
                ON curso_salon.curso_id = salon.curso_id
            '''
            # query = 'SELECT * FROM curso_salon'
            records = conn.execute_my_query(query)

            return records
        except Exception as e:
            print(e)

    def insert_curso_salon(self):
        try:
            conn = Connection('curso_salon')
            conn.insert({
                'salon_id': self.salon_id,
                'curso_id': self.curso_id,
                # 'precio': self.precio
            })
            print(
                'Se registro el curso_salon')
            # print(
            #     f'Se registro el modelo: {self.modelo} con el precio {self.precio}')
        except Exception as e:
            print(e)

    def update_curso_salon(self):
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


class Cole:
    def __init__(self):
        pass


print(Curso_Salon.all_curso_salon())
