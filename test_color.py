import unittest
import color

class _convertColorDepth(unittest.TestCase):

    def test_CorrectInput_GoodOutput(self):

        whiteRgb16Bit = 65535
        expectedWhite8Bit = 255

        resultWhite8Bit = color.convertColorDepth(self,whiteRgb16Bit)

        self.assertTrue(0 <= resultWhite8Bit <= 255)
        self.assertTrue(
            resultWhite8Bit == expectedWhite8Bit,
            msg="Error: result white 8bit "
                + str(resultWhite8Bit)
                + " does not match expectation "
                + str(expectedWhite8Bit)
        )


if __name__ == '__main__':
    unittest.main()
