def _get_wom_rule(self) -> Optional[str]:
    weekdays = unique(self.index.weekday)
    if len(weekdays) > 1:
        return None
    week_of_months = unique((self.index.day - 1) // 7)
    week_of_months = week_of_months[week_of_months < 4]
    if len(week_of_months) == 0 or len(week_of_months) > 1:
        return None
    week = week_of_months[0] + 1
    wd = int_to_weekday[weekdays[0]]
    return f'WOM-{week}{wd}'