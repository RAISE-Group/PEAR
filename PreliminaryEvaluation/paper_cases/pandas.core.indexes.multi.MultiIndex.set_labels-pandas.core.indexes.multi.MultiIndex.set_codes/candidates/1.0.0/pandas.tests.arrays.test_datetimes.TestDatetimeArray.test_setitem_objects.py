@pytest.mark.parametrize('obj', [pd.Timestamp.now(), pd.Timestamp.now().to_datetime64(), pd.Timestamp.now().to_pydatetime()])
def test_setitem_objects(self, obj):
    dti = pd.date_range('2000', periods=2, freq='D')
    arr = dti._data
    arr[0] = obj
    assert arr[0] == obj