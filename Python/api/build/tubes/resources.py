from flask import request, jsonify
from flask_restful import Resource

from core import get_database_session
from core.auth.jwt import check_role_validation, check_validation
from core.models import Tube, TubeFilterView

from api.build.utils.filter import filter_entity


class AddTube(Resource):
    @check_role_validation(['ChangeRecord'])
    def post(self):
        json_data = request.get_json()
        if 'value' not in json_data:
            return jsonify({'msg': 'no_value'})
        if 'depth' not in json_data:
            return jsonify({'msg': 'no_depth'})
        if 'houseId' not in json_data:
            return jsonify({'msg': 'no_houseId'})

        value = str(json_data['value'])
        depth = float(json_data['depth'])
        house_id = int(json_data['houseId'])

        db_tube = get_database_session().query(Tube).\
            filter(Tube.value == value).\
            filter(Tube.house_id == house_id).first()
        if db_tube:
            return jsonify({'msg': 'NOT_ORIGINAL_TUBE'})
        else:
            tube = Tube(value=value, depth=depth, house_id=house_id)
            try:
                get_database_session().add(tube)
                get_database_session().commit()
            except:
                return jsonify({'msg': 'NO_HOUSE'})
        return jsonify({'msg': 'OK', 'tube_id': tube.id})


class ChangeTube(Resource):
    @check_role_validation(['ChangeRecord'])
    def post(self):
        json_data = request.get_json()
        if 'id' not in json_data:
            return jsonify({'msg': 'no_tubeId'})

        tube_id = int(json_data['id'])
        db_tube = get_database_session().query(Tube).\
            filter(Tube.id == tube_id).\
            first()

        if not db_tube:
            return jsonify({'msg': 'NO_TUBE'})

        if 'value' in json_data:
            if json_data['value'] != db_tube.value:
                db_tube_repeat = get_database_session().query(Tube). \
                    filter(Tube.value == json_data['value']). \
                    first()
                if db_tube_repeat:
                    return jsonify({'msg': 'NOT_ORIGINAL_TUBE'})
                else:
                    db_tube.value = str(json_data['value'])
        if 'depth' in json_data:
            db_tube.depth = float(json_data['depth'])
        if 'houseId' in json_data:
            db_tube.house_id = int(json_data['houseId'])
        get_database_session().commit()
        return jsonify({'msg': 'OK'})


class DeleteTube(Resource):
    @check_role_validation(['ChangeRecord'])
    def post(self):
        json_data = request.get_json()
        if 'id' not in json_data:
            return jsonify({'msg': 'no_tubeId'})
        tube_id = int(json_data['id'])
        db_tube = get_database_session().query(Tube).\
            filter(Tube.id == tube_id).\
            first()

        if not db_tube:
            return jsonify({'msg': 'NO_TUBE'})
        get_database_session().delete(db_tube)
        get_database_session().commit()

        return jsonify({'msg': 'OK'})


class GetTubeList(Resource):
    @check_validation
    def post(self):
        data = filter_entity(entity_class=TubeFilterView)
        return data


class GetTube(Resource):
    @check_validation
    def post(self, tube_id):
        db_tube = get_database_session().query(Tube).filter(Tube.id == tube_id).first()
        if not db_tube:
            return jsonify({'msg': 'NO_TUBE'})
        return jsonify(db_tube.to_basic_dictionary())
