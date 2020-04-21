from houses.resources import AddHouse, GetHouseList, GetHouse
from houses.resources import DeleteHouse
from houses.resources import ChangeHouse

urls = [
    (AddHouse, '/api/houses/add'),
    (DeleteHouse, '/api/houses/delete'),
    (ChangeHouse, '/api/houses/change'),
    (GetHouseList, '/api/houses/list'),
    (GetHouse, '/api/houses/<int:house_id>'),
]