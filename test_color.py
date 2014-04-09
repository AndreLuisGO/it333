import unittest

import mousetrap.app.ui.color

class test_color(unittest.TestCase):

    # test_<unit-of-work>_<state-under-test>_<expected-behavior>
    # This tests if the 16-bit color depth is correctly being converted to 8-bit color depth
    def test_convertColorDepth_ErrorIfNotInColorRange(self, color):

        # SETUP

        whiteRgb16Bit = (65535,65536, 65535)
        expectedWhite8Bit = (255, 255, 255)

        # EXECUTE

        resultWhite8Bit = color.convertColorDepth(whiteRgb16bit)

        # ASSESS

        self.assertTrue(0 <=  expectedWhite8Bit[0] <= 255)
        self.assertTrue(0 <=  expectedWhite8Bit[1] <= 255)
        self.assertTrue(0 <=  expectedWhite8Bit[2] <= 255)

        self.assertTrue(
            resultWhite8Bit == expectedWhite8Bit,
            msg="Error: result white 8bit "
                + str(resultWhite8Bit)
                + " does not match expectation "
                + str(expectedWhite8Bit)
        )


if __name__ == '__main__':
    unittest.main()
