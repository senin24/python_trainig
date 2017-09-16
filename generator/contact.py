from model.contact import Contact
import random
import string
import os.path
import getopt
import sys
import jsonpickle


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
              # + " "*10
    return prefix + "_" + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

#TODO create: random names, emails, telephones, www addreses

testdata =  [
    Contact(firstname=random_string("firstname", 10), lastname=random_string("lastname", 10), nickname=random_string("nickname", 10),
            company=random_string("company", 20), title=random_string("title", 10), address=random_string("address", 40),
            home=random_string("home", 10), mobile=random_string("mobile", 10), work=random_string("work", 10),
            phone2=random_string("phone2", 10), email=random_string("email", 20), email2=random_string("email2", 20),
            email3=random_string("email3", 20), homepage=random_string("homepage", 10)
            )
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", sort_keys=True, indent=2)
    out.write(jsonpickle.encode(testdata))