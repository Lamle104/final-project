birthdays = {'Tj': 'Sept 29', 'Tommy': 'Aug 30', 'Antonette': 'June 6'} #dictionary of names stored
dates = {'Tj': 'A cooking pan', 'Tommy': 'Coffee', 'Antonette': 'microphone'}



print('Whos birthday do you want me to remind you of? Tj, Tommy, or Antonette.')



while True:
    print('Enter the name: (blank to quit)') #enter the name of friend
    name = input() #the name is what you input
    if name == '': #if blank then the program exits
        break
    
    if name in birthdays: #checks to see if the name exits in the dictionary
        print(birthdays[name] + ' is the birthday of ' + name)
    if name in dates: #checks to see if the name exits in the dictionary
        print(dates[name] + ' is the gift for ' + name)
    else:
        print('I do not have birthday information for ' + name) #if there is no birthday you can add the name
        print('What is their birthday?') #asking what is their birthday
        bday = input() #input your friends birthday
        birthdays[name] = bday 
        print('Birthday database updated.') #birthday is updated in the database.



