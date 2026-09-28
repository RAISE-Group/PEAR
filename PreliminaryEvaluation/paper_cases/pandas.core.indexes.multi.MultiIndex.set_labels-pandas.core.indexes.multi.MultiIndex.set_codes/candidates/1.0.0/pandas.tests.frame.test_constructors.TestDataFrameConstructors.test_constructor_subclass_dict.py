def test_constructor_subclass_dict(self, float_frame, dict_subclass):
    data = {'col1': dict_subclass(((x, 10.0 * x) for x in range(10))), 'col2': dict_subclass(((x, 20.0 * x) for x in range(10)))}
    df = DataFrame(data)
    refdf = DataFrame({col: dict(val.items()) for col, val in data.items()})
    tm.assert_frame_equal(refdf, df)
    data = dict_subclass(data.items())
    df = DataFrame(data)
    tm.assert_frame_equal(refdf, df)
    from collections import defaultdict
    data = {}
    float_frame['B'][:10] = np.nan
    for k, v in float_frame.items():
        dct = defaultdict(dict)
        dct.update(v.to_dict())
        data[k] = dct
    frame = DataFrame(data)
    expected = frame.reindex(index=float_frame.index)
    tm.assert_frame_equal(float_frame, expected)