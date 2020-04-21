from flask import request, jsonify
from flask_restful import Resource

from core import get_database_session
from core.auth.jwt import check_role_validation
from core.models import TubeSample


class AddSample(Resource):
    @check_role_validation(['ChangeRecord'])
    def post(self):
        json_data = request.get_json()
        if 'tubeId' not in json_data:
            return jsonify({'msg': 'no_tubeId'})
        if 'depth' not in json_data:
            return jsonify({'msg': 'no_depth'})
        if 'date' not in json_data:
            return jsonify({'msg': 'no_date'})
        if 'value' not in json_data:
            return jsonify({'msg': 'no_value'})

        value = float(json_data['value'])
        depth = float(json_data['depth'])
        tube_id = int(json_data['houseId'])
        date = int(json_data['date'])

        db_sample = get_database_session().query(TubeSample).\
            filter(TubeSample.tube_id == tube_id).\
            filter(TubeSample.date == date).first()
        if db_sample:
            return jsonify({'msg': 'NOT_ORIGINAL_SAMPLE'})
        else:
            sample = TubeSample(value = value, depth = depth, tube_id = tube_id, date = date)
            try:
                get_database_session().add(sample)
                get_database_session().commit()
            except:
                return jsonify({'msg': 'NO_TUBE'})
        return jsonify({'msg': 'OK', 'sample_id': sample.id})