@pytest.mark.slow
def test_donot_overwrite_index_name(self):
    df = DataFrame(randn(2, 2), columns=['a', 'b'])
    df.index.name = 'NAME'
    df.plot(y='b', label='LABEL')
    assert df.index.name == 'NAME'