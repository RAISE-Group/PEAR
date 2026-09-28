def test_numeric_values(self):
    assert nanops._ensure_numeric(1) == 1
    assert nanops._ensure_numeric(1.1) == 1.1
    assert nanops._ensure_numeric(1 + 2j) == 1 + 2j