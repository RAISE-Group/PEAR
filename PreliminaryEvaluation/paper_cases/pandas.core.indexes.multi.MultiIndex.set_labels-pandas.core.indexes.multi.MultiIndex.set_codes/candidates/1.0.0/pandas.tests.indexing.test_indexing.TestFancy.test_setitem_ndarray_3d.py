@pytest.mark.parametrize('index', tm.all_index_generator(5), ids=lambda x: type(x).__name__)
@pytest.mark.parametrize('obj', [lambda i: Series(np.arange(len(i)), index=i), lambda i: DataFrame(np.random.randn(len(i), len(i)), index=i, columns=i)], ids=['Series', 'DataFrame'])
@pytest.mark.parametrize('idxr, idxr_id', [(lambda x: x, 'setitem'), (lambda x: x.loc, 'loc'), (lambda x: x.iloc, 'iloc')])
def test_setitem_ndarray_3d(self, index, obj, idxr, idxr_id):
    obj = obj(index)
    idxr = idxr(obj)
    nd3 = np.random.randint(5, size=(2, 2, 2))
    msg = "Buffer has wrong number of dimensions \\(expected 1, got 3\\)|'pandas._libs.interval.IntervalTree' object has no attribute 'set_value'|unhashable type: 'numpy.ndarray'|No matching signature found|^\\[\\[\\[|Index data must be 1-dimensional"
    if idxr_id == 'iloc' or (isinstance(obj, Series) and idxr_id == 'setitem' and (index.inferred_type in ['floating', 'string', 'datetime64', 'period', 'timedelta64', 'boolean', 'categorical'])):
        idxr[nd3] = 0
    else:
        err = (ValueError, AttributeError)
        with pytest.raises(err, match=msg):
            idxr[nd3] = 0