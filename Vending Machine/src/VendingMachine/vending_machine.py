class VendingMachine:

  coin_return_slot = []

  def consume_coin(self, coin):
    result = ""
    if coin.size == 1 and coin.weight == 1:
      result = "Reject"
      self.coin_return_slot.append(coin)
    else:
      result = "Accept"
    return result


  def get_contents_of_coin_return_slot(self):
    return self.coin_return_slot
