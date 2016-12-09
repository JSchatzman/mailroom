"""Test mailroom module for managing donation history list, emails."""

import pytest


def test_choose_path_stout(capfd):
    """Ensure basic options presented."""
    from mailroom import choose_path
    choose_path()
    out, err = capfd.readouterr()
    assert out == 'If you want to submit a thank you, enter "Send a Thank You".  If you would like to see a donation report, enter "Create a Report". If at any time you wish to return to this menu, enter "menu".  Otherwise, enter "Quit" to quit.'


def test_send_thank_you(capfd):
     """Barf."""
    from mailroom import send_thank_you
    send_thank_you()
    out, err = capfd.readouterr()
    assert out == 'If you want to see a list of donors, enter "list".'


def test_add_donor(capfd):
    """Ensure a new donation can be added to a donor's history."""
    from mailroom import add_donation
    add_donation('bob')
    out, err = capfd.readouterr()
    assert out == 'How much is the new donation worth?'

