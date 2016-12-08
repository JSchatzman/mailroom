"""Mailroom Implementation.  Create thank you cards or donation reports."""

donors = {'jordan': [100, 200, 400, 50.6],
          'rick': [500, 300, 100, 50, 1.24],
          'sally': [50, 100, 1, 2, 99],
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
            print (donor)
    elif choice.lower == 'menu':
        choose_path()
    else:
        pass 


def create_a_report():
    """Show donor list and allow for new donations to be entered."""
    """Finally, send thank you."""
    pass

choose_path()