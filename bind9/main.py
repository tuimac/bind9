#!/usr/bin/env python3

import os
import path
import logging
import traceback
import yaml
import argparse
import .config.namedConfig

logger = logging.getLogger('bind9')

def importConfig(path):
    try:
        path = os.path.expanduser(path)
        with open(path, 'r') as conf:
            return yaml.load(conf, Loader=yaml.SafeLoader)
    except Exception as e:
        raise e

class CustomArgparse(argparse.ArgumentParser):
    def error(self, message):
        if message == "":
            print("[Error] Argument is wrong...<(^^;)\n", file=sys.stderr)
        else:
            print("[Error] " + message + "\n", file=sys.stderr)
        self.print_help()
        sys.exit(2)

def main():
    parser = CustomArgparse(
        prog = "bind9",
        description = "Just Bind9 manager to set up easier.",
        add_help = True
    )
    try:
        parser.add_argument(
            "-c",
            "--config",
            dest = "config",
            nargs = 1,
            required = True,
            help = "[Required] Direct bind9.yaml to import config.",
        ) 
        args = parser.parse_args()

        if args.config:
            config = Config(importConfig(args.config))

        else:
            parser.error

    except:
        parser.
        traceback.print_exc()

if __name__ == '__main__':
    main()
