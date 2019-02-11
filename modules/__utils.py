import os, sys, socket, requests
from __meta import Colors, Patterns

## Variables - Colors ##
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

## Secondary entry ##
class MetaUtils:

    def __init__(self, website, wordlist, use_ssl, port=80):
        self.url = website
        self.list = wordlist
        self.ssl = use_ssl
        self.port = port

    # Checks the connection to the host
    def check_host(self):
        # Notify the user that checks are on-going
        print astk + ws + "Checking remote host (URL): " + ce + ys + self.url + ce

        try:
            # Initialize the socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except Exception as e:
            print "\n" + rs + "Error: " + ce + ws + str(e) + ce + "\n"
            pass

        # Try to establish the connection
        try:
            stat = sock.connect_ex((self.url, self.port))
            # Close the connection
            sock.close()

            # Check status
            if stat == 0:
                print astk + ws + "Remote host checked, looks good, proceeding..." + ce
                pass
            else:
                print + "\n" + minus + ys + "Could not establish connection to remote host: " + self.url + ce + "\n"
                sys.exit(1)
        except socket.error as e:
            print "\n" + rs + "Error: " + ce + ws + "Host unreachable, here is what I got:" + ce
            print ws + "Stack -> " + ce + ys + str(e) + ce + "\n"
            sys.exit(1)

    # Iterator function
    def check_valid_path(self, path):
        print astk + ws + "Initializing directory run-through..." + ce
        try:
            if self.ssl:
                resp = requests.get("https://" + self.url + "/" + path)
            else:
                resp = requests.get("http://" + self.url + "/" + path)
        except Exception as e:
            print "\n" + rs + "Error: " + ce + ws + str(e) + ce + "\n"
            sys.exit(1)

        if resp in [200, 205]:
            print ys + "== Valid path: " + ce + ws, path, ce
            pass

    # Run checks on the supplied wordlist and then run the iterator function
    def check_wordlist_run(self):
        print astk + ws + "Parsing supplied wordlist..." + ce
        try:
            # Open the wordlist file
            with open(str(self.list), 'r') as src:
                src2 = src.read().strip().split('\n')
                # Check for any \ characters
                if "\\" in src2 or len(src2) == 0:
                    print "\n" + minus + ws + "Possible word list errors detected:" + ce
                    print ys + "\t\t1.) The use of \"\\\" character." + ce
                    print ys + "\t\t2.) The list is empty..." + ce + "\n"
                    return
            # Print the total number of paths inside the list
            print astk + ws + "Checks complete, number of paths to check: " + ce + ys, str(len(src2)), ce

            # Run the check function for possible directories
            for x in range(len(src2)):
                main = MetaUtils(self.url, self.list, self.ssl)
                main.check_valid_path(str(src2[x]))
                pass
            pass
        except IOError as e:
            print "\n" + rs + "Error: " + ce + ws + "Could not read file, here is the error:" + ce
            print ys + "Message: " + ce + ws + str(e) + ce
            sys.exit(1)

