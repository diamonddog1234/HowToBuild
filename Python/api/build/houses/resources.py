from flask import request, jsonify
from flask_restful import Resource
from numpy.ma import arange

from build.utils.filter import filter_entity, advanced_filter_entity
from core import get_database_session
from core.models import House, Street, District, HouseFilterView, PivotView

from core.auth.jwt import check_role_validation, check_validation

def add_house(json_data):
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


class AddHouse(Resource):
    @check_role_validation(['ChangeRecord'])
    def post(self):
        json_data = request.get_json()
        if 'street' not in json_data:
            return jsonify({'msg': 'no_street'})
        print(json_data)
        if 'district' not in json_data:
            return jsonify({'msg': 'no_district'})
        #if 'minLayingDepth' not in json_data:
        #    return jsonify({'msg': 'no_minLayingDepth'})
        #if 'maxLayingDepth' not in json_data:
        #    return jsonify({'msg': 'maxLayingDepth'})
        if 'number' not in json_data:
            return jsonify({'msg': 'no_number'})

        street = json_data['street']
        district = json_data['district']

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
                          number = number)

            if 'buildYear' in json_data:
                house.build_year = int(json_data['buildYear'])

            if 'lng' in json_data:
                house.lng = json_data['lng']

            if 'lat' in json_data:
                house.lat = json_data['lat']

            if 'minLayingDepth' in json_data:
                house.min_laying_depth = float(json_data['minLayingDepth'])
            if 'maxLayingDepth' in json_data:
                house.max_laying_depth = float(json_data['maxLayingDepth'])

            get_database_session().add(house)
            get_database_session().commit()
        else:
            return jsonify({'msg': 'NOT_ORIGINAL_HOUSE'})
        return jsonify({'msg': 'OK', 'house_id': house.id})


class DeleteHouse(Resource):
    @check_role_validation(['ChangeRecord'])
    def post(self):
        json_data = request.get_json()
        if 'id' not in json_data:
            return jsonify({'msg': 'no_id'})

        house_id = int(json_data['id'])
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
        if 'id' not in json_data:
            return jsonify({'msg': 'no_id'})
        house_id = int(json_data['id'])
        db_house = get_database_session().query(House).\
            filter(House.id == house_id).\
            first()
        if not db_house:
            return jsonify({'msg': 'NO_HOUSE'})
        new_street = db_house.street
        new_district = db_house.district
        new_min_laying_depth = db_house.min_laying_depth
        new_max_laying_depth = db_house.max_laying_depth
        new_number = db_house.number
        new_build_year = db_house.build_year
        if 'street' in json_data:
            new_street = get_database_session().query(Street).filter(Street.value == json_data['street']).first()
            if not new_street:
                new_street = Street(value=json_data['street'])
                get_database_session().add(new_street)
                get_database_session().flush()
        if 'district' in json_data:
            new_district = get_database_session().query(District).\
                filter(District.value == json_data['district']).first()
            if not new_district:
                new_district = District(value=json_data['district'])
                get_database_session().add(new_district)
                get_database_session().flush()
        if 'minLayingDepth' in json_data:
            new_min_laying_depth = json_data['minLayingDepth']
        if 'maxLayingDepth' in json_data:
            new_max_laying_depth = json_data['maxLayingDepth']
        if 'number' in json_data:
            new_number = json_data['number']
        if json_data['buildYear']:
            new_build_year = int(json_data['buildYear'])
        db_house_repeat = get_database_session().query(House).\
            filter(House.street_id == new_street.id).\
            filter(House.district_id == new_district.id).\
            filter(House.number == new_number).\
            filter(House.id != house_id).\
            first()

        if db_house_repeat:
            return jsonify({'msg': 'NOT_ORIGINAL_HOUSE'})

        db_house.street = new_street
        db_house.district = new_district
        db_house.number = new_number
        db_house.min_laying_depth = new_min_laying_depth
        db_house.max_laying_depth = new_max_laying_depth
        db_house.build_year = new_build_year
        get_database_session().commit()
        return jsonify({'msg': 'OK'})


class GetHouseList(Resource):
    @check_validation
    def post(self):
        data = filter_entity(entity_class=HouseFilterView)
        return data


class GetHouse(Resource):
    @check_validation
    def post(self, house_id):
        json_data = request.get_json()
        db_house = get_database_session().query(House).filter(House.id == house_id).first()
        if not db_house:
            return jsonify({'msg': 'NO_HOUSE'})
        return jsonify(db_house.to_basic_dictionary())


mouths = ['Январь', 'Февраль', 'Март', 'Апрель','Май','Июнь','Июль','Август','Сентябрь','Октябрь','Ноябрь','Декабрь'];

class GetPivotTable(Resource):
    @check_validation
    def post(self):

        json_data = request.get_json()
        pivot_view_filter = advanced_filter_entity(PivotView)
        count = pivot_view_filter['count']

        pivot_view = pivot_view_filter['entities']

        if not pivot_view:
            return jsonify({'msg': 'NO_HOUSE'})

        min = 1
        max = 1

        result = {}
        result['entities'] = []
        depths = []
        samples_datekey_all = {}
        for sample in pivot_view:
            depths.append(sample.depth)
            if sample.depth > max:
                max = int(sample.depth)
            if sample.tubeId not in samples_datekey_all:
                samples_datekey_all[sample.tubeId] = {}
            if 'dates' not in samples_datekey_all[sample.tubeId]:
                samples_datekey_all[sample.tubeId]['dates'] = {}
            samples_datekey_all[sample.tubeId]['value'] = sample.tube
            samples_datekey_all[sample.tubeId]['houseId'] = sample.houseId
            samples_datekey_all[sample.tubeId]['tubeId'] = sample.tubeId
            if sample.date.strftime('%d-%m-%Y') in samples_datekey_all[sample.tubeId]['dates']:
                count = count-1
            samples_datekey_all[sample.tubeId]['dates'][sample.date.strftime('%d-%m-%Y')] = []

        depths = tuple(range(min, max+1))

        for sample in pivot_view:
            for depth in depths:
                if len(samples_datekey_all[sample.tubeId]['dates'][sample.date.strftime('%d-%m-%Y')]) < depth:
                    samples_datekey_all[sample.tubeId]['dates'][sample.date.strftime('%d-%m-%Y')].append('-')
                if sample.depth == depth:
                    samples_datekey_all[sample.tubeId]['dates'][sample.date.strftime('%d-%m-%Y')][depth-1] = sample.value

        result = {}
        result['entities'] = []
        for tube_key in samples_datekey_all:
            for date_key in samples_datekey_all[tube_key]['dates']:
                result['entities'].append({
                    'quarter': int(int(date_key.split('-')[1])/4)+1,
                    'date': date_key,
                    'month': mouths[int(date_key.split('-')[1])-1] + ' (' + str(  int(date_key.split('-')[1])) + ')' ,
                    'day': int(date_key.split('-')[0]),
                    'year': int(date_key.split('-')[2]),
                    'tube': samples_datekey_all[tube_key]['value'],
                    'houseId': samples_datekey_all[tube_key]['houseId'],
                    'tubeId': samples_datekey_all[tube_key]['tubeId'],
                    'depth_values': samples_datekey_all[tube_key]['dates'][date_key]
                })
        result['count'] = len(result['entities'])
        if 'pagination' in json_data:
            pagination_data = json_data['pagination']
            offset = pagination_data['currentPage'] * pagination_data['rowsPerPage']
            result['entities'] = result['entities'][offset:offset+pagination_data['rowsPerPage']]
        result['depths'] = depths

        return jsonify(result)