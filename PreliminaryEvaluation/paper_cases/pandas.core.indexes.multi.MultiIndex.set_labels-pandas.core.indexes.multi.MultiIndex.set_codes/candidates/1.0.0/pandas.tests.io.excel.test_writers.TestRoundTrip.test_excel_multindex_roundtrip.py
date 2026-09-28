@td.skip_if_no('xlsxwriter')
@pytest.mark.parametrize('c_idx_names', [True, False])
@pytest.mark.parametrize('r_idx_names', [True, False])
@pytest.mark.parametrize('c_idx_levels', [1, 3])
@pytest.mark.parametrize('r_idx_levels', [1, 3])
def test_excel_multindex_roundtrip(self, ext, c_idx_names, r_idx_names, c_idx_levels, r_idx_levels):
    with tm.ensure_clean(ext) as pth:
        if c_idx_levels == 1 and c_idx_names:
            pytest.skip("Column index name cannot be serialized unless it's a MultiIndex")
        check_names = r_idx_names or r_idx_levels <= 1
        df = tm.makeCustomDataframe(5, 5, c_idx_names, r_idx_names, c_idx_levels, r_idx_levels)
        df.to_excel(pth)
        act = pd.read_excel(pth, index_col=list(range(r_idx_levels)), header=list(range(c_idx_levels)))
        tm.assert_frame_equal(df, act, check_names=check_names)
        df.iloc[0, :] = np.nan
        df.to_excel(pth)
        act = pd.read_excel(pth, index_col=list(range(r_idx_levels)), header=list(range(c_idx_levels)))
        tm.assert_frame_equal(df, act, check_names=check_names)
        df.iloc[-1, :] = np.nan
        df.to_excel(pth)
        act = pd.read_excel(pth, index_col=list(range(r_idx_levels)), header=list(range(c_idx_levels)))
        tm.assert_frame_equal(df, act, check_names=check_names)