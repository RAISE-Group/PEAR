@pytest.mark.parametrize('index', tm.all_index_generator(5), ids=lambda x: type(x).__name__)
@pytest.mark.parametrize('obj', [lambda i: Series(np.arange(len(i)), index=i), lambda i: DataFrame(np.random.randn(len(i), len(i)), index=i, columns=i)], ids=['Series', 'DataFrame'])
@pytest.mark.parametrize('idxr, idxr_id', [(lambda x: x, 'getitem'), (lambda x: x.loc, 'loc'), (lambda x: x.iloc, 'iloc')])
def test_getitem_ndarray_3d(self, index, obj, idxr, idxr_id):
    obj = obj(index)
    idxr = idxr(obj)
    nd3 = np.random.randint(5, size=(2, 2, 2))
    msg = 'Buffer has wrong number of dimensions \\(expected 1, got 3\\)|Cannot index with multidimensional key|Wrong number of dimensions. values.ndim != ndim \\[3 != 1\\]|Index data must be 1-dimensional'
    if isinstance(obj, Series) and idxr_id == 'getitem' and (index.inferred_type in ['string', 'datetime64', 'period', 'timedelta64', 'boolean', 'categorical']):
        with tm.assert_produces_warning(DeprecationWarning, check_stacklevel=False):
            idxr[nd3]
    else:
        with pytest.raises(ValueError, match=msg):
            with tm.assert_produces_warning(DeprecationWarning):
                idxr[nd3]