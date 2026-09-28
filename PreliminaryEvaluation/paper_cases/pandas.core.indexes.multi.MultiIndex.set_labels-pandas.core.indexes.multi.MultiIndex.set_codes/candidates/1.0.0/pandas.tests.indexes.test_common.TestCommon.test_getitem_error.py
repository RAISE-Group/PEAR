@pytest.mark.parametrize('itm', [101, 'no_int'])
@pytest.mark.filterwarnings('ignore::FutureWarning')
def test_getitem_error(self, indices, itm):
    with pytest.raises(IndexError):
        indices[itm]