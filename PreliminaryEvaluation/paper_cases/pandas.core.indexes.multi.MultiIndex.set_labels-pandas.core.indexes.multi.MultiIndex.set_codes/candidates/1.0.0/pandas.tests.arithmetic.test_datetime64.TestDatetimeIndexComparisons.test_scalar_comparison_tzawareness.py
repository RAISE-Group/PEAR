@pytest.mark.parametrize('op', [operator.eq, operator.ne, operator.gt, operator.ge, operator.lt, operator.le])
@pytest.mark.parametrize('other', [datetime(2016, 1, 1), Timestamp('2016-01-01'), np.datetime64('2016-01-01')])
@pytest.mark.filterwarnings('ignore:elementwise comp:DeprecationWarning')
@pytest.mark.filterwarnings('ignore:Converting timezone-aware:FutureWarning')
def test_scalar_comparison_tzawareness(self, op, other, tz_aware_fixture, box_with_array):
    tz = tz_aware_fixture
    dti = pd.date_range('2016-01-01', periods=2, tz=tz)
    dtarr = tm.box_expected(dti, box_with_array)
    msg = 'Cannot compare tz-naive and tz-aware'
    with pytest.raises(TypeError, match=msg):
        op(dtarr, other)
    with pytest.raises(TypeError, match=msg):
        op(other, dtarr)