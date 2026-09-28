@pytest.mark.parametrize('orient', ['index', 'columns'])
def test_frame_non_unique_index_raises(self, orient):
    df = DataFrame([['a', 'b'], ['c', 'd']], index=[1, 1], columns=['x', 'y'])
    msg = f"DataFrame index must be unique for orient='{orient}'"
    with pytest.raises(ValueError, match=msg):
        df.to_json(orient=orient)