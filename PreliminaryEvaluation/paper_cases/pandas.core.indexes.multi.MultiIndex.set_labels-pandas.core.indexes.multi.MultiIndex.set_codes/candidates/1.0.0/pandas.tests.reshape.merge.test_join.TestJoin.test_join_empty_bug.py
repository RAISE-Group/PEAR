def test_join_empty_bug(self):
    x = DataFrame()
    x.join(DataFrame([3], index=[0], columns=['A']), how='outer')