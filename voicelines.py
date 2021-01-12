class voicelines:
  
  @classmethod
  def greeting(cls):
    print("Welcome to Digital Blackjack! For this game you'll \n just play against the dealer with one player. Try and get \n as close to 21 without going over, 2 through 10 are all \n their numbered values. Jacks, Queens, and Kings all equal \n 10, and the Ace card can either equal 1, or 11 depending on what you chose.")

  @classmethod
  def hit_or_stay(cls):
    hit_or_stay = "Player, do you wish to draw \n another card, or keep the \n cards you have? (hit/pass) "
    return hit_or_stay

  @classmethod
  def one_or_eleven(cls):
    one_or_eleven = "Player, you drew an Ace! Would \n you like it to count as a 1, or an 11? (1/11) "
    return one_or_eleven

  @classmethod
  def went_bust(cls):
    print("Sorry player, you went over 21, in other \n words you went bust.")

  @classmethod
  def you_won(cls):
    print("Congratulations player! You beat the dealer!")

  @classmethod
  def you_lost(cls):
    print("Sorry player, the dealer won this time.")

  @classmethod
  def you_tied(cls):
    print("Looks like you and the dealer tied this time.")