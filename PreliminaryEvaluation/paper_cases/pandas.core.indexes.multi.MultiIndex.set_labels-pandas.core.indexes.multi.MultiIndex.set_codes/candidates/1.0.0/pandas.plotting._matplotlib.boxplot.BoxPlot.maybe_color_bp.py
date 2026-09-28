def maybe_color_bp(self, bp):
    if isinstance(self.color, dict):
        boxes = self.color.get('boxes', self._boxes_c)
        whiskers = self.color.get('whiskers', self._whiskers_c)
        medians = self.color.get('medians', self._medians_c)
        caps = self.color.get('caps', self._caps_c)
    else:
        boxes = self.color or self._boxes_c
        whiskers = self.color or self._whiskers_c
        medians = self.color or self._medians_c
        caps = self.color or self._caps_c
    setp(bp['boxes'], color=boxes, alpha=1)
    setp(bp['whiskers'], color=whiskers, alpha=1)
    setp(bp['medians'], color=medians, alpha=1)
    setp(bp['caps'], color=caps, alpha=1)