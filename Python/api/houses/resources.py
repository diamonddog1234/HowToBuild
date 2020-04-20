from flask import request, jsonify
from flask_restful import Resource

from Python.api.core import get_database_session
from Python.api.core.models import House, Street, District


class AddHouse(Resource):
    def post(self):
        json_data = request.get_json()
        if 'street' not in json_data:
            return jsonify({'msg': 'no_street'})
        if 'district' not in json_data:
            return jsonify({'msg': 'no_district'})
        if 'min_laying_depth' not in json_data:
            return jsonify({'msg': 'min_laying_depth'})
        if 'max_laying_depth' not in json_data:
            return jsonify({'msg': 'max_laying_depth'})

        street = json_data['street']
        district = json_data['district']
        min_laying_depth = json_data['min_laying_depth']
        max_laying_depth = json_data['max_laying_depth']

        db_street = get_database_session().query(Street).filter(Street.value == street).first()
        if not db_street:
            db_street = Street(value = street)
            get_database_session().add(db_street)
            get_database_session().flush()

        db_district = get_database_session().query(District).filter(District.value == district).first()
        if not db_district:
            db_district = District(value = district)
            get_database_session().add(db_district)
            get_database_session().flush()

        # house = House()

        return jsonify({'msg': 'OK'})