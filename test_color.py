import unittest

import mousetrap.app.ui.color

class test_color(unittest.TestCase):

    # test_<unit-of-work>_<state-under-test>_<expected-behavior>
    # test_convertColorDepth_passedTypicalRgbValues_returnTypicalHsvValue:
    # test_convertColorDepth_badRgbValuesPassed_throwsException:
    def test_convertColorDepth_ErrorIfNotInColorRange(self, color):

        # SETUP

        blackRgb = (0, 0, 0)
        expectedBlackHsv = (255, 255, 0)

        # EXECUTE

        resultBlackHsv = color.convertColorDepth(blackRgb)

        # ASSESS

        self.assertTrue(0 <= resultBlackHsv[0] <= 255)
        self.assertTrue(0 <= resultBlackHsv[1] <= 255)
        self.assertTrue(0 == resultBlackHsv[2])

        self.assertTrue(
            resultBlackHsv == expectedBlackHsv,
            msg="Error: result black hsv "
                + str(resultBlackHsv)
                + " does not match expectation "
                + str(expectedBlackHsv)
        )

        # self.assertTrue(0 <= color <= 255, msg="Error: color is out of the range! (0 - 255)")
    

if __name__ == '__main__':
    unittest.main()
