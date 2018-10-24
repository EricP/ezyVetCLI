#!/usr/bin/env python
# -*- coding: utf-8 -*-

from settings import *    # This file contains login credentials do not track with git
from ezyvet import ezyvet
from pprint import pprint,pformat
import logging
import sys
import getopt

logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

def main():
    ''' Main function to parce commandline options
    '''
    try:
        opts, args = getopt.getopt(sys.argv[1:], "vT", ["help", "debug"])
    except getopt.GetoptError as err:
        # print help information and die:
        print(err)
        usage()
        sys.exit(2)

    try:
        if len(opts) == 0 or "-h" in opts:
            usage()
            sys.exit(0)

        else:
            mode = None

            for o, a in opts:
                if o == "-v":
                    logging.basicConfig(level=logging.INFO)

                if o == "--debug":
                    logging.basicConfig(level=logging.DEBUG)

                elif o in ("-h", "--help"):
                    usage()
                    sys.exit(0)

                elif o == "-T":
                    # Test the connection
                    ezy = ezyvet(SETTINGS, logger)
                    #sys.exit(0)

                elif o == "-p":
                    dove = ezyvet(SETTINGS, logger)
                    logger.info("ezyVet pending communications requested...")
                    coms =  dove.getPendingCommunications()
                    if coms is not None:
                        for p in coms:
                            print(p)
                        print("There are ", str(len(coms)), " communications.")
                    else:
                        print("There are no pending communications.")

                else:
                    usage()
                    assert False, "unhandled option"
    except:
        logger.error("Something went wrong, bye.", exc_info=True)

def usage():
    print("\nCommandline ezyVet by Avi Solomon (asolomon@dovelewis.org) v0.1")
    print("USAGE: >python ezyvet_cli.py [OPTIONS]")
    print("\t -h or --help: Get Help (print this help text)")
    print("\t -T Test connection to API and exit")
    print("\t -v: Verbose output")
    print("\t --debug: Very verbose output")
    print("")

if __name__ == "__main__":
    main()
