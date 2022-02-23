import unittest
import typewise_alert


class TypewiseTest(unittest.TestCase):
  def test_infers_breach_as_per_limits(self):
    self.assertTrue(typewise_alert.infer_breach(20, 50, 100) == 'TOO_LOW')
    self.assertTrue(typewise_alert.infer_breach(60, 50, 100) == 'NORMAL')
    self.assertTrue(typewise_alert.infer_breach(110, 50, 100) == 'TOO_HIGH')
    self.assertTrue(typewise_alert.classify_temperature_breach('PASSIVE_COOLING', 100) == 'TOO_HIGH')
    self.assertTrue(typewise_alert.check_and_alert('TO_CONTROLLER',{'coolingType': 'PASSIVE_COOLING'}, 100) == 1)
    self.assertTrue(typewise_alert.check_and_alert('TO_EMAIL',{'coolingType': 'PASSIVE_COOLING'}, 100) == 1)


if __name__ == '__main__':
  unittest.main()
