import unittest
from unittest.mock import MagicMock, patch
from package.engine.engine import Engine
from package.protagonist.protagonist import Protagonist

class TestEngine(unittest.TestCase):

    @patch('package.engine.engine.pygame.time.Clock')
    @patch('package.engine.engine.Protagonist')
    def test_start(self, mock_protagonist_class, mock_clock_class):
        mock_protagonist_instance = MagicMock(spec=Protagonist)
        mock_clock_instance = MagicMock()
        mock_protagonist_class.return_value = mock_protagonist_instance
        mock_clock_class.return_value = mock_clock_instance

        Engine.start()

        mock_protagonist_class.assert_called_once_with(20, 200, 200)

        mock_clock_class.assert_called_once()

        self.assertEqual(Engine._protagonist, mock_protagonist_instance)
        self.assertEqual(Engine._clock, mock_clock_instance)

    @patch('package.engine.engine.Protagonist')
    def test_move_protagonist(self, mock_protagonist_class):
        mock_protagonist_instance = MagicMock(spec=Protagonist)
        mock_protagonist_instance.x = 100
        mock_protagonist_instance.y = 150
        Engine._protagonist = mock_protagonist_instance

        Engine.move_protagonist(10, -20)

        expected_new_x = 100 + 10
        expected_new_y = 150 + (-20)

        mock_protagonist_instance.set_pos.assert_called_once_with(expected_new_x, expected_new_y)

    def test_get_protagonist(self):

        mock_protagonist_instance = MagicMock(spec=Protagonist)
        Engine._protagonist = mock_protagonist_instance

        result = Engine.get_protagonist()

        self.assertEqual(result, mock_protagonist_instance)

if __name__ == '__main__':
    unittest.main()
