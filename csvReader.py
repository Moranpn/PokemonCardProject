import csv

# returns the list of pokemon rows from the CSV file along with the headers
def getListFromCSV(filename):
    output = []
    reading = False
    header = []
    with open(filename, 'r') as csvfile:
        datareader = csv.reader(csvfile)
        for row in datareader:
            if(row[0]=='Name'):
                header = row
                reading = True # start reading since headers reached
            elif(reading): # elif used since we don't want to read the headers
                if(row[0]==''):
                    reading = False # stop reading since end of type reached
                else:
                    #print(row) # display the row with pokemon on it
                    output.append(row)
    return output, list(filter(lambda x: x!='', header)) # removes empty headers from the list, will mess up if there are empty headers between columns

# returns a list of all items in the specified column
def getColumn(csvRows, column): 
    output = []
    for pokemon in csvRows:
        output.append(pokemon[column])
    return output

# returns a column number for the requested trait
# param header - the string of the requested header
# param headers - the list of possible headers
def getHeaderIndex(header, headers):
    return headers.index(header)

#appennds pokemon name and url
def appendURLs(csvRows, headers):
  urls = [] #list of urls
  i = 0 #index counter

  #adds the inital url to the list along with the set
  for setTag in getColumn(csvRows, getHeaderIndex('Set', headers)):
    
    #removes spaces and replaces them with hypens
    name = setTag.split() 
    name3 = ''
    for name2 in name:
      name3+=name2+"-"
    name3=name3[:-1] # Remove the last dash

    urls.append('https://shop.tcgplayer.com/pokemon/'+name3+'/')

  for penis in getColumn(csvRows, getHeaderIndex('Name', headers)): #grabs the list of pokemon names
    
    #removes spaces and replaces them with hypens
    name = penis.split()
    name3 = ''
    for name2 in name:
      name3+=name2+"-"
    name3=name3[:-1]

    specialTag = getColumn(csvRows, getHeaderIndex('Special', headers))[i]
    #goes through possible specialties and adds it to the tag
    if(specialTag == 'EX'):
      urls[i] += name3+'-ex'
    elif(specialTag == 'SR'):
      urls[i] += name3+'-'+secrets(csvRows, headers, i)
    elif(specialTag == 'GX'):
      urls[i] += name3+'-gx'
    #elif(specialTag == 'FA'):
    #  urls[i] += name3+'-full-art'
    elif(specialTag == 'V'):
      urls[i] += name3+'-v'
    elif(specialTag == 'LvX'):
      urls[i] += name3+'-lvx'
    elif(specialTag == 'Prism'):
      urls[i] += name3+'-prism-star'
    elif(specialTag == 'Mega EX'):
      urls[i] += name3+'-ex'
    elif(specialTag == 'GX Tag Team'):
      urls[i] += name3+'-gx'
    elif(specialTag == 'Prime'):
      urls[i] += name3+'-prime'
    elif(specialTag == 'Break'):
      urls[i] += name3+'-break'
    elif(specialTag == 'Primal EX'):
      urls[i] += name3+'-ex'
    elif(specialTag == 'GX Ultra Beast'):
      urls[i] += name3+'-gx'
    elif(specialTag == 'Star'):
      urls[i] += name3+'-star'
    elif(specialTag == 'Delta Species'):#deoxys
      urls[i] += name3+'-delta-species-defense-forme'
    else:
      #urls.insert(i, name3)
      urls[i] += name3

    rarityTag = getColumn(csvRows, getHeaderIndex('Rarity', headers))[i]
    #goes through possible rarities and adds it to the tag
    if(rarityTag == 'RR'):
      urls[i] += '-secret'
    elif(rarityTag == 'FA UR'):
      urls[i] += '-' + fullarts(csvRows, headers, i)
    elif(rarityTag == 'PROMO UR'):
      urls[i] += '-' + promos(csvRows, headers, i) 
    elif(rarityTag == 'FA UR OMEGA'):#groudon
      urls[i] += '-omega-151-full-art'
    elif(rarityTag == 'FA UR 89'):#hoopa
      urls[i] += '-89-full-art'
    elif(rarityTag == 'PROMO UR SHINY'):#metagross
      urls[i] += '-shiny'
    elif(rarityTag == 'UR Plasma'):#palkia
      urls[i] += '-team-plasma'

    if(getColumn(csvRows, getHeaderIndex('Number', headers))[i] == 'XY85'):#hoopa
      urls[i] += '-collection-promo'
    #if(getColumn(csvRows, getHeaderIndex('Number', headers))[i] == '6/34'):#team aqua kyogre
    #  urls[i] += ''
    
    i+=1
    
  return urls

#adds the card number to the full art tag
def fullarts(csvRows, headers, i):
  fullArtTag = getColumn(csvRows, getHeaderIndex('Set', headers))[i]
  if(fullArtTag != 'XY Roaring Skies' and fullArtTag != 'XY Primal Clash' and getColumn(csvRows, getHeaderIndex('Special', headers))[i] != 'FA'): 
    return 'full-art'
  else:
    number = getColumn(csvRows, getHeaderIndex('Number', headers))[i]
    return number[0:number.find('/')] + '-full-art'

#checks to see if the SR card needs SR tag
def secrets(csvRows, headers, i):
  if(getColumn(csvRows, getHeaderIndex('Special', headers))[i] != "SR"):
    return '-secret'
  else:
    return ''

#checks promos for tag team or for black and white set
def promos(csvRows, headers, i):
  if(getColumn(csvRows, getHeaderIndex('Name', headers))[i].find(" and ") == -1 and getColumn(csvRows, getHeaderIndex('Set', headers))[i].find(" and ") == -1):
    return getColumn(csvRows, getHeaderIndex('Number', headers))[i]
  else:
   return ''



#https://shop.tcgplayer.com/pokemon/swsh01-sword-and-shield-base-set/quick-ball

def main(): # not needed, just nice to have a runner
    # List of lists where each list inside is a row of the CSV that had a pokemon
    CSVRows, headers = getListFromCSV('PokemonCardsNicholas.csv')
    #print(CSVRows)
    #print (getColumn(CSVRows, getHeaderIndex('Set', headers)))
    #print (getColumn(CSVRows, headers.index('Name')) # in an alternate universe where we have foresight

    return appendURLs(CSVRows, headers)


main()