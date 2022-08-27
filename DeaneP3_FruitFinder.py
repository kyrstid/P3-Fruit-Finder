
# DeaneP3
# Programmer: Kyrsti Deane
# Email: kdeane1@cnm.edu
# Purpose: Finds the names of fruit(s) in a string entered by the user



fruits_list = ('apricot',
'asian pear',
'avocado',
'banana',
'blackberries',
'blueberries',
'boysenberries',
'cactus pear',
'cantaloupe',
'cherries',
'coconut',
'cranberries',
'figs',
'gooseberries',
'grapefruit',
'grapes',
'honeydew melon',
'kiwifruit',
'limes',
'longan',
'loquat',
'lychee',
'madarins',
'malanga',
'mandarin oranges',
'mangos',
'mulberries',
'nectarines',
'oranges',
'papayas',
'passion fruit',
'peaches',
'pears',
'persimmons',
'pineapple',
'plums',
'pomegranate',
'prunes',
'quince',
'raisins',
'raspberries',
'rhubarb',
'strawberries',
'tangelo',
'tangerines',

'tomato',
'ugli fruit',
'watermelon')

# print list of fruit for user
print('Hello, here is a list of fruits for you to review: ')
print('  ')
# have user enter a sentence that contains the name of at least one fruit
print(str(fruits_list))
print('  ')
print('>>> Note: please do not include punctuation in your sentence. <<<')
print('Enter a sentence that contains the name of at least one fruit in the list above: ')

user_sentence = str(input())
fruits = set(user_sentence.split())

userfruits = list(set(fruits)&set(fruits_list))

# display number of fruit(s) entered and fruit names
print('You entered this many fruit names: ',len(userfruits))
print('The fruit(s) you entered are: ',(userfruits))
print('  ')
# add 'brussel sprouts' to the user's sentence
print('Here''s your sentence with some brussel sprouts: ' )
print(user_sentence + ' (plus I secretly love brussel sprouts!)')

