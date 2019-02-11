import os, sys
from modules.tbf_utils import Utils
from optparse import OptionParser

## Main module ##

def main():
    parser = OptionParser(usage="%prog [OPTIONS] <ARG=path_to_wordlist> | -h, --help", conflict_handler="resolve")
    # Add the host, ssl, and wordlist options as well as port options
    parser.add_option('-H', '--remote-host', dest="host", default="127.0.0.1", help="The remote URL to pass through.")
    parser.add_option('-w', '--wordlist', type=str, dest="wlist", help="Specify the wordlist to parse.")
    parser.add_option('-p', '--port', dest="port", default=80, help="The remote port to use.")
    parser.add_option('--use-ssl', dest="use_ssl", action="store_true", help="Use SSL when passing through pages.")

    (options, args) = parser.parse_args()

    if options.wlist:
        with open(options.wlist, 'r') as words:
            main = Utils(options.host, options.use_ssl, str(words), int(options.port))

        main.main_loop()


if __name__ == '__main__':
    main()
