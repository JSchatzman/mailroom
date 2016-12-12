"""Mailroom Implementation.  Create thank you cards or donation reports."""
from __future__ import unicode_literals

donors = {'jordan schatzman': [100, 200, 400, 50.6],
          'rick valenzuela': [500, 300, 100, 50, 1.24],
          'sally johnson': [50, 100, 1, 2, 99],
          'jane': [39, 23, 532, 2432],
          'bob': [89, 23, 12, 3.45643]}


def main():
    """Allow the user to begin the program."""
    while True:
        input_prompt = 'If you want to submit a thank you, enter'
        input_prompt += ' "Send a Thank You".  If you would like to see a'
        input_prompt += ' donation report, enter "Create a Report".'
        input_prompt += ' If at any time you wish to return to this menu,'
        input_prompt += ' enter "menu".  Otherwise, enter "Quit" to quit: '
        choice = input(input_prompt)
        if choice.lower() == 'create a report':
            print (create_a_report())
        elif choice.lower() == 'send a thank you':
            control_thank_you()
        elif choice.lower() == 'quit':
            exit()
        else:
            print ('\n Please submit a valid input. \n')
            main()


def control_thank_you():
    """Handle logic for sending a thank you."""
    while True:
        input_prompt = 'If you want to see a list of donors, enter "list".'
        input_prompt += '  Otherwise, enter a donor name: '
        choice = input(input_prompt)
        if choice == 'list':
            sorted_donors = create_sorted_list()
            for donor in sorted_donors:
                print (donor)
        elif choice == 'menu':
            print ('\n \n')
            main()
        elif choice.lower() in donors:
            chosen_donor = choice.lower()
            input_prompt = choice + ' has already donated.'
            input_prompt += '  Please enter a new donation:  '
            donation = input(input_prompt)
            new_donation = add_donation(chosen_donor, donation)
            print (print_email(chosen_donor, new_donation))
        elif choice.lower() not in donors:
            chosen_donor = choice.lower()
            donors[chosen_donor] = []
            input_prompt = chosen_donor + ' has been added.  Please'
            input_prompt += ' submit a donation'
            donation = input(input_prompt)
            new_donation = add_donation(chosen_donor, donation)
            print (print_email(chosen_donor, new_donation))


def create_sorted_list():
    """Create a sorted list of donors."""
    sorted_list = []
    for donor in sorted(list(donors.keys())):
        donor = donor.split(' ')
        sorted_list.append(' '.join(list(map(lambda x: x.capitalize(), donor))))
    return sorted_list


def add_donation(donor, donation):
    """Add donation for a speciic donor."""
    invalid_donation = True
    while invalid_donation:
        try:
            invalid_donation = float(donation)
            donors[donor].append(float(donation))
            invalid_donation = False
        except ValueError:
            input_prompt = 'Please enter a valid number: '
            donation = input(input_prompt)
    return donation


def print_email(donor, donation):
    """Print email to console."""
    email = "Dear {0},"
    email += '\n \n \n'
    email += 'Thanks so much for your donation of ${1}.  We love you!'
    email += ' Please feel free to donate again.'
    email += '\n \n \n'
    email += 'Love, \n CodeFellows'
    return email.format(donor, donation)


def create_a_report():
    """Create a donor report with list of donors, count, average and sum."""
    output = ''
    output += 'Donor Name--------------Count-----Average--------Sum\n'
    output += ('-' * 62) + '\n'
    donor_ordered = [[k, sum(v)] for k, v in donors.items()]
    donor_ordered.sort(key=lambda x: -x[1])
    for donor in donor_ordered:
        donations = donors[donor[0]]
        donation_count = str(len(donations))
        donation_sum = str(round(sum(donations), 2))
        donation_avg = str(round(float(sum(donations)) / len(donations), 2))
        name = donor[0].split(' ')
        name = ' '.join(list(map(lambda x: x.capitalize(), name)))

        output += '{0}{1}{2}{3}{4}{5}{6}{7}\n'.format(' ' * 3,
                                                      name,
                                                      ' ' * (23 - len(name)),
                                                      str(len(donations)),
                                                      ' ' * (10 - len(donation_count)),
                                                      donation_avg,
                                                      ' ' * (13 - len(donation_avg)),
                                                      donation_sum)
    return output

"""
def create_a_report():
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
                                                 donation_sum)) """

if __name__ == '__main__':
    main()
