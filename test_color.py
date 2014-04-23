import unittest

import color  

class test_color(unittest.TestCase):

    def test_ConvertColorDepth_CorrectInput(self):

        whiteRgb16Bit = (65535)
        expectedWhite8Bit = (255)
        
        resultWhite8Bit = color.convertColorDepth(whiteRgb16bit)
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
