import sys
import numpy as np
import json
import argparse


def get_argument_parser():
    parser = argparse.ArgumentParser();
    parser.add_argument('--file_name', type=str, default='files_to_be_compressed/hmm40.txt',
                        help='The name of the input file')
    
    return parser

parser = get_argument_parser()
FLAGS = parser.parse_args()

input_file = FLAGS.file_name
param_file = "params"
output_file = "output"

with open(input_file) as fp:
    data = fp.read()

print(len(data))
vals = list(set(data))
vals.sort()
print(vals)

char2id_dict = {c: i for (i,c) in enumerate(vals)}
id2char_dict = {i: c for (i,c) in enumerate(vals)}

params = {'char2id_dict':char2id_dict, 'id2char_dict':id2char_dict}
with open(param_file, 'w') as f:
    json.dump(params, f, indent=4)

print(char2id_dict)
print(id2char_dict)

out = [char2id_dict[c] for c in data]
integer_encoded = np.array(out)
integer_encoded = integer_encoded.reshape(len(integer_encoded), 1)
print(integer_encoded[:10])
print(data[:10])

np.save(output_file, integer_encoded)