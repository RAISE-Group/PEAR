def test_register_by_default(self):
    code = "'import matplotlib.units; import pandas as pd; units = dict(matplotlib.units.registry); assert pd.Timestamp in units)'"
    call = [sys.executable, '-c', code]
    assert subprocess.check_call(call) == 0