from flask_app.config.mysqlconnection import  connectToMySQL
from flask import flash

from datetime import datetime, timedelta
today = datetime.now() 




class Event:
    def __init__(self,data):
        self.id = data['id']
        self.task = data['task']
        self.date = data['date']
        self.status = data['status']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']   

    @staticmethod
    def valid_event(formulario):
        es_valido = True

        if len(formulario['task']) < 3:
            flash("El nombre de la nueva tarea debe tener al menos 3 caracteres", "event")
            es_valido = False
        
        date = formulario['date']
        if formulario['date'] == "":
            flash("Ingrese una fecha", "event")
            es_valido = False
        elif  str(date) < str(today):
            flash("Debes ingresar una fecha mayor a la fecha actual", "event")
            es_valido = False


        
        
        
        if formulario['status'] == str(0):
            flash("debe asignarle un estado", "event")
            es_valido = False
        
        print(formulario['status'])
        
        
        return es_valido 


    @classmethod
    def save(cls, formulario):
        query = "INSERT INTO events (task, date, status, user_id) VALUES ( %(task)s, %(date)s, %(status)s, %(user_id)s)"
        newtask = connectToMySQL('diary').query_db(query, formulario)
        return newtask

    @classmethod
    def get_events_user(cls,formulario): 
        query = "SELECT events.* FROM events WHERE user_id = %(id)s"
        results = connectToMySQL('diary').query_db(query,formulario) 
        events = []
        
        for e in results:
            
            events.append(cls(e)) 
        return events


    @classmethod
    def get_by_id(cls, formulario): 
        query = "SELECT events.* FROM events WHERE id = %(id)s"
        result = connectToMySQL('diary').query_db(query, formulario) 
        event = cls(result[0])
        return event

    @classmethod
    def update(cls, formulario): 
        query = "UPDATE events SET task = %(task)s, date = %(date)s, status = %(status)s WHERE id = %(id)s"
        result = connectToMySQL('diary').query_db(query, formulario)
        return result
    

    @classmethod
    def delete(cls, formulario): 
        query = "DELETE FROM events WHERE id = %(id)s"
        result = connectToMySQL('diary').query_db(query, formulario)
        return result