@pytest.mark.parametrize('dtype', [True, False])
@pytest.mark.parametrize('convert_axes', [True, False])
@pytest.mark.parametrize('numpy', [True, False])
def test_frame_from_json_missing_data(self, orient, convert_axes, numpy, dtype):
    num_df = DataFrame([[1, 2], [4, 5, 6]])
    result = read_json(num_df.to_json(orient=orient), orient=orient, convert_axes=convert_axes, dtype=dtype)
    assert np.isnan(result.iloc[0, 2])
    obj_df = DataFrame([['1', '2'], ['4', '5', '6']])
    result = read_json(obj_df.to_json(orient=orient), orient=orient, convert_axes=convert_axes, dtype=dtype)
    if not dtype:
        assert result.iloc[0, 2] is None
    else:
        assert np.isnan(result.iloc[0, 2])