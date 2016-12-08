"""Test mailroom module for managing donation history list, emails."""

import pytest


def test_choose_path(capfd):
    """Ensure basic options presented, input read."""
    from mailroom import choose_path
    choose_path()
    out, err = capfd.readouterr()
    assert out == 'If you want to submit a thank you, enter "Send a Thank You".  If you would like to see a donation report, enter "Create a Report". If at any time you wish to return to this menu, enter "menu".  Otherwise, enter "Quit" to quit.'
