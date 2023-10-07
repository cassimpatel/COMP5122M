# -*- coding: utf-8 -*-
"""
Created on 26 Sep 2018. Updated 29 Jan 2021.

How to use chardet to detect a text file's encoding

@author: Roy Ruddle
"""
import chardet
import pandas as pd

def detect_file_encoding(input_filename):
    """
    Detect and return the encoding of a text file
    
    :param input_filename: The name of the file
    :return A dictionary containing the 'encoding' and a 'confidence' level, or None (file could not be found/opened)
    """
    read_in_chunks = False # True or False
    confidence_level = 0.9 # 0.0 to 1.0
    result = None
    
    try:    
        with open(input_filename, "rb") as fin:
    
            if read_in_chunks:
    
                while True:
    
                    try:
                        chunk_size = 1024
                        rawdata = fin.read(chunk_size)
                        
                        if len(rawdata) > 0:
                            result = chardet.detect(rawdata)
                            
                            if result['confidence'] >= confidence_level:
                                break
                            else:
                                result = None
    
                        else:
                            break
    
                    except Exception as e:
                        raise
    
            else:
    
                try:
                    rawdata = fin.read()
                    
                    if len(rawdata) > 0:
                        result = chardet.detect(rawdata)
    
                except Exception as e:
                    raise
    
    except Exception as e:
        raise
    else:
        print(result)
    
    return result


#
# Main program
#

print('Create a data frame with English and German names')
data = {'Name': ['Andrew', 'Jörn'], 'Number': [1, 2]}
df = pd.DataFrame.from_dict(data)
print(df)

print() # Blank line
print('Write the data frame to a file (the Pandas to_csv() default text file encoding is utf-8)')
output_filename = 'teaching chardet.csv'
df.to_csv(output_filename)

print() # Blank line
print('Detect the file encoding (do you know why the result is different to the encoding that to_csv() actually used?)')
input_filename = output_filename
result = detect_file_encoding(input_filename)

print() # Blank line
print('Read the file using the encoding that chardet() detected')
df2 = pd.read_csv(input_filename, encoding=result['encoding'])

print() # Blank line
print('Read the file using ascii encoding (do you know why this crashes?)')
df2 = pd.read_csv(input_filename, encoding='ascii')
