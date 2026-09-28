@pytest.mark.parametrize('cast_as_obj', [True, False])
@pytest.mark.parametrize('index', [pd.date_range('2015-01-01 10:00', freq='D', periods=3, tz='US/Eastern', name='Green Eggs & Ham'), pd.date_range('2015-01-01 10:00', freq='D', periods=3), pd.timedelta_range('1 days', freq='D', periods=3), pd.period_range('2015-01-01', freq='D', periods=3)])
def test_constructor_from_index_dtlike(self, cast_as_obj, index):
    if cast_as_obj:
        result = pd.Index(index.astype(object))
    else:
        result = pd.Index(index)
    tm.assert_index_equal(result, index)
    if isinstance(index, pd.DatetimeIndex):
        assert result.tz == index.tz
        if cast_as_obj:
            index += pd.Timedelta(nanoseconds=50)
            result = pd.Index(index, dtype=object)
            assert result.dtype == np.object_
            assert list(result) == list(index)