import sys

from src.draw.draw_result import draw_result

from src.game.game_controller import GameController
from src.detection.detection_controller import DetectionController
from src.directory.create_directory import FileManager
from src.minizinc.minizinc_controller import MinizincController



def main():
    base_dir = "activegame"
    
    AMOUNT_OF_WORLDS = 2
    AMOUNT_OF_LEVELS_WORLD1 = 33
    AMOUNT_OF_LEVELS_WORLD2 = 50

    LEVELS_PER_WORLD = [AMOUNT_OF_LEVELS_WORLD1, AMOUNT_OF_LEVELS_WORLD2]
  
    game_controller = GameController()

    for world in range(AMOUNT_OF_WORLDS):
        AMOUNT_OF_LEVELS = LEVELS_PER_WORLD[world]
        world_index = world + 1

        world_dir = "{}/world{}".format(base_dir, world_index)

        file_manager = FileManager(world_dir)
        file_manager.create_world_directory(world_dir)
        level_directories = file_manager.create_level_directories(AMOUNT_OF_LEVELS)
    
        for index, level_directory in enumerate(level_directories): 
            level_index = index + 1

            print("Calculating World {} Level {}!".format(world_index, level_index))
            
            screenshot_dir = "{}/Level{}.png".format(level_directory, level_index)
            # level_directory = "activegame/Level11"
            # screenshot_dir = "activegame/Level11/Level11.png"
            game_controller.take_screenshot(screenshot_dir)

            detection_controller = DetectionController()
            node_list = detection_controller.detect_nodes(screenshot_dir, level_directory)
            line_list = detection_controller.detect_lines(screenshot_dir, level_directory, node_list)

            connection_list = detection_controller.detect_connections(level_directory, node_list, line_list)
            connection_list.find_unique_connections()

            draw_result(connection_list, screenshot_dir, level_directory)

            connection_list.calculate_constraints()

            minizinc_controller = MinizincController()
            minizinc_controller.execute_minizinc(node_list)

            game_controller.play(node_list)
            
            if level_index < AMOUNT_OF_LEVELS:
                game_controller.click_next_level_button()
            else: 
                # Jump to next world!
                next_world_url = "https://thedollargame.io/game/level/100/{}00/1".format(world_index + 1)
                game_controller.go_to_next_world(next_world_url)


def check_single_level(world_number, level_number):
    base_dir = "activegame/world{}".format(world_number)
    level_name = "Level{}".format(level_number)
    screenshot_dir = "{}/{}/{}.png".format(base_dir, level_name, level_name)
    level_directory = "{}/{}".format(base_dir, level_name)
    

    detection_controller = DetectionController()
    node_list = detection_controller.detect_nodes(screenshot_dir, level_directory)
    line_list = detection_controller.detect_lines(screenshot_dir, level_directory, node_list)

    connection_list = detection_controller.detect_connections(level_directory, node_list, line_list)
    connection_list.find_unique_connections()

    draw_result(connection_list, screenshot_dir, level_directory)

    connection_list.calculate_constraints()

    minizinc_controller = MinizincController()
    minizinc_controller.execute_minizinc(node_list)

if __name__ == '__main__':
    if len(sys.argv) > 2:
        world_number = int(sys.argv[1])
        level_number = int(sys.argv[2])
        check_single_level(world_number, level_number)
    else:
        main()

