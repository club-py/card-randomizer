
# scroll to the bottom to run

def get_random_card(type='int'):
    
    # this function gets a random card from two predetermined lists.
    # in the input, you can choose either 'string' or 'int' types
    # if 'str' is chosen, the function will return the value of one full card
    # if 'int' is chosen, the function will return a random number between 0 and the total number of cards
    
    import random

    # check if 'type' (defined in the function call) is 'str', if it is, set the 'cards' variable to a list of all cards
    if type == 'str':
        cards = [
            'Allowed to use your hands to score',
            'Goal counts for double',
            'Two goalies',
            'No goalies',
            'You can\'t kick the ball with your right leg',
            'You can\'t kick the ball with your left leg',
            'You have to side shuffle around the field',
            'You have to grapevine around the field',
            'You have to gallop around the field',
            'You have to score above the goal',
            'The ball cannot touch the ground',
            'Set aside this card, draw 2 more cards, follow both those rules for the 1 round, if both cards are conflicting, redraw the second card',
            'Draw a card from the bottom of the deck',
            'No communication',
            'One word communication only',
            'Only players with blue on their clothes can score',
            'Only players with red on their clothes can score',
            'Walking only',
            'Airplane arms and noises the whole round',
            'Referee chooses a \'spy\' on each team to work in the favor of the opposing team',
            'Whoever is in possession of the ball must sing a song',
            'Whoever is in possession of the ball must recite a youtube sponsorship ',
            'Every time you touch the ball you have to give a heartfelt apology to the ball',
            'You can only have the ball for 3 seconds at a time before passing to someone else ',
            'Whoever is in possession of the ball must flirt with it',
            'Switch out the soccer ball for a tennis ball, team members must juggle it to the goal to score, to steal the ball you can swipe it but must start juggling afterwards',
            'You are now a sports commentator! The player in possession of the ball must narrate everything they do',
            'Every time you take the ball from the opposing team, you must give a heartfelt apology',
            'Every time the ball switches possession, the receiver must compliment the person who touched it last',
            'Every time the ball switches possession, the receiver must give a random fun fact',
            'No more speaking, everyone must use only animal sounds',
            'Every time the ball switches possession, the receiver must dab',
            'Referee calls red light and green light, if you move on red light, you must go to your end of the field, leave the ball where it is if you are sent back',
            'Each team must form a Conga line (including goalies)',
            'One member from each team must step onto the sidelines and dance with each other until the end of the round.']
    
    # if 'type' is anything other than string, this executes.
    else:
        # set the 'cards' variable to a list of all numbers between and including 1 and 35 (this is the total number of cards)
        cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
    
    # return to the function call with a random choice from the list of cards that was set
    return random.choice(cards)

def get_many_cards(size = 10):

    # this function uses a primitive solution to create a list of many random cards

    # create an empty list called 'list'. you should not use list as a variable name, but i dont care.
    list = []

    # for every element in the range between 0 and the size (defined in the function call), add a random card to the list we made
    # i imagine using a for loop is not the best for this, but it has served me quite well.
    for i in range(0, size):

        # append the value from get_random_card() to the list named 'list'
        list.append(get_random_card())

    # return the created list of cards
    return list

def convert_dict_to_str(d):

    # this is a simple little function, and im rather proud of how compact it is

    # this is another form of for loop, but in simple terms, this goes through the entire dictionary, and converts each
    # key to a string, and each value to an integer
    # this is to make the data more readable in the final plot.
    return {str(k): int(v) for k, v in d.items()}

def plot(CARDS=100000):
    import matplotlib.pyplot as plt

    # in this section, well set up our baseline variables

    # using the function get_many_cards(), create a list of 35 cards (as denoted in size = 35)
    values = get_many_cards(size=CARDS)

    # create an empty dictionary
    freq = {}

    # this section counts the number of occurences of each value in the list (which is denoted by our 'values' variable)

    # iterate through 'values' list
    for i in values:

        # we'll use the value in the list as our dictionary 'key', and let its value be the number of times it occurs

        # let the current key = 0 and add 1, or if it already exists just add one
        freq[i] = freq.get(i, 0) + 1

    # in this section, well do some post-processing on the dictionary to make it nicer to display.

    # let freq = a sorted version of itself
    freq = {k: v for k, v in sorted(freq.items())}

    # call convert_dict_to_str() function (which converts every key in the dictionary to a string), and assign it to the variable freq2
    freq2 = convert_dict_to_str(freq)

    # in this section, we'll create our graph and get it ready for displaying

    # create a bar graph using the key names (which are the numbers that occur in our 'values' list, and their values, which is how often that value occurs)
    plt.bar(freq2.keys(), freq2.values())

    # label and title the graph
    plt.xlabel('random card (rule number)')
    plt.ylabel('frequency of occurence')
    plt.title(f'is python\'s random number generator biased?\n(dataset of {CARDS} cards)')

    # display the created chart
    plt.show()

if __name__ == '__main__':
    # heres where to choose what this script actually does. 
    # leave all items commented except the one you want to use
    # guide:
    #   uncomment print(get_random_card('str')) to print one random card.
    #   uncomment print(get_many_cards(size=100)) to print 100 random cards
    #   uncomment plot(1000) to graph the outcome of 1000 cards.

    print(get_random_card('str'))
    #print(get_many_cards(size=100))
    #plot(1000)
