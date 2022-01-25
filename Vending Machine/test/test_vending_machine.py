import unittest
from unittest.mock import patch

from src.VendingMachine.vending_machine import VendingMachine

class TestVendingMachine(unittest.TestCase):

    @patch("src.Coin.coin.Coin")
    def test_should_reject_invalid_coins(self, mocked_coin):
        penny = mocked_coin()
        penny.size = 1
        penny.weight = 1
        
        failure_message = "Pennies should have been rejected"
        self.assertEqual("Reject", VendingMachine().consume_coin(penny), failure_message)


    @patch("src.Coin.coin.Coin")
    def test_should_accept_valid_coins(self, mocked_coin):
        quarter = mocked_coin()
        quarter.size = 3
        quarter.weight = 3

        dime = mocked_coin()
        dime.size = .5
        dime.weight = .5

        nickle = mocked_coin()
        nickle.size = 1
        nickle.weight = .5

        msg = "Quarter should have been accepted"
        self.assertEqual("Accept", VendingMachine().consume_coin(quarter), msg)
        msg = "Dime should have been accepted"
        self.assertEqual("Accept", VendingMachine().consume_coin(dime), msg)
        msg = "Nickle should have been accepted"
        self.assertEqual("Accept", VendingMachine().consume_coin(nickle), msg)


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
