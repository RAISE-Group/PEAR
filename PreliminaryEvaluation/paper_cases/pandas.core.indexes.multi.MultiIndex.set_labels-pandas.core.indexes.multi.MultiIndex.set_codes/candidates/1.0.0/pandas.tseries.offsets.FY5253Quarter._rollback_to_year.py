def _rollback_to_year(self, other):
    """
        Roll `other` back to the most recent date that was on a fiscal year
        end.

        Return the date of that year-end, the number of full quarters
        elapsed between that year-end and other, and the remaining Timedelta
        since the most recent quarter-end.

        Parameters
        ----------
        other : datetime or Timestamp

        Returns
        -------
        tuple of
        prev_year_end : Timestamp giving most recent fiscal year end
        num_qtrs : int
        tdelta : Timedelta
        """
    num_qtrs = 0
    norm = Timestamp(other).tz_localize(None)
    start = self._offset.rollback(norm)
    if start < norm:
        qtr_lens = self.get_weeks(norm)
        end = liboffsets.shift_day(start, days=7 * sum(qtr_lens))
        assert self._offset.is_on_offset(end), (start, end, qtr_lens)
        tdelta = norm - start
        for qlen in qtr_lens:
            if qlen * 7 <= tdelta.days:
                num_qtrs += 1
                tdelta -= Timedelta(days=qlen * 7)
            else:
                break
    else:
        tdelta = Timedelta(0)
    return (start, num_qtrs, tdelta)