def test_nat_representations(self):
    for f in (str, repr, methodcaller('isoformat')):
        assert f(pd.NaT) == 'NaT'