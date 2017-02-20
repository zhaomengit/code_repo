#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
脚本模板

实现:

qdcontrol start/stop/version等命令行


"""

import sys


def start_fun(args):
    print "start"


def stop_fun(args):
    print 'stop'


def upgrade_fun(args):
    print 'Coding in action, please waiting.....'


def version_fun(args):
    print 'version'


def _cli_parse():  # pragma: no coverage
    from argparse import ArgumentParser

    parser = ArgumentParser(usage="Usage: ./qdcontrol <command>, --help for help.")
    subparsers = parser.add_subparsers(title='Commands', description='all commands')
    start_parser = subparsers.add_parser('start', help='Start qdagent.')
    stop_parser = subparsers.add_parser('stop', help='Stop qdagent.')
    upgrade_parser = subparsers.add_parser('upgrade', help='Upgrade qdagent.')
    version_parser = subparsers.add_parser('version', help='Show the agent version.')

    start_parser.set_defaults(func=start_fun)
    stop_parser.set_defaults(func=stop_fun)
    upgrade_parser.set_defaults(func=upgrade_fun)
    version_parser.set_defaults(func=version_fun)

    cli_args = parser.parse_args()
    return cli_args, parser


def _main(argv):
    args, parser = _cli_parse()

    args.func(args)

    def _cli_error(cli_msg):
        parser.print_help()
        print '\nError: %s\n' % cli_msg
        sys.exit(1)


if __name__ == '__main__':  # pragma: no coverage

    if len(sys.argv) == 1:
        print "Usage: ./qdcontrol <command>, --help for help."
        sys.exit(1)
    _main(sys.argv)
