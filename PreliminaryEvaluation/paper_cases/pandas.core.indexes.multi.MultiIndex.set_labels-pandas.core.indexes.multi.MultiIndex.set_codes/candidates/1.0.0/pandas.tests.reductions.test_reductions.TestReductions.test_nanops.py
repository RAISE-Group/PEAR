def test_nanops(self):
    for opname in ['max', 'min']:
        for klass in [Index, Series]:
            arg_op = 'arg' + opname if klass is Index else 'idx' + opname
            obj = klass([np.nan, 2.0])
            assert getattr(obj, opname)() == 2.0
            obj = klass([np.nan])
            assert pd.isna(getattr(obj, opname)())
            assert pd.isna(getattr(obj, opname)(skipna=False))
            obj = klass([], dtype=object)
            assert pd.isna(getattr(obj, opname)())
            assert pd.isna(getattr(obj, opname)(skipna=False))
            obj = klass([pd.NaT, datetime(2011, 11, 1)])
            assert getattr(obj, opname)() == datetime(2011, 11, 1)
            assert getattr(obj, opname)(skipna=False) is pd.NaT
            assert getattr(obj, arg_op)() == 1
            result = getattr(obj, arg_op)(skipna=False)
            if klass is Series:
                assert np.isnan(result)
            else:
                assert result == -1
            obj = klass([pd.NaT, datetime(2011, 11, 1), pd.NaT])
            assert getattr(obj, opname)(), datetime(2011, 11, 1)
            assert getattr(obj, opname)(skipna=False) is pd.NaT
            assert getattr(obj, arg_op)() == 1
            result = getattr(obj, arg_op)(skipna=False)
            if klass is Series:
                assert np.isnan(result)
            else:
                assert result == -1
            for dtype in ['M8[ns]', 'datetime64[ns, UTC]']:
                obj = klass([], dtype=dtype)
                assert getattr(obj, opname)() is pd.NaT
                assert getattr(obj, opname)(skipna=False) is pd.NaT
                with pytest.raises(ValueError, match='empty sequence'):
                    getattr(obj, arg_op)()
                with pytest.raises(ValueError, match='empty sequence'):
                    getattr(obj, arg_op)(skipna=False)
    obj = Index(np.arange(5, dtype='int64'))
    assert obj.argmin() == 0
    assert obj.argmax() == 4
    obj = Index([np.nan, 1, np.nan, 2])
    assert obj.argmin() == 1
    assert obj.argmax() == 3
    assert obj.argmin(skipna=False) == -1
    assert obj.argmax(skipna=False) == -1
    obj = Index([np.nan])
    assert obj.argmin() == -1
    assert obj.argmax() == -1
    assert obj.argmin(skipna=False) == -1
    assert obj.argmax(skipna=False) == -1
    obj = Index([pd.NaT, datetime(2011, 11, 1), datetime(2011, 11, 2), pd.NaT])
    assert obj.argmin() == 1
    assert obj.argmax() == 2
    assert obj.argmin(skipna=False) == -1
    assert obj.argmax(skipna=False) == -1
    obj = Index([pd.NaT])
    assert obj.argmin() == -1
    assert obj.argmax() == -1
    assert obj.argmin(skipna=False) == -1
    assert obj.argmax(skipna=False) == -1