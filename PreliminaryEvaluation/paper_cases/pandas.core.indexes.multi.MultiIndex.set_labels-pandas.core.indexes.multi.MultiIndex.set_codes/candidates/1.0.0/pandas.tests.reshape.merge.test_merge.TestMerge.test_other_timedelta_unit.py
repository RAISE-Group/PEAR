@pytest.mark.parametrize('unit', ['D', 'h', 'm', 's', 'ms', 'us', 'ns'])
def test_other_timedelta_unit(self, unit):
    df1 = pd.DataFrame({'entity_id': [101, 102]})
    s = pd.Series([None, None], index=[101, 102], name='days')
    dtype = 'm8[{}]'.format(unit)
    df2 = s.astype(dtype).to_frame('days')
    assert df2['days'].dtype == 'm8[ns]'
    result = df1.merge(df2, left_on='entity_id', right_index=True)
    exp = pd.DataFrame({'entity_id': [101, 102], 'days': np.array(['nat', 'nat'], dtype=dtype)}, columns=['entity_id', 'days'])
    tm.assert_frame_equal(result, exp)