from flask_restplus import fields
from datetime import datetime
from src.config.restplus import api


data_request = api.model('Data Request', {
    'acc1': fields.Float(required=True) ,
    'acc2': fields.Float(required=True) ,
    'acc3': fields.Float(required=True) ,
    'gyro1': fields.Float(required=True) ,
    'gyro2': fields.Float(required=True) ,
    'gyro3': fields.Float(required=True) ,
    'countSteps': fields.Float(required=True)
})

data_result = api.model('Data Result', {
    'id': fields.Integer(required=True),
    'acc1': fields.Float(required=True) ,
    'acc2': fields.Float(required=True) ,
    'acc3': fields.Float(required=True) ,
    'gyro1': fields.Float(required=True) ,
    'gyro2': fields.Float(required=True) ,
    'gyro3': fields.Float(required=True) ,
    'countSteps': fields.Float(required=True) ,
    'createdAt': fields.String(required=True)
})

