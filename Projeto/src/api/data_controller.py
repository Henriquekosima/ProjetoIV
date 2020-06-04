from flask import request
from flask_restplus import Resource
from src.config.restplus import api
from src.api.serializers.data_serializer import data_request, data_result
from src.services.data_service import create, get_all
 

ns = api.namespace('api/data', description='Operations related to data')


@ns.route('')#define rota
class DataCollection(Resource):
    @api.expect(data_request)#define parametro de entrada para a documentaçao do swagger
    @api.marshal_with(data_result)#define resultado da metodo 
    def post(self):
        """
        Create a new Data
        """ 
        data = create(request.json)
        return data 

    @api.marshal_with(data_result)#define resultado da metodo 
    def get(self):
        data_list = get_all()
        return data_list

 

