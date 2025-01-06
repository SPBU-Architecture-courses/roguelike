import unittest
from unittest.mock import MagicMock, patch
import pygame
from package.engine.gui.gameWindow import GameWindow

class TestGameWindow(unittest.TestCase):    
    @patch('pygame.quit')
    @patch('pygame.time.Clock')
    @patch('pygame.key.get_pressed')
    @patch('pygame.event.get')
    def test_run(self, mock_event_get, mock_get_pressed, mock_clock, mock_pygame_quit):
        game_window = GameWindow()

        def side_effect():
            game_window.running = False
            return []

        mock_event_get.side_effect = side_effect

        with patch.object(game_window, 'render') as mock_render, patch.object(game_window, 'handle_keydowns') as mock_handle_keydowns:

            game_window.run()

            mock_get_pressed.assert_called_once()
            mock_handle_keydowns.assert_called_once()

            mock_render.assert_called_once()

            mock_pygame_quit.assert_called_once()

if __name__ == '__main__':
    unittest.main()
