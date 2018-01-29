import time
import random
# import smtplib
from email.message import EmailMessage
from email.utils import formatdate, make_msgid

from flask import (Flask, redirect, url_for, render_template, request, session,
                   flash, jsonify)
from celery import Celery
from loggers import log_to_file


app = Flask(__name__)

app.config['SECRET_KEY'] = 'Some secret key'
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'
# app.config['SMTP_SERVER'] = 'localhost'
# app.config['SMTP_PORT'] = '1025'
app.config['MAIL_SENDER'] = 'sender@example.org'

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)


@celery.task
def fake_send_mail(recepient, msg):
    # s = smtplib.SMTP(host=app.config['SMTP_SERVER'],
    #                  port=app.config['SMTP_PORT'])
    # s.sendmail(from_addr=app.config.get('MAIL_SENDER'),
    #            to_addrs=recepient,
    #            msg=msg)
    # s.quit()
    log_to_file.info(f'Email was sent to "{recepient}": \n{msg}')


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html', email=session.get('email', ''))

    email = request.form['email']
    session['email'] = email

    msg = EmailMessage()
    msg['From'] = app.config.get('MAIL_SENDER')
    msg['To'] = email
    msg['Subject'] = 'Test mail'
    msg['Date'] = formatdate()
    msg['Message-ID'] = make_msgid()
    msg.set_content('Hello, this is a test mail.')
    msg = msg.as_string()

    if request.form['submit'] == 'Send now':
        fake_send_mail.delay(email, msg)
        flash('Sending email right now.')
    elif request.form['submit'] == 'Send 10s later':
        fake_send_mail.apply_async(args=[email, msg], countdown=10)
        flash('An email will be sent later...')

    return redirect(url_for('index'))


@celery.task(bind=True)
def fake_task(self):
    total = random.randint(5, 20)
    step = 100 // total
    for i in range(1, 100, step):
        self.update_state(state='PROGRESS',
                          meta={'current': i, 'status': 'Processing...'})
        time.sleep(2)
    return {
        'current': 100,
        'status': 'Task completed.',
        'result': 42,
    }


@app.route('/add_task', methods=['POST'])
def add_task():
    task = fake_task.apply_async()
    return jsonify({}), 202, {'Location': url_for('task_status',
                                                  task_id=task.id)}


@app.route('/task_status/<task_id>')
def task_status(task_id):
    task = fake_task.AsyncResult(task_id)
    if task.state == 'PENDING':
        # Task is waiting for execution or unknown
        response = {
            'state': task.state,
            'status': 'Pending...',
            'current': 0,
        }
    elif task.state == 'FAILURE':
        # Task execution resulted in failure.
        response = {
            'state': task.state,
            'status': str(task.info),  # exception raised
            'current': 1,
        }
    else:
        response = {
            'state': task.state,
            'status': task.info.get('status', ''),
            'current': task.info.get('current', 0),
        }
        if 'result' in task.info:
            response['result'] = task.info['result']
    return jsonify(response)
