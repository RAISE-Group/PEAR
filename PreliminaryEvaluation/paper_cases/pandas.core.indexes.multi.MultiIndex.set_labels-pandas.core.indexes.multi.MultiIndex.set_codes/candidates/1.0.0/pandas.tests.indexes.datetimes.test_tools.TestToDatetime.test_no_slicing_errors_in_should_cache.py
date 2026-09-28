@pytest.mark.parametrize('listlike', [deque([pd.Timestamp('2010-06-02 09:30:00')] * 51), [pd.Timestamp('2010-06-02 09:30:00')] * 51, tuple([pd.Timestamp('2010-06-02 09:30:00')] * 51)])
def test_no_slicing_errors_in_should_cache(self, listlike):
    assert tools.should_cache(listlike) is True