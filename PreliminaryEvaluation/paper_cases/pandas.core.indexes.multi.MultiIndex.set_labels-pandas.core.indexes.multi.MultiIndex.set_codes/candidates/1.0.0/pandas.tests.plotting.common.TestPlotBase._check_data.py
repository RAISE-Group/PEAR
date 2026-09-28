def _check_data(self, xp, rs):
    """
        Check each axes has identical lines

        Parameters
        ----------
        xp : matplotlib Axes object
        rs : matplotlib Axes object
        """
    xp_lines = xp.get_lines()
    rs_lines = rs.get_lines()

    def check_line(xpl, rsl):
        xpdata = xpl.get_xydata()
        rsdata = rsl.get_xydata()
        tm.assert_almost_equal(xpdata, rsdata)
    assert len(xp_lines) == len(rs_lines)
    [check_line(xpl, rsl) for xpl, rsl in zip(xp_lines, rs_lines)]
    tm.close()