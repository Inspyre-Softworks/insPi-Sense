#!/usr/bin/env python3

from argparse import ArgumentParser

parser = ArgumentParser(prefix_chars='+-')

subparsers = parser.add_subparsers()
parser.add_argument('-v', '--verbose',
                    action='store_true',
                    dest='is_verbose',
                    help='Set program to output logs to STDOUT verbosely',
                    required=False)

gui_parser = subparsers.add_parser("GUI")

gui_parser.add_argument('--qt',
                        help='Run with QT instead of TKInter',
                        action='store_true',
                        dest='is_qt',
                        required=False)

args = parser.parse_args()

print(args)

import inspi_sense

inspi_sense.InsPiSense(args)

