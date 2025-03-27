import pytest
from unittest.mock import patch
from main import (
    get_prize,
    verify_picks,
    generate_lottery_five,
    generate_mega_ball,
    get_user_selection
)

def test_verify_picks():
    lottery_numbers = {1, 2, 3, 4, 5}
    user_picks = {1, 2, 3, 6, 7}
    result = verify_picks(lottery_numbers, user_picks)
    assert result == {1, 2, 3}

def test_generate_lottery_five():
    result = generate_lottery_five()
    assert len(result) == 5
    assert all(1 <= num <= 70 for num in result)

def test_generate_mega_ball():
    result = generate_mega_ball()
    assert 1 <= result <= 25

@pytest.mark.parametrize("matched,power_ball,expected_prize", [
    (5, True, 310000000),  # Jackpot
    (5, False, 1000000),   # Second prize
    (4, True, 10000),      # Third prize
    (4, False, 500),       # Fourth prize
    (3, True, 200),        # Fifth prize
    (3, False, 10),        # Sixth prize
    (2, True, 10),         # Seventh prize
    (1, True, 4),         # Eighth prize
    (0, True, 2),         # Ninth prize
])
def test_get_prize(matched, power_ball, expected_prize):
    message, prize = get_prize(matched, power_ball)
    assert prize == expected_prize

@patch('builtins.input')
def test_get_user_selection_valid_input(mock_input):
    mock_input.return_value = "1,2,3,4,5,10"
    five_picks, mega_ball = get_user_selection()
    assert five_picks == {1,2,3,4,5}
    assert mega_ball == 10

@patch('builtins.input')
def test_get_user_selection_invalid_input(mock_input):
    mock_input.side_effect = ["1,2,3", "1,2,3,4,5,80", "1,2,3,4,5,10"]
    five_picks, mega_ball = get_user_selection()
    assert five_picks == {1,2,3,4,5}
    assert mega_ball == 10
