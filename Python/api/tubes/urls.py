from tubes.resources import AddTube, DeleteTube, ChangeTube

urls = [
    (AddTube, '/api/tubes/add'),
    (DeleteTube, '/api/tubes/delete'),
    (ChangeTube, '/api/tubes/change')
]