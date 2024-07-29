from machine import Machine
from player import Player

def main():
    player1 = Player("1", "Carter Sperry")
    Player.get_player_info(player1)
    machine1 = Machine("hi", "hi")
    machine1.display_slot_machine()

if __name__ == "__main__":
    main()