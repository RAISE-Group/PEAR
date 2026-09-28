@pytest.mark.parametrize('ser', [Series(np.arange(5)), Series(list('abcde')), Series(np.random.randn(5))])
def test_dt_accessor_invalid(self, ser):
    with pytest.raises(AttributeError, match='only use .dt accessor'):
        ser.dt
    assert not hasattr(ser, 'dt')