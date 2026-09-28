@pytest.mark.parametrize('dtype, engine_type', [(np.int8, libindex.Int8Engine), (np.int16, libindex.Int16Engine), (np.int32, libindex.Int32Engine), (np.int64, libindex.Int64Engine)])
def test_engine_type(self, dtype, engine_type):
    if dtype != np.int64:
        num_uniques = {np.int8: 1, np.int16: 128, np.int32: 32768}[dtype]
        ci = pd.CategoricalIndex(range(num_uniques))
    else:
        ci = pd.CategoricalIndex(range(32768))
        ci.values._codes = ci.values._codes.astype('int64')
    assert np.issubdtype(ci.codes.dtype, dtype)
    assert isinstance(ci._engine, engine_type)