@pytest.mark.parametrize('df', [DataFrame(), DataFrame(columns=list('AB')), DataFrame(columns=list('AB'), index=range(3))])
def test_get_none(self, df):
    assert df.get(None) is None