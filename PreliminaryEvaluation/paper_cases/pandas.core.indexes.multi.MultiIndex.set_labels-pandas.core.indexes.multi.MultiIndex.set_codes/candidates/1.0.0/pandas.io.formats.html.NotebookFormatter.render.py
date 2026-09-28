def render(self) -> List[str]:
    self.write('<div>')
    self.write_style()
    super().render()
    self.write('</div>')
    return self.elements