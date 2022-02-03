import sys

from src.draw.draw_result import draw_result

from src.game_elements.node.node import Node
from src.game_elements.node.node_list import NodeList
from src.vc.vc_controller import VisualComputingController
from src.game.game_controller import GameController
from src.detection.detection_controller import DetectionController
from src.directory.create_directory import FileManager
from src.minizinc.minizinc_controller import MinizincController



def main():
    base_dir = "activegame"
    file_manager = FileManager(base_dir)
    
    AMOUNT_OF_LEVELS = 10

    level_directories = file_manager.create_directories_for_active_game(AMOUNT_OF_LEVELS)
    game_controller = GameController()
    # level_directories = [1]
    
    for index, level_directory in enumerate(level_directories): 
        level_index = index + 1

        print("Calculating for Level {}!".format(level_index))
        
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
        game_controller.click_next_level_button()

def check_single_level(level_number):
    base_dir = "activegame"
    level_name = "Level{}".format(level_number)
    screenshot_dir = "{}/{}/{}.png".format(base_dir, level_name, level_name)
    level_directory = "{}/{}".format(base_dir, level_name)
    # screenshot_dir = "activegame/Level11/Level11.png"

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
<<<<<<< HEAD
    #url = "https://thedollargame.io/game/level/100/100/2"
    #orig_url = take_screenshot(url) # take screenshot of game and return screenshot URL
    orig_url = "img/archive/Level2/screenshot.png"
    #orig_url = "test_img/test.png"
=======
    if len(sys.argv) > 1:
        level_number = int(sys.argv[1])
        check_single_level(level_number)
    else:
        main()
>>>>>>> da76719 (solves first 10 levels on fullscreen)

