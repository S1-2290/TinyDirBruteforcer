import os, sys, requests
from __meta import Colors, Patterns
from __utils import MetaUtils

## Variables - Colors ##
# C: https://null-byte.wonderhowto.com/how-to/build-directory-brute-forcing-tool-python-0169477/
gs = Colors.GREEN
rs = Colors.RED
ys = Colors.YELLOW
ws = Colors.WHITE
bs = Colors.BLUE
ce = Colors.COLOR_END
# Patterns
plus = Patterns.PLUS
minus = Patterns.MINUS
astk = Patterns.ASTK

## Main entry ##
class Utils:

    def __init__(self, web_site, use_ssl, wordlist, port):
        self.url = web_site
        self.ssl = use_ssl
        self.list = wordlist
        self.port = port

    def main_loop(self):
        main = MetaUtils(self.url, self.ssl, str(self.list), int(self.port))

        main.check_host()
        main.check_wordlist_run()
