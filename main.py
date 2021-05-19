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


class Nota:
    def __init__(self, nota, alumno_id, curso_id, aescolar_id):
        self.nota = nota
        self.alumno_id = alumno_id
        self.curso_id = curso_id
        self.aescolar_id = aescolar_id

        # self.insert_curso()
        # self.create_table()

    def create_table(self):
        try:
            conn = Connection("nota")
            query = '''
                CREATE TABLE IF NOT EXISTS nota(
                    id SERIAL PRIMARY KEY NOT NULL,
                    nota DOUBLE NOT NULL
                    alumno_id INTEGER FOREIGN KEY
                    curso_id INTEGER FOREIGN KEY
                    aescolar_id INTEGER FOREIGN KEY
                );
            '''
            conn.execute_query(query)
            conn.commit()
        except Exception as e:
            conn.rollback()
            print(e)

    @classmethod
    def all_notas(cls):
        try:
            conn = Connection('bimestre')
            records = conn.select([])

            for record in records:
                print(f'ID: {record[0]}')
                print(f'BIMESTRE: {record[1]}')
                # print(f'Precio: {record[2]}')
                print('=====================')
            return records
        except Exception as e:
            print(e)

    def insert_nota(self):
        try:
            conn = Connection('nota')
            conn.insert({
                'nombre': self.nota,
                'nombre': self.alumno_id,
                'nombre': self.curso_id,
                'nombre': self.aescolar_id,
                # 'precio': self.precio
            })
            print(
                f'Se registro la nota: {self.nota}')
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
            query = '''
                SELECT p.id, p.nombre, p.dni, p.edad, p.correo, c.nombre FROM profesor p
                JOIN curso c ON p.curso_id = c.id
            '''
            records = conn.execute_my_query(query)

            for record in records:
                print(f'ID: {record[0]}')
                print(f'Nombre: {record[1]}')
                print(f'DNI: {record[2]}')
                print(f'Edad: {record[3]}')
                print(f'Correo: {record[4]}')
                print(f'Curso: {record[5]}')
                # print(f'Precio: {record[2]}')
                print('=====================')
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
            query = '''
                SELECT s.id, s.nombre, ae.nombre FROM salon s
                JOIN aescolar ae ON s.aescolar_id = ae.id
            '''
            records = conn.execute_my_query(query)

            for record in records:
                print(f'ID: {record[0]}')
                print(f'Nombre: {record[1]}')
                print(f'Año Escolar: {record[2]}')
                print('=====================')
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
            query = '''
                SELECT a.id, a.nombre, a.edad, a.correo, s.nombre FROM alumno a
                JOIN salon s ON a.salon_id = s.id
            '''
            records = conn.execute_my_query(query)

            for record in records:
                print(f'ID: {record[0]}')
                print(f'Nombre: {record[1]}')
                print(f'Edad: {record[2]}')
                print(f'Correo: {record[3]}')
                print(f'Salon: {record[4]}')
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
                SELECT s.nombre, c.nombre FROM curso_salon cs
                JOIN curso c ON cs.curso_id = c.id
                JOIN salon s ON cs.salon_id = s.id
                WHERE s.nombre = '1A'
            '''
            # query = 'SELECT * FROM curso_salon'
            records = conn.execute_my_query(query)
            print(records)
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

    def interfaz_inicial(self):
        while True:
            print('''
                BIENVENIDO AL SISTEMA DE GESTION ESCOLAR
                Seleccione el número de su opción:
                1) Gestionar Alumnos
                2) Gestionar Profesores
                3) Gestionar Salones
                4) Gestionar Cursos
                5) Gestionar Notas
                6) Salir del Progama
            ''')
            opcion = input('>')
            if (opcion == '1'):
                self.interfaz_alumno()
            if (opcion == '2'):
                self.interfaz_profesor()
            if (opcion == '3'):
                pass
            if (opcion == '4'):
                pass
            if (opcion == '5'):
                pass
            if (opcion == '6'):
                exit()
            else:
                print('Ingrese una opción válida')

    def interfaz_profesor(self):
        while True:
            print('''
                PROFESORES
                1) Mostrar Profesores
                2) Crear Profesor
                3) Regresar
            ''')
            opcion = input('>')
            if (opcion == '1'):
                Profesor.all_profesor()
            if (opcion == '2'):
                self.ingresar_profesor()
            if (opcion == '3'):
                return
            else:
                print('Ingrese una opción válida')

    def interfaz_alumno(self):
        while True:
            print('''
                ALUMNOS
                1) Mostrar Alumnos
                2) Crear Alumno
                3) Regresar
            ''')
            opcion = input('>')
            if (opcion == '1'):
                Alumno.all_alumno()
            if (opcion == '2'):
                self.ingresar_alumno()
            if (opcion == '3'):
                return
            else:
                print('Ingrese una opción válida')

    def ingresar_profesor(self):
        pass

    def ingresar_alumno(self):
        nombre = input('Nombre del alumno > ')
        edad = input('Edad del alumno > ')
        correo = input('Correo del alumno > ')
        Salon.all_salon()
        print('Seleccione el salón: > ')
        salon_id = input('>')
        Alumno(nombre, edad, correo, salon_id).insert_alumno()


# print(Curso_Salon.all_curso_salon())
Cole().interfaz_inicial()
