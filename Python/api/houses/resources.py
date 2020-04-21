from flask import request, jsonify
from flask_restful import Resource

from core import get_database_session
from core.models import House, Street, District

from core.auth.jwt import check_role_validation


class AddHouse(Resource):
    @check_role_validation(['ChangeRecord'])
    def post(self):
        json_data = request.get_json()
        if 'street' not in json_data:
            return jsonify({'msg': 'no_street'})
        if 'district' not in json_data:
            return jsonify({'msg': 'no_district'})
        if 'minLayingDepth' not in json_data:
            return jsonify({'msg': 'no_minLayingDepth'})
        if 'maxLayingDepth' not in json_data:
            return jsonify({'msg': 'maxLayingDepth'})
        if 'number' not in json_data:
            return jsonify({'msg': 'no_number'})

        street = json_data['street']
        district = json_data['district']
        min_laying_depth = float(json_data['minLayingDepth'])
        max_laying_depth = float(json_data['maxLayingDepth'])
        number = str(json_data['number'])

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

        db_house = get_database_session().query(House).\
            filter(House.street_id == db_street.id).\
            filter(House.district_id == db_district.id).\
            filter(House.number == number).\
            first()
        if not db_house:
            house = House(street_id=db_street.id,
                          district_id=db_district.id,
                          min_laying_depth=min_laying_depth,
                          max_laying_depth=max_laying_depth,
                          number = number)
            get_database_session().add(house)
            get_database_session().commit()
        else:
            return jsonify({'msg': 'NOT_ORIGINAL_HOUSE'})
        return jsonify({'msg': 'OK', 'house_id': house.id})


class DeleteHouse(Resource):
    @check_role_validation(['ChangeRecord'])
    def post(self):
        json_data = request.get_json()
        if 'houseId' not in json_data:
            return jsonify({'msg': 'no_houseId'})
        house_id = int(json_data['houseId'])
        db_house = get_database_session().query(House).\
            filter(House.id == house_id).\
            first()
        if not db_house:
            return jsonify({'msg': 'NO_HOUSE'})
        get_database_session().delete(db_house)
        get_database_session().commit()
        return jsonify({'msg': 'OK'})


class ChangeHouse(Resource):
    @check_role_validation(['ChangeRecord'])
    def post(self):
        json_data = request.get_json()
        if 'houseId' not in json_data:
            return jsonify({'msg': 'no_houseId'})
        house_id = int(json_data['houseId'])
        db_house = get_database_session().query(House).\
            filter(House.id == house_id).\
            first()
        if not db_house:
            return jsonify({'msg': 'NO_HOUSE'})

        if 'street' in json_data:
            db_house.street = json_data['street']
        if 'district' in json_data:
            db_house.district_id = json_data['district']
        if 'minLayingDepth' in json_data:
            db_house.min_laying_depth = json_data['minLayingDepth']
        if 'maxLayingDepth' in json_data:
            db_house.max_laying_depth = json_data['maxLayingDepth']
        if 'number' in json_data:
            db_house.number = json_data['number']
        get_database_session().commit()
        return jsonify({'msg': 'OK'})