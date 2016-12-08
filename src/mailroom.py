"""Mailroom Implementation.  Create thank you cards or donation reports."""
from __future__ import unicode_literals

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
    input_prompt += ' enter "menu".  Otherwise, enter "Quit" to quit.'
    choice = input(input_prompt)
    if choice.lower() == 'create a report':
        create_a_report()
    elif choice.lower() == 'send a thank you':
        send_thank_you
    elif choice.lower() == 'exit':
        exit()


def send_thank_you():
    """Create a report with full donor list with name and donation stats."""
    input_prompt = 'If you want to see a list of donors, enter "list".'
    input_prompt += 'Otherwise, enter a donor name.'
    choice = input(input_prompt)
    if choice.lower() == 'list':
        for donor in sorted(list(donors.keys())):
            donor = donor.split(' ')
            # The line below breaks prints capitalized first/last name
            print (' '.join(list(map(lambda x: x.capitalize(), donor))))
    elif choice.lower == 'menu':
        choose_path()
    else:
        if choice.lower() in donors:
            print ('{0} has already donated.  Enter new donation.'.format(choice))
            add_donation(choice.lower())
        else:
            print ('{0} has been added.  Enter new donation.'.format(choice))
            donors[choice.lower()] = []
            add_donation(choice.lower())

def add_donation(donor):
    """Add donation for existing donor,"""
    input_prompt = 'How much is the new donation worth?'
    donation = input(input_prompt)
    while not donation.isnumeric():
        input_prompt = 'Please enter a valid number'
        donation = input(input_prompt)
    donors[donor].append(donation)




def create_a_report():
    """Show donor list and allow for new donations to be entered."""
    """Finally, send thank you."""
    pass

send_thank_you()