#!/usr/bin/python
import argparse
import logging
import os
import sys
import xformer

def transform(input_file_path, transformer_file_path, transform_type, separator):
    
    # verify inputs exist
    if not os.path.exists(input_file_path):
        raise IOError("%s does not exist." % input_file_path)

    if not os.path.exists(transformer_file_path):
        raise IOError("%s does not exist." % transformer_file_path)

    # transform
    if transform_type == 'xslt':
        xformed = xformer.xslt_transformer(input_file_path, transformer_file_path)
        sys.stdout(xformed)
    elif transform_type == 'simple':
        xformer.simple_transformer(input_file_path, transformer_file_path, separator)



def main():
    parser = argparse.ArgumentParser(description="Transforms provided input to standard output, based on the transform.")
    parser.add_argument('-i', '--input', help='Input File', action='store', required=True)
    parser.add_argument('-t', '--transformer', help='Transform File', action='store', required=True)
    parser.add_argument('-x', '--transformer_type', help='Transformer Type', choices=['xslt', 'simple'], default='simple')
    parser.add_argument('-s', '--separator', help='Row Separator for standard output. Not applicable for xslt.', default='')

    args = parser.parse_args()
    try:
        transform(args.input, args.transformer, args.transformer_type, args.separator)
    except Exception, e:
        logging.exception("Error occurred while running code.")

if __name__ == "__main__":
    main()
