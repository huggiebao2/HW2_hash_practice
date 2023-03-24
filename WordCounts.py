import os.path

# get the file path
def Get_File_Path():
    path = os.path.abspath(__file__)    # absolute path of main program
    dir = os.path.dirname(path)         # current directory
    filepath = os.path.join(dir, 'hw2_data.txt')
    return filepath

def main():
    # Create A empty hash table
    word_counts = {}

    with open(Get_File_Path(), 'r') as f:
        for line in f:
            # process every line in file (strip words)
            word = line.strip()
            # check whether it is in hash table (as a "key") or not
            if word in word_counts:
                # if is key in table, value += 1
                word_counts[word] += 1
            else:
                # if not key in table, value = 1
                word_counts[word] = 1

    # Statistic outcome (show the hash table)
    print('Words: ', len(word_counts))
    print('Word Frequency: ', word_counts)

if __name__ == "__main__":
    main()