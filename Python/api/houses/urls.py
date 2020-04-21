from houses.resources import AddHouse
from houses.resources import DeleteHouse
from houses.resources import ChangeHouse

urls = [
    (AddHouse, '/api/houses/add'),
    (DeleteHouse, '/api/houses/delete'),
    (ChangeHouse, '/api/houses/change'),
]