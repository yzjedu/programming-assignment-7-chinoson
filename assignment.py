import csv

# Constants for column indices

# Function that loads movie data from a CSV file and returns it as a list of lists.

def load_movie_data(filename):

    inFile = open(filename, 'r')
    
    movieTable = []

    for line in inFile:
        row = line.strip().split(',')
        movieTable.append(row)

    inFile.close()

    return movieTable

# /Users/henderson/Documents/loyola/summer_24/CS701_WO2/week_5/programming_assignment/programming-assignment-7-chinoson/movies.csv

# Function that adds a profit column to the movie data.

def add_profit_column(movieTable):

    for i in range(len(movieTable)):
        profit = float(movieTable[i][3]) - float(movieTable[i][2])
        movieTable[i].append(profit)
    
    return movieTable

# Function that prints the movies with the highest and lowest profits.

def print_min_and_max_profit(movieTable):

    min = 0
    max = 0
    lowestProfit = []
    highestProfit = []

    for i in range(len(movieTable)):
        if movieTable[i][4] < min:
            min = movieTable[i][4]
            lowestProfit = movieTable[i]
        if movieTable[i][4] > max:
            max = movieTable[i][4]
            highestProfit = movieTable[i]


    print(lowestProfit)
    print(highestProfit)


# Function that prints detailed information about a movie.

def get_movie_details(movieTable,title):
    header = ['Release Date', 'Title', 'Production Costs', 'Expenses', 'Profit']
    print(header)
    for i in range(len(movieTable)):
        if movieTable[i][1] == title:
            print(movieTable[i])

# Function that saves the movie data with the profit column to a new CSV file.

def save_profit_file(movieTable, path):
    
    outfile = open(path,'w')
    out = ''

    for line in movieTable:
        lineString = ''
        for item in line:
            lineString += str(item)
            lineString += ','
        lineString += '\n'
        out += lineString
        
    outfile.write(out)

    outfile.close

def main():
    # Write the code for the main function here and delete pass
    #pass

    #load provided file
    movieTable = load_movie_data('/Users/henderson/Documents/loyola/summer_24/CS701_WO2/week_5/programming_assignment/programming-assignment-7-chinoson/movies.csv')

    #add profit data
    movieTablewProfit = add_profit_column(movieTable)

    #print highest and lowest profiting movies
    print_min_and_max_profit(movieTablewProfit)

    #print details for a film of interest
    get_movie_details(movieTablewProfit, 'The Dark Knight Rises')

    #save movie data with profit info added - same format as original input file
    save_profit_file(movieTablewProfit, '/Users/henderson/Documents/loyola/summer_24/CS701_WO2/week_5/programming_assignment/programming-assignment-7-chinoson/movies_w_profit.csv')



if __name__ == "__main__":
    main()