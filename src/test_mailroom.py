"""Test mailroom module for managing donation history list, emails."""

import pytest


def test_create_sorted_list():
    """Test the create_sorted_list function."""
    from mailroom import create_sorted_list
    donors = {'jordan schatzman': [100, 200, 400, 50.6],
              'rick valenzuela': [500, 300, 100, 50, 1.24],
              'sally johnson': [50, 100, 1, 2, 99],
              'jane': [39, 23, 532, 2432],
              'bob': [89, 23, 12, 3.45643],
              'XXXX TEXT': [0]}

    test_list = create_sorted_list(donors)
    assert test_list[0] == 'Bob'
    assert test_list[1] == 'Jane'
    assert test_list[2] == 'Jordan Schatzman'
    assert test_list[3] == 'Rick Valenzuela'
    assert test_list[4] == 'Sally Johnson'
    assert test_list[5] == 'Xxxx Text'


def test_add_donation():
    """Test the add_donation funtion."""
    from mailroom import add_donation
    donors = {'jordan schatzman': [],
              'rick valenzuela': [500, 300, 100, 50, 1.24],
              'sally johnson': [50, 100, 1, 2, 99],
              'jane': [39, 23, 532, 2432],
              'bob': [89, 23, 12, 3.45643],
              'XXXX TEXT': [1]}
    first_test = add_donation(donors, 'jordan schatzman', .111)
    second_test = add_donation(donors, 'XXXX TEXT', 500)
    assert first_test == .111
    assert donors['jordan schatzman'] == [.111]
    assert second_test == 500
    assert donors['XXXX TEXT'] == [1, 500]


def test_print_email():
    """Test the print_email function."""
    from mailroom import print_email
    donors = {'jordan schatzman': [],
              'rick valenzuela': [500, 300, 100, 50, 1.24],
              'sally johnson': [50, 100, 1, 2, 99],
              'jane': [39, 23, 532, 2432],
              'bob': [89, 23, 12, 3.45643],
              'XXXX TEXT': [1]}
    email_test1 = "Dear Jane,\n \n \n"
    email_test1 += 'Thanks so much for your donation of $0.  We love you!'
    email_test1 += ' Please feel free to donate again.'
    email_test1 += 'Love, \n CodeFellows\n\n\n'
    assert print_email(donors, 'jane', 0) == email_test1
    email_test2 = "Dear Jane Doe The Third,\n \n \n"
    email_test2 += 'Thanks so much for your donation of $50.  We love you!'
    email_test2 += ' Please feel free to donate again.'
    email_test2 += 'Love, \n CodeFellows\n\n\n'
    assert print_email(donors, 'Jane Doe the third', 50) == email_test2


def test_create_a_report():
    """Test the create_a_report function."""
    from mailroom import create_a_report
    donors_test1 = {'jordan schatzman': [0],
                    'rick valenzuela': [500, 300, 100, 50, 1.24],
                    'sally johnson': [50, 100, 1, 2, 99],
                    'jane': [39, 23, 532, 2432],
                    'bob': [89, 23, 12, 3.45643]}
    test_report1 = 'Donor Name--------------Count-----Average--------Sum\n'
    test_report1 += ('-' * 62) + '\n'
    test_report1 += '   Jane                   4         756.50       3026.00\n'
    test_report1 += '   Rick Valenzuela        5         190.25       951.24\n'
    test_report1 += '   Sally Johnson          5         50.40        252.00\n'
    test_report1 += '   Bob                    4         31.86        127.46\n'
    test_report1 += '   Jordan Schatzman       1         0.00         0.00\n'
    assert create_a_report(donors_test1) == test_report1
    donors_test2 = {'jim bob smith': [1, 2, 3, 4, 5, 6, 7, 8, 9, 101020101]}
    test_report2 = 'Donor Name--------------Count-----Average--------Sum\n'
    test_report2 += ('-' * 62) + '\n'
    test_report2 += '   Jim Bob Smith          10        10102014.60  101020146.00\n'
    assert create_a_report(donors_test2) == test_report2
