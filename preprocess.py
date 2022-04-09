# Remove duplicated records
folder = "Data/"
country_name = "Korea"
in_file = folder+ country_name + "_data.csv"
out_file = folder + country_name+ "_processed.csv"

import re

spcial_char_map = {ord('ä'):'ae',
                   ord('ü'):'ue',
                   ord('ö'):'oe',
                   ord('ß'):'ss',

                   ord('é'): 'e',
                   ord('è'): 'e',
                   ord('á'): 'a',
                   ord('à'): 'a',
                   ord('ó'): 'o',
                   ord('ò'): 'o',
                   ord('ú'): 'u',
                   ord('ù'): 'u',
                   ord('í'): 'i',
                   ord('ì'): 'i',

                   ord('â'): 'a',
                   ord('î'): 'i',
                   ord('ê'): 'e',
                   ord('ñ'): 'n',
                   ord('ç'): 'c',
                   ord('ï'): 'i',

                   ord('æ'): 'ae',
                   ord('œ'): 'oe',
                   }
with open(in_file,'r') as in_file, open(out_file,'w') as out_file:
    seen = set() # set for fast O(1) amortized lookup
    for line in in_file:
        line = line.translate(spcial_char_map).lower()
        line = line.encode("ascii", "ignore").decode()
        if line not in seen:
            seen.add(line)
            out_file.write(line)