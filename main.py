from machine import Machine
from player import Player

def main():
    player = Player("1", "Carter Sperry")
    Player.get_player_info(player)

if __name__ == "__main__":
    main()