# Jesse Butcher
# CIS256 Fall 2026
# Programming Assignment 4


import pytest
import guess_the_word

def test_winning_game(monkeypatch):
    #tests for a winning game
    monkeypatch.setattr("random.choice", lambda x: "cat")

# simulates inputting letters for game
    input = iter(["c", "a", "t"])
    monkeypatch.setattr("builtins.input", lambda _: next(input))

    result = guess_the_word.play()
    assert result == "win"


def test_losing_game(monkeypatch):
#tests for a loss at the game
    monkeypatch.setattr("random.choice", lambda x: "pig")
#simulates using all available guesses
    input = iter(["a","b", "c", "d", "e"])
    monkeypatch.setattr("builtins.input", lambda _: next(input))

    result = guess_the_word.play()
    assert result == "loss"

def test_input_validation(monkeypatch):

    monkeypatch.setattr("random.choice", lambda x: "cow")

#provides invalid inputs like numbers, strings, duplicates and correct inputs in code
    input = iter(["1", "jab", "c", "c", "o", "w"])
    monkeypatch.setattr("builtins.input", lambda _: next(input))

    result = guess_the_word.play()
    assert result == "win"

