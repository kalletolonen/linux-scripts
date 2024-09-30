import sys

input_filename = sys.argv[1]
output_filename = 'output_with_commas.txt'

open(input_filename).read().replace(',\n','S,\n').write()