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
    input_prompt = 'If you want to submit a thank you, enter'
    input_prompt += ' "Send a Thank You".  If you would like to see a'
    input_prompt += ' donation report, enter "Create a Report".'
    input_prompt += ' If at any time you wish to return to this menu,'
    input_prompt += ' enter "menu".  Otherwise, enter "Quit" to quit: '
    valid = True
    while valid:
        choice = input(input_prompt)
        if choice.lower() == 'create a report':
            create_a_report()
        elif choice.lower() == 'send a thank you':
            get_donation_info()
        elif choice.lower() == 'quit':
            exit()
        else:
            print ('\n Please submit a valid input. \n')
            choose_path()

choice = ""
donation = ""


def get_donation_info():
    """Create variables to pass to send_thank_you()."""
    global choice
    global donation
    input_prompt = 'If you want to see a list of donors, enter "list".'
    input_prompt += '  Otherwise, enter a donor name: '
    choice = input(input_prompt)
    if choice.lower() == 'list':
        for donor in sorted(list(donors.keys())):
            donor = donor.split(' ')
            # The line below breaks prints capitalized first/last names
            print (' '.join(list(map(lambda x: x.capitalize(), donor))))
    else:
        print("Enter donation amount: ")
        donation = int(input("> "))
        # while not donation.isnumeric():
        #     input_prompt = 'Please enter a valid number: '
        #     donation = input(input_prompt)

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
        print ('{choice} has already donated. Adding new donation.')
        donors[choice].append(float(donation))
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

if __name__ == '__main__':
    choose_path()
