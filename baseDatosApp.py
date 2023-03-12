import mysql.connector



'''conexion= mysql.connector.connect(host= "localhost", user= "root", passwd= "", database= "Seleccion")
cursor= conexion.cursor()
cursor.execute("""CREATE TABLE JUGADORES(
                    CODIGO INT,
                    DNI INT(8),
                    NOMBRE VARCHAR (50),
                    APELLIDO VARCHAR (50),
                    N_CAMISETA INT(2));""")'''

class Selecc:
    def abrir(self):
        conexion= mysql.connector.connect(host= "localhost", user= "root", passwd= "", database= "Seleccion")

        return conexion

    def agregar(self, datos):
        conexion= self.abrir()
        cursor= conexion.cursor()
        instruction= "INSERT INTO jugadores VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(instruction, datos)
        conexion.commit()
        conexion.close()

    def borrar(self, datos):
        conexion= self.abrir()
        cursor= conexion.cursor()
        instrction= "DELETE FROM jugadores WHERE CODIGO= %s"
        cursor.execute(instrction, datos)
        conexion.commit()
        conexion.close()

    def listar(self):
        conexion= self.abrir()
        cursor= conexion.cursor()
        instrction= "SELECT * FROM jugadores ORDER BY CODIGO"
        cursor.execute(instrction)
        conexion.close()
        return cursor.fetchall()

    def consultar(self, datos):
        conexion= self.abrir()
        cursor= conexion.cursor()
        instruction= "SELECT CODIGO, DNI, NOMBRE, APELLIDO, N_CAMISETA FROM JUGADORES WHERE CODIGO= %s ORDER BY CODIGO ASC"
        cursor.execute(instruction, datos)
        conexion.close()
        return cursor.fetchall()

    def actualizar(self, datos):
        conexion= self.abrir()
        cursor= conexion.cursor()
        instruccion= "UPDATE jugadores SET DNI= %s, NOMBRE= %s, APELLIDO= %s, N_CAMISETA= %s WHERE CODIGO= %s"
        cursor.execute(instruccion, datos)
        conexion.commit()
        conexion.close()

    def imprimir(self):
        conexion=self.abrir()
        cursor=conexion.cursor()
        instruction= "SELECT * FROM JUGADORES ORDER BY CODIGO ASC"
        cursor.execute(instruction)
        conexion.close
        return cursor.fetchall()