class Repository:
    def __init__(self, connector_database):
        self.connector = connector_database

    def get_student_by_id(self, student_id):
        query = "SELECT * FROM Estudiantes WHERE ID = 2;"
        result = self.connector.execute_and_fetchone(query)
        return result


