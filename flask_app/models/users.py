from flask_app.config.mysqlconnection import connectToMySQL
import re #Importamos expresiones regulares

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+[a-zA-Z]+$')

from flask import flash

class User:

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.classroom_id = data['classroom_id']
        self.password = data['password']

    @classmethod
    def read(cls):
        query = 'SELECT * FROM users'
        results = connectToMySQL('esquema_de_usuarios').query_db(query)
        # [
        #	{'id': '1','first_name': 'Cynthia','last_name': 'Apellido','email': 'c@cd.com','created_at': '2002-02'}
        # ] 
        users = []
        for u in results:
            users.append(cls(u))
        return users
    
    @classmethod
    def create(cls, formulario):
        #data = {'first_name': 'C','last_name': 'X','email': 'c@cd.com'}
        query = 'INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s)'
        result = connectToMySQL('esquema_usuarios').query_db(query, formulario)
        return result
    
    @classmethod
    def delete(cls, formulario):
        query = 'DELETE FROM users WHERE id = %(id)s'
        result = connectToMySQL('esquema_de_usuarios').query_db(query, formulario)
        return result
