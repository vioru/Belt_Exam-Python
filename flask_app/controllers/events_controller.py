from flask import render_template, redirect, session, request, flash 
from flask_app import app
from flask_app.models.users import User
from flask_app.models.events import Event

@app.route('/new/task')
def new_task():

    if 'usuario_id' not in session: 
        return redirect('/')

    formulario = {
        "id": session['usuario_id']
    }

    user = User.get_by_id(formulario)
    
    return render_template('new_task.html', user=user)



@app.route ('/create/task', methods=['POST'])
def create_task():
    if 'usuario_id' not in session: 
        return redirect('/')

    if not Event.valid_event(request.form):
        return redirect('/new/task')

    Event.save(request.form)
    return redirect('/agenda')

@app.route('/edit/task/<int:id>') 
def edit_task(id):
    if 'usuario_id' not in session: #Solo puede ver la página si ya inició sesión 
        return redirect('/')
    
    formulario = {
        "id": session['usuario_id']
    }

    user = User.get_by_id(formulario) 

    formulario_task = { "id": id }
    
    event = Event.get_by_id(formulario_task)

    return render_template('edit_task.html', user=user, event = event)


@app.route('/edit/task', methods=['POST'])
def update_task():
    if 'usuario_id' not in session: 
        return redirect('/')
    
    if not Event.valid_event(request.form):
        return redirect('/edit/task/'+request.form['id'])

    Event.update(request.form)

    return redirect('/agenda')

@app.route('/delete/task/<int:id>')
def delete_task(id):
    if 'usuario_id' not in session: 
        return redirect('/')
    
    formulario = {"id": id}
    Event.delete(formulario)

    return redirect('/agenda')






