@pytest.mark.parametrize('box', [pd.Series, pd.DataFrame])
def test_axis_classmethods(self, box):
    obj = box(dtype=object)
    values = list(box._AXIS_NAMES.keys()) + list(box._AXIS_NUMBERS.keys()) + list(box._AXIS_ALIASES.keys())
    for v in values:
        assert obj._get_axis_number(v) == box._get_axis_number(v)
        assert obj._get_axis_name(v) == box._get_axis_name(v)
        assert obj._get_block_manager_axis(v) == box._get_block_manager_axis(v)