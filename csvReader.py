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

  #adds the inital url to the list along with the set
  for setTag in getColumn(csvRows, getHeaderIndex('Set', headers)):
     
    #removes spaces and replaces them with hypens
    name = setTag.split(' ') 
    name3 = ''
    for name2 in name:
      name3+=name2+"-"
    name3=name3[:-1]    

    urls.append('https://shop.tcgplayer.com/pokemon/'+name3+'/')


  i = 0 #index counter
  for penis in getColumn(csvRows, getHeaderIndex('Name', headers)): #grabs the list of pokemon names
    
    #removes spaces and replaces them with hypens
    name = penis.split(' ') 
    name3 = ''
    for name2 in name:
      name3+=name2+"-"
    name3=name3[:-1]

    #goes through possible specialties and adds it to the tag
    if(getColumn(csvRows, getHeaderIndex('Special', headers))[i] == 'EX'):
      urls[i] += name3+'-ex'
    elif(getColumn(csvRows, getHeaderIndex('Special', headers))[i] == 'SR'):
      urls[i] += name3+'-secret'
    elif(getColumn(csvRows, getHeaderIndex('Special', headers))[i] == 'RR'):
      urls[i] += name3+'-secret'
    elif(getColumn(csvRows, getHeaderIndex('Special', headers))[i] == 'GX'):
      urls[i] += name3+'-gx'
    elif(getColumn(csvRows, getHeaderIndex('Special', headers))[i] == 'FA'):
      urls[i] += name3+'-full-art'
    else:
      urls.insert(i, name3)

    i=i+1
    
  return urls



#https://shop.tcgplayer.com/pokemon/swsh01-sword-and-shield-base-set/quick-ball

def main(): # not needed, just nice to have a runner
    # List of lists where each list inside is a row of the CSV that had a pokemon
    CSVRows, headers = getListFromCSV('PokemonCardsNicholas.csv')
    #print(CSVRows)
    #print (getColumn(CSVRows, getHeaderIndex('Set', headers)))
    #print (getColumn(CSVRows, headers.index('Name')) # in an alternate universe where we have foresight

    return appendURLs(CSVRows, headers)


main()