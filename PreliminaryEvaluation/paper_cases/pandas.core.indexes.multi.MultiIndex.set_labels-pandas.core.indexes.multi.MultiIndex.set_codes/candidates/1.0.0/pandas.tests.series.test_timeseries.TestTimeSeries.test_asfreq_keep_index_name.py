def test_asfreq_keep_index_name(self):
    index_name = 'bar'
    index = pd.date_range('20130101', periods=20, name=index_name)
    df = pd.DataFrame(list(range(20)), columns=['foo'], index=index)
    assert index_name == df.index.name
    assert index_name == df.asfreq('10D').index.name