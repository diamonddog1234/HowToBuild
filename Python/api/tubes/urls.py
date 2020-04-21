from tubes.resources import AddTube, DeleteTube, ChangeTube, GetTubeList, GetTube
from tubes.tube_samples.resources import AddSample, ChangeSample, DeleteSample, GetSampleList, GetSample

urls = [
    (AddTube, '/api/tubes/add'),
    (DeleteTube, '/api/tubes/delete'),
    (ChangeTube, '/api/tubes/change'),
    (GetTubeList, '/api/tubes/list'),
    (GetTube, '/api/tubes/<int:tube_id>'),

    (AddSample, '/api/tubes/samples/add'),
    (ChangeSample, '/api/tubes/samples/change'),
    (DeleteSample, '/api/tubes/samples/delete'),
    (GetSampleList, '/api/tubes/samples/list'),
    (GetSample, '/api/tubes/samples/<int:sample_id>'),
]