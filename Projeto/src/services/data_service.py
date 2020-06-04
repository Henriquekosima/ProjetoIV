from src.models import db
from src.models.data import Data
from src.config.restplus import  json_abort
from sqlalchemy.exc import SQLAlchemyError 
import datetime

### AUTOR SERVICE
### gerenciar as regras de negocio e CRUD do author
###

def create(data):
    try:
        acc1 = data.get('acc1')
        acc2 = data.get('acc2')
        acc3 = data.get('acc3')
        gyro1 = data.get('gyro1')
        gyro2 = data.get('gyro2')
        gyro3 = data.get('gyro3')
        countSteps = data.get('countSteps')
        createdAt = datetime.datetime.now()

        #chama objeto para gravar no banco
        data = Data(acc1=acc1,acc2=acc2,acc3=acc3,gyro1=gyro1,gyro2=gyro2,gyro3=gyro3,countSteps=countSteps,createdAt=createdAt)
        db.session.add(data)
        db.session.commit()

        return data

    except SQLAlchemyError as err: 
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)


def get_all():
    try:
        
        data = Data.query.all()

        if not data:
            json_abort(400, "Data not found")
        else:
            return data

    except SQLAlchemyError as err: 
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error) 

