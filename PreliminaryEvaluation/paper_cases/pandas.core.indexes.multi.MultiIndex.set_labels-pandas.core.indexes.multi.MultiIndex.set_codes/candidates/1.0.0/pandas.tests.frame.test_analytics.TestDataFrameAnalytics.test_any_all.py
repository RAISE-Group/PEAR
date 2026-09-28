@pytest.mark.parametrize('opname', ['any', 'all'])
def test_any_all(self, opname, bool_frame_with_na, float_string_frame):
    assert_bool_op_calc(opname, getattr(np, opname), bool_frame_with_na, has_skipna=True)
    assert_bool_op_api(opname, bool_frame_with_na, float_string_frame, has_bool_only=True)