from operator import or_

from flask import request

from core import get_database_session


def filter_like_query(filter_data):
    if filter_data['value'] == '':
        return  filter_data['query']
    return filter_data['query'].\
        filter(getattr(filter_data['entity_class'], filter_data['key']).\
               like('%' + str(filter_data['value']) + '%'))


def filter_equal(filter_data):
    if filter_data['value'] == '':
        return  filter_data['query']
    return filter_data['query'].\
        filter(getattr(filter_data['entity_class'], filter_data['key']) == filter_data['value'])


def filter_more(filter_data):
    if filter_data['value'] == '':
        return  filter_data['query']
    return filter_data['query'].\
        filter(getattr(filter_data['entity_class'], filter_data['key']) > filter_data['value'])

def filter_less(filter_data):
    if filter_data['value'] == '':
        return  filter_data['query']
    return filter_data['query'].\
        filter(getattr(filter_data['entity_class'], filter_data['key']) < filter_data['value'])

def filter_more_qual(filter_data):
    if filter_data['value'] == '':
        return  filter_data['query']
    return filter_data['query'].\
        filter(getattr(filter_data['entity_class'], filter_data['key']) >= filter_data['value'])

def filter_less_equal(filter_data):
    if filter_data['value'] == '':
        return  filter_data['query']
    return filter_data['query'].\
        filter(getattr(filter_data['entity_class'], filter_data['key']) <= filter_data['value'])

def filter_in_range(filter_data):
    if filter_data['value'] == '':
        return  filter_data['query']
    split = filter_data['value'].split(';')
    a = float(split[0][1:])
    b = float(split[1][:-1])
    if b < a:
        a, b = b, a
    return filter_data['query'].\
        filter(getattr(filter_data['entity_class'], filter_data['key']) <= b).\
        filter(getattr(filter_data['entity_class'], filter_data['key']) >= a)

def filter_out_range(filter_data):
    if filter_data['value'] == '':
        return  filter_data['query']
    split = filter_data['value'].split(';')
    a = float(split[0][1:])
    b = float(split[1][:-1])

    if b < a:
        a, b = b, a

    print(a)
    return filter_data['query'].\
        filter(or_(getattr(filter_data['entity_class'], filter_data['key']) < a,
                   getattr(filter_data['entity_class'], filter_data['key']) > b))


filter_type_funcs = {
    'like': filter_like_query,
    'equal': filter_equal,
    'more': filter_more,
    'less': filter_less,
    'lessEqual': filter_less_equal,
    'moreEqual': filter_less_equal,
    'inRange': filter_in_range,
    'outRange': filter_out_range,
}

def filter_entity(entity_class):
    query = get_database_session().query(entity_class)
    count = 0
    if request.headers.get('content-type') == 'application/json':
        json_data = request.get_json()
        if 'filter' in json_data:
            filter = json_data['filter']
            if filter:
                for filter_key, filter_array in filter.items():
                    for filter in filter_array:
                        if hasattr(entity_class, filter_key):
                            filter_data = {
                               'entity_class': entity_class,
                               'query': query,
                               'key': filter_key,
                               'value': filter['value']
                            }

                            if filter['type'] in filter_type_funcs:
                                query = (filter_type_funcs[filter['type']](filter_data=filter_data))
    all = query.all()
    count = len(all)
    if 'pagination' in json_data:
        pagination_data = json_data['pagination']
        query = query.limit(pagination_data['rowsPerPage'])
        query = query.offset(pagination_data['currentPage'] * pagination_data['rowsPerPage'])
    all = query.all()
    return { 'count': count, 'entities': [entity.to_basic_dictionary() for entity in all] }