def _get_roll(self, i, before_day_of_month, after_day_of_month):
    n = self.n
    is_month_end = i.is_month_end
    if n > 0:
        roll_end = np.where(is_month_end, 1, 0)
        roll_before = np.where(before_day_of_month, n, n + 1)
        roll = roll_end + roll_before
    elif n == 0:
        roll_after = np.where(after_day_of_month, 2, 0)
        roll_before = np.where(~after_day_of_month, 1, 0)
        roll = roll_before + roll_after
    else:
        roll = np.where(after_day_of_month, n + 2, n + 1)
    return roll