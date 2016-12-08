"""Test mailroom module for managing donation history list, emails."""

FIRST_OPTIONS_TABLE = [
    ['CREATE a REPORT'],
    ['Sedn a tahnk you'],
    ['Send a Thank You'],
    ['exit'],
]

import pytest


def test_choose_path_stout(capfd):
    """Ensure basic options presented."""
    from mailroom import choose_path
    choose_path()
    out, err = capfd.readouterr()
    assert out == 'If you want to submit a thank you, enter "Send a Thank You".  If you would like to see a donation report, enter "Create a Report". If at any time you wish to return to this menu, enter "menu".  Otherwise, enter "Quit" to quit.'


def test_choose_path_options(monkeypatch, 'input', FIRST_OPTIONS_TABLE):
    """Ensure user's options accepted."""
    monkeypatch.setitem(__builtins__, 'input', FIRST_OPTIONS_TABLE):
    from mailroom import choose_path
    choose_path()
    assert input == create_a_report()

# def test_send_thank_you():
#     """Ensure 