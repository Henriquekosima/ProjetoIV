from . import db 
from datetime import datetime

#configura modelo de dados do AUTHOR
class Data(db.Model):
    __tablename__ = 'data'

    id = db.Column(db.Integer, primary_key=True)
    acc1 = db.Column(db.Float())
    acc2 = db.Column(db.Float())
    acc3 = db.Column(db.Float())
    gyro1 = db.Column(db.Float())
    gyro2 = db.Column(db.Float())
    gyro3 = db.Column(db.Float())
    countSteps = db.Column(db.Float())
    createdAt = db.Column(db.DateTime())

    def get_user_id(self):
        return self.id

  

