"""Mailroom Implementation.  Create thank you cards or donation reports."""
from __future__ import unicode_literals
import math

donors = {'jordan schatzman': [100, 200, 400, 50.6],
          'rick valenzuela': [500, 300, 100, 50, 1.24],
          'sally johnson': [50, 100, 1, 2, 99],
          'jane': [39, 23, 532, 2432],
          'bob': [89, 23, 12, 3.45643]}


def choose_path():
    """Allow the user to begin the program."""
    print('If you want to submit a thank you, enter:')
    print('[T] to send a [T]hank you')
    print('[R] to show a donation [R]eport')
    print('If at any time you wish to return to this menu,')
    print('enter "menu".  Otherwise, enter "Quit" to quit')
    input_prompt = "> "
    valid = True
    while valid:
        choice = input(input_prompt)
        if choice.lower() == 'r':
            create_a_report()
        elif choice.lower() == 't':
            get_donor()
        elif choice.lower() == 'quit':
            exit()
        else:
            print ('\n Please submit a valid input. \n')
            choose_path()

choice = ""
donation = ""


def get_donor():
    """Create donor to pass to send_thank_you()."""
    global choice
    input_prompt = 'If you want to see a list of donors, enter "list".'
    input_prompt += '  Otherwise, enter a donor name: '
    choice = input(input_prompt)
    if choice.lower() == 'menu':
        choose_path()
    elif choice.lower() == 'quit':
        exit()
    elif choice.lower() == 'list':
        for donor in sorted(list(donors.keys())):
            donor = donor.split(' ')
            # The line below breaks prints capitalized first/last names
            print (' '.join(list(map(lambda x: x.capitalize(), donor))))
        get_donor()
    get_donation_amt()


def get_donation_amt():
    """Create donation amount variable."""
    global donation
    print("Enter donation amount: ")
    donation = input("> ")
    while not isinstance(donation, int) or not isinstance(donation, float):
        input_prompt = 'Please enter a valid number: '
        donation = input(input_prompt)

    print(donors)
    add_donation()
    print(donors)


def send_thank_you():
    """Create a report with full donor list with name and donation stats."""
    donation = add_donation(choice.lower())
    print_email(choice, donation)


def add_donation():
    """Add donation for existing donor."""
    if choice.lower() in donors:
        print("{} has already donated. Adding new donation.".format(choice))
        donors[str(choice)].append(float(donation))
        print_email(choice, donation)
    else:
        print ('Adding {choice} and donation amount to the donors list.')
        donors[choice.lower()] = [donation]
        print_email(choice, donation)


def print_email(donor, donation):
    """Print email to console."""
    email = "Dear {0},"
    email += '\n \n \n'
    email += 'Thanks so much for your donation of ${1}.  We love you!'
    email += ' Please feel free to donate again.'
    email += '\n \n \n'
    email += 'Love, \n CodeFellows'
    print (email.format(donor, donation))


def create_a_report():
    """Print donation report, with total, count, average."""
    print ('Donor Name--------------Count-----Average--------Sum')
    print ('-' * 62)
    donor_ordered = [[k, sum(v)] for k, v in donors.items()]
    donor_ordered.sort(key=lambda x: -x[1])
    for donor in donor_ordered:
        donations = donors[donor[0]]
        donation_count = str(len(donations))
        donation_sum = str(round(sum(donations), 2))
        donation_avg = str(round(float(sum(donations)) / len(donations), 2))
        name = donor[0].split(' ')
        name = ' '.join(list(map(lambda x: x.capitalize(), name)))

        print ('{0}{1}{2}{3}{4}{5}{6}{7}'.format(' ' * 3,
                                                 name,
                                                 ' ' * (23 - len(name)),
                                                 str(len(donations)),
                                                 ' ' * (10 - len(donation_count)),
                                                 donation_avg,
                                                 ' ' * (13 - len(donation_avg)),
                                                 donation_sum))
    choose_path()

if __name__ == '__main__':
    choose_path()
