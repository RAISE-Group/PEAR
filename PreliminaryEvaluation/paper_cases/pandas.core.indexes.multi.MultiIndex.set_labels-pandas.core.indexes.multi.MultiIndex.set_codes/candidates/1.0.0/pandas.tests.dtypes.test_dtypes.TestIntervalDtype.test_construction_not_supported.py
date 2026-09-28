@pytest.mark.parametrize('subtype', [CategoricalDtype(list('abc'), False), CategoricalDtype(list('wxyz'), True), object, str, '<U10', 'interval[category]', 'interval[object]'])
def test_construction_not_supported(self, subtype):
    msg = 'category, object, and string subtypes are not supported for IntervalDtype'
    with pytest.raises(TypeError, match=msg):
        IntervalDtype(subtype)