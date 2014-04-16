import unittest

#this brings "No module named mousetrap.app.ui.color"
import color  

class test_color(unittest.TestCase):

    # test_<unit-of-work>_<state-under-test>_<expected-behavior>
    # This tests if the 16-bit color depth is correctly being converted to 8-bit color depth
    def test_convertColorDepth_correctInput(self):

        # SETUP

        whiteRgb16Bit = (65535)

        expectedWhite8Bit = (255)


        # EXECUTE
        #when ignoring the module error (line 3), it brings " ' test.color' object has no attribute 'convertColorDepth'
        resultWhite8Bit = color.convertColorDepth(whiteRgb16bit)

        # ASSESS

        self.assertTrue(0 <=  expectedWhite8Bit <= 255)

        self.assertTrue(
            resultWhite8Bit == expectedWhite8Bit,
            msg="Error: result white 8bit "
                + str(resultWhite8Bit)
                + " does not match expectation "
                + str(expectedWhite8Bit)
        )


if __name__ == '__main__':
    unittest.main()
