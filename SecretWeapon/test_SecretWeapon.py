import unittest
from unittest.mock import patch
from SecretWeapon import Game

class TestGame(unittest.TestCase):
    def test_play_wins_game(self):
        # Arrange
        game = Game(10)
        game.secret_x = 5
        game.secret_y = 5

        with patch('builtins.input', side_effect=['5', '5']):
            # Act
            game.play()

            # Assert
            self.assertTrue(game.won)

    def test_play_loses_game(self):
        # Arrange
        game = Game(4)
        game.secret_x = 1
        game.secret_y = 1

        with patch('builtins.input', side_effect=['2', '2', '3', '3', '4', '4', '2', '1', '1', '2', '2', '3', '1', '3', '3', '1','4', '1']):
            # Act
            game.play()

            # Assert
            self.assertFalse(game.won)

    def test_get_distance_returns_correct_distance(self):
        # Arrange
        game = Game(5)
        game.secret_x = 2
        game.secret_y = 3

        # Act
        distance = game.get_distance(5, 7)

        # Assert
        self.assertEqual(distance, 5)

if __name__ == '__main__':
    unittest.main()
