from build.houses.resources import AddHouse, GetHouseList, GetHouse, GetPivotTable
from build.houses.resources import DeleteHouse
from build.houses.resources import ChangeHouse

urls = [
    (AddHouse, '/api/houses/add'),
    (DeleteHouse, '/api/houses/delete'),
    (ChangeHouse, '/api/houses/change'),
    (GetHouseList, '/api/houses/list'),
    (GetHouse, '/api/houses/<int:house_id>'),
    (GetPivotTable, '/api/houses/pivot')
]