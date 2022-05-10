import sys
import argparse

from src.draw.draw_result import draw_result

from src.game.game_controller import GameController
from src.detection.detection_controller import DetectionController
from src.directory.create_directory import FileManager
from src.minizinc.minizinc_controller import MinizincController


AMOUNT_OF_WORLDS = 4
AMOUNT_OF_LEVELS_WORLD1 = 33
AMOUNT_OF_LEVELS_WORLD2 = 50
AMOUNT_OF_LEVELS_WORLD3 = 50
AMOUNT_OF_LEVELS_WORLD4 = 100

LEVELS_PER_WORLD = [AMOUNT_OF_LEVELS_WORLD1, AMOUNT_OF_LEVELS_WORLD2, AMOUNT_OF_LEVELS_WORLD3, AMOUNT_OF_LEVELS_WORLD4]

def standard_game():
    base_dir = "activegame"
  
    game_controller = GameController()

    for world in range(AMOUNT_OF_WORLDS):
        AMOUNT_OF_LEVELS = LEVELS_PER_WORLD[world]
        world_index = world + 1

        world_dir = "{}/world{}".format(base_dir, world_index)

        file_manager = FileManager(world_dir)
        file_manager.create_world_directory(world_dir)
        level_directories = file_manager.create_level_directories(0, AMOUNT_OF_LEVELS)
    
        for index, level_directory in enumerate(level_directories): 
            level_index = index + 1

            print("Calculating World {} Level {}!".format(world_index, level_index))
            
            screenshot_dir = "{}/Level{}.png".format(level_directory, level_index)
            # level_directory = "activegame/Level11"
            # screenshot_dir = "activegame/Level11/Level11.png"
            game_controller.take_screenshot(screenshot_dir)

            detection_controller = DetectionController(world_index)
            node_list = detection_controller.detect_nodes(screenshot_dir, level_directory)
            line_list = detection_controller.detect_lines(screenshot_dir, level_directory, node_list)

            connection_list = detection_controller.detect_connections(level_directory, node_list, line_list)
            connection_list.find_unique_connections()

            connection_list.calculate_constraints()

            minizinc_controller = MinizincController()
            minizinc_controller.execute_minizinc(node_list)

            draw_result(connection_list, screenshot_dir, level_directory)

            game_controller.play(node_list)
            
            if level_index < AMOUNT_OF_LEVELS:
                game_controller.click_next_level_button()
            else: 
                # Jump to next world!
                next_world_url = "https://thedollargame.io/game/level/100/{}00/1".format(world_index + 1)
                game_controller.get_url(next_world_url)

            game_controller.retrieve_local_storage()






def start_at_specific_level(world_number, level_number):

    base_dir = "activegame"

    level_url = "https://thedollargame.io/game/level/100/{}00/{}".format(world_number, level_number)

    game_controller = GameController()
    game_controller.write_to_local_storage()
    game_controller.get_url(level_url)

    for world in range(world_number - 1, AMOUNT_OF_WORLDS):
        AMOUNT_OF_LEVELS = LEVELS_PER_WORLD[world]
        world_index = world + 1

        world_dir = "{}/world{}".format(base_dir, world_index)

        file_manager = FileManager(world_dir)
        file_manager.create_world_directory(world_dir)

        detection_controller = DetectionController(world)
        
        if world_index > world_number:
            level_number = 1

        level_directories = file_manager.create_level_directories(0, AMOUNT_OF_LEVELS)
        
        for index in range(level_number - 1, AMOUNT_OF_LEVELS): 
            level_index = index + 1
            level_directory = level_directories[index]

            print("Calculating World {} Level {}!".format(world_index, level_index))
            
            screenshot_dir = "{}/Level{}.png".format(level_directory, level_index)
            game_controller.take_screenshot(screenshot_dir)

            node_list = detection_controller.detect_nodes(screenshot_dir, level_directory)
            line_list = detection_controller.detect_lines(screenshot_dir, level_directory, node_list)

            connection_list = detection_controller.detect_connections(level_directory, node_list, line_list)
            connection_list.find_unique_connections()

            connection_list.calculate_constraints()

            minizinc_controller = MinizincController()
            minizinc_controller.execute_minizinc(node_list)

            draw_result(connection_list, screenshot_dir, level_directory)

            game_controller.play(node_list)
            
            if level_index < AMOUNT_OF_LEVELS:
                game_controller.click_next_level_button()
            else: 
                # Jump to next world!
                next_world_url = "https://thedollargame.io/game/level/100/{}00/1".format(world_index + 1)
                game_controller.get_url(next_world_url)

            game_controller.retrieve_local_storage()





def check_single_level(world_number, level_number):
    base_dir = "activegame/world{}".format(world_number)
    level_name = "Level{}".format(level_number)
    screenshot_dir = "{}/{}/{}.png".format(base_dir, level_name, level_name)
    level_directory = "{}/{}".format(base_dir, level_name)
    

    detection_controller = DetectionController(world_number - 1)
    node_list = detection_controller.detect_nodes(screenshot_dir, level_directory)
    line_list = detection_controller.detect_lines(screenshot_dir, level_directory, node_list)

    connection_list = detection_controller.detect_connections(level_directory, node_list, line_list)
    connection_list.find_unique_connections()

    connection_list.calculate_constraints()

    minizinc_controller = MinizincController()
    minizinc_controller.execute_minizinc(node_list)

    draw_result(connection_list, screenshot_dir, level_directory)



    connection_list.calculate_constraints()

    minizinc_controller = MinizincController()
    minizinc_controller.execute_minizinc(node_list)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-mode', type=str, help='Standard, Start from specific level, Calculate single level')
    parser.add_argument('--world', type=int, help='World Index')
    parser.add_argument('--level', type=int, help='Level Index')

    args = parser.parse_args()

    mode = args.mode

    if mode != None: 
        if mode == "standard":
            standard_game()
        else:
            world_index = args.world
            level_index = args.level

            if world_index == None or level_index == None:
                print("Please provide a level and world index")
            else:
                if mode == "start_at_level":
                    start_at_specific_level(world_index, level_index)
                elif mode == "calculate_level":
                    check_single_level(world_index, level_index)
    else:
        print("Please provide a mode argument: standard, start_at_specific_level, calculate_specific_level")


