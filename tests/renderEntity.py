import unittest
from unittest.mock import MagicMock, patch
from package.protagonist.protagonist import Protagonist
from package.engine.render.renderEntity import RenderEntity
import package.engine.constants as constants
import pygame

class TestRenderEntity(unittest.TestCase):
    @patch('pygame.draw.circle')
    def test_render(self, mock_draw_circle):
        mock_protagonist = MagicMock(spec=Protagonist)
        mock_protagonist.x = 100
        mock_protagonist.y = 150

        mock_surface = MagicMock()

        RenderEntity.render(mock_protagonist, mock_surface)

        expected_color = constants.PERSON_COLOR
        expected_position = (mock_protagonist.x, mock_protagonist.y)
        expected_radius = constants.PERSON_RADIUS

        mock_draw_circle.assert_called_once_with(
            mock_surface,
            expected_color,
            expected_position,
            expected_radius
        )

if __name__ == '__main__':
    unittest.main()
