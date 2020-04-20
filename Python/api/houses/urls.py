from houses.resources import AddHouse
from houses.resources import DeleteHouse

urls = [
    (AddHouse, '/api/houses/add'),
    (DeleteHouse, '/api/houses/delete'),
]