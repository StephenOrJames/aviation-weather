import unittest
from aviation_weather.report import Report


class TestReport(unittest.TestCase):
    """Unit tests for the Report parser"""

    def _test_parse(self, raw):
        self.assertEqual(raw, str(Report(raw)))

    def test_parse_KJFK(self):
        self._test_parse("KJFK 182151Z 28022G34KT 10SM SCT065 M04/M17 A2990 RMK AO2 "
                         "PK WND 30034/2145 SLP123 VIRGA OHD AND E-SE T10391167")

    def test_parse_MKJP(self):
        self._test_parse("MKJP 182300Z 14014KT 9999 SCT022 28/22 Q1015")

    def test_parse_LBBG(self):
        self._test_parse("METAR LBBG 041600Z 12003MPS 290V310 1400 R04/P1500N R22/P1500U "
                         "+SN BKN022 OVC050 M04/M07 Q1020 NOSIG 8849//91=")

    def test_parse_KTTN(self):
        self._test_parse("METAR KTTN 051853Z 04011KT 1/2SM VCTS SN FZFG BKN003 OVC010 "
                         "M02/M02 A3006 RMK AO2 TSB40 SLP176 P0002 T10171017=")

    def test_parse_KSLC(self):
        self._test_parse("KSLC 192353Z 30004KT 10SM CLR 29/02 A3000 RMK AO2 SLP110 T02940017 10306 20261 56014")

    def test_parse_KAZO(self):
        self._test_parse("KAZO 270257Z 26013KT 1 3/4SM R35/4500VP6000FT -SN BKN016 "
                         "OVC022 M02/M06 A3009 RMK AO2 P0000 T10221056")

    def test_parse_TJSJ(self):
        self._test_parse("SPECI TJSJ 270256Z 12003KT 10SM FEW020 SCT036 BKN095 24/22 A3013 "
                         "RMK AO2 RAB06E37 SLP203 SHRA DSNT W P0024 60026 T02440222 50005")

    def test_parse_EIDW(self):
        self._test_parse("EIDW 092307Z 24035G55KT 210V270 1700 +SHRA BKN007 OVC015CB 08/07")

    def test_retrieve(self):
        self.assertIsInstance(Report.retrieve("KJFK"), Report)


if __name__ == "__main__":
    unittest.main()
