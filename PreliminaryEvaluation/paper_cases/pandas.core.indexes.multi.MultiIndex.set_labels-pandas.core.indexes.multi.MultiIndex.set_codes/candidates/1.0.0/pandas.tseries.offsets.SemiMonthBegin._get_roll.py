def _get_roll(self, i, before_day_of_month, after_day_of_month):
    n = self.n
    is_month_start = i.is_month_start
    if n > 0:
        roll = np.where(before_day_of_month, n, n + 1)
    elif n == 0:
        roll_start = np.where(is_month_start, 0, 1)
        roll_after = np.where(after_day_of_month, 1, 0)
        roll = roll_start + roll_after
    else:
        roll_after = np.where(after_day_of_month, n + 2, n + 1)
        roll_start = np.where(is_month_start, -1, 0)
        roll = roll_after + roll_start
    return roll