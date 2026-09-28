@pytest.mark.parametrize('inp', ['geopoint', 'geojson', 'fake_type'])
def test_convert_json_field_to_pandas_type_raises(self, inp):
    field = {'type': inp}
    with pytest.raises(ValueError, match=f'Unsupported or invalid field type: {inp}'):
        convert_json_field_to_pandas_type(field)