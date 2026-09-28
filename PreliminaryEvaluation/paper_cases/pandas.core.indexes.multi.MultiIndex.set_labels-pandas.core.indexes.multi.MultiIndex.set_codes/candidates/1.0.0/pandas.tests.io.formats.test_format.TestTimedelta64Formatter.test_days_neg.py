def test_days_neg(self):
    x = pd.to_timedelta(list(range(5)) + [pd.NaT], unit='D')
    result = fmt.Timedelta64Formatter(-x, box=True).get_result()
    assert result[0].strip() == "'0 days'"
    assert result[1].strip() == "'-1 days'"