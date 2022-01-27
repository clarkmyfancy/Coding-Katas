class VendingMachine:

  coin_return_slot = []
  virtual_wallet = []

  def __init__(self):
    self.coin_return_slot = []
    self.virtual_wallet = []

  def consume_coin(self, coin):
    result = ""
    if coin.size == 1 and coin.weight == 1:
      result = "Reject"
      self.coin_return_slot.append(coin)
    else:
      result = "Accept"
      self.virtual_wallet.append(coin)
    return result


  def get_contents_of_coin_return_slot(self):
    return self.coin_return_slot

  def get_contents_of_virtual_wallet(self):
    return self.virtual_wallet
