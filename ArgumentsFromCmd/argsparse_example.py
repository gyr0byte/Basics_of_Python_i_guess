import argparse

parser = argparse.ArgumentParser(
    description="This program prints color i entered"
)

parser.add_argument('-c', '--color', 
                    metavar= 'color', required= True, choices= {"red", "yellow", "blue"},
                    help= " The color to search for")

args = parser.parse_args()
print(args.color)

# steps to run
# open terminal and type cd ArgumentsFromCmd
# and type python argsparse_example.py -c blue