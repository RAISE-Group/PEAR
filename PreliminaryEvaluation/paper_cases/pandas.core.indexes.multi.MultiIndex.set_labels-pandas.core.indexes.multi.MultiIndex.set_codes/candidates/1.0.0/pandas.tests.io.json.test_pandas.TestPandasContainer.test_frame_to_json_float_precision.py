@pytest.mark.skipif(is_platform_32bit(), reason='not compliant on 32-bit, xref #15865')
@pytest.mark.parametrize('value,precision,expected_val', [(0.95, 1, 1.0), (1.95, 1, 2.0), (-1.95, 1, -2.0), (0.995, 2, 1.0), (0.9995, 3, 1.0), (0.9999999999999994, 15, 1.0)])
def test_frame_to_json_float_precision(self, value, precision, expected_val):
    df = pd.DataFrame([dict(a_float=value)])
    encoded = df.to_json(double_precision=precision)
    assert encoded == f'{{"a_float":{{"0":{expected_val}}}}}'