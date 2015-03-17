import pickle

class game_record():
    def __init__(self):
        self.name = None
        self.platform = None
        self.genre = None
        self.cost = None
        self.player_count = None
        self.online = None
games = game_record()
game_list = []


def load_games(filename):  #gamefile                     
    with open(filename, mode = "rb") as file:
        game_list = pickle.load(file)
        return game_list

def save_games(filename, game_list): #gamefile
    with open(filename, mode = "wb") as file:
        pickle.dump(game_list,file)
        
              

#the parameter is games because eventually you will be displaying
#multiple games using this function

def display_games(game_list):
    name = "Name"
    platform = "Platform"
    genre = "Genre"
    cost = "Cost"
    players = "Players"
    online = "Online"
    print("-" * 79)
    print("| {0:^10} | {1:^10} | {2:^10} | {3:^10} | {4:^10} | {5:^10} |".format(name, platform, genre, cost, players, online))
    print("-" * 79)
    for game in game_list:
        print("| {0:^10} | {1:^10} | {2:^10} | {3:^10} | {4:^10} | {5:^10} |".format(game.name, game.platform, game.genre, game.cost, game.player_count, game.online))
        print("-" * 79)


def get_game_from_user(games, game_list):
       
    rouge = 0
    while rouge != -1:
        games = game_record()
        games.name = input("Please enter the name of the game: ")
        games.platform = input("Please enter the platform the game can be played on: ")
        games.genre = input("Please enter the genre of the game: ")
        games.cost = input("Please enter how much the game costs: ")
        games.player_count = input("Please enter the total number of offline players allowed: ")                
        games.online = input("Does the game have online functionality? ")
        game_list.append(games)
        rouge = int(input("Enter -1 to terminate, anything else will continue: "))
    return game_list



    
    

def display_menu():
    print()
    print("***Welcome to the Computer and Video Game Database***")
    print()
    print("1. Add new games")
    print("2. Display games")
    print("3. Exit program")
    print()
    

def main():
    game_list = []
    user_file = input("Please enter the file name: ")
    game_list = load_games(user_file)
    exit_program = False
    while not exit_program:
        display_menu()
        selected_option = int(input("Please select a menu option: "))
        if selected_option == 1:
            game_list = get_game_from_user(games, game_list)
        elif selected_option == 2:
            display_games(game_list)
        elif selected_option == 3:
            save_games(user_file, game_list)  
            exit_program = True
            
        else:
            print("Please enter a valid option (1-3)")
            print()

if __name__ == "__main__":
    main()
