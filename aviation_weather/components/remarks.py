from aviation_weather.components import _Component
from aviation_weather.exceptions import RemarksDecodeError


class Remarks(_Component):

    def __init__(self, raw):
        if raw.startswith("RMK "):
            self.text = raw
        else:
            raise RemarksDecodeError("Remarks(%s) could not be parsed" % raw)

    @property
    def raw(self):
        return self.text
