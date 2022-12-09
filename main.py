import os
import sys
import numpy as np

if __name__ == '__main__':
    DATA = "./data/"

    days = range(5, 25, 1)
    for d in days:

        dayName = "Day{0}".format(d)
        pyName = "{0}.py".format(dayName)
        dataNameA = "{0}{1}_A.txt".format(DATA, dayName)
        dataNameB = "{0}{1}_B.txt".format(DATA, dayName)
        pyData = "import os\nimport sys\nimport numpy as np\nfrom collections import defaultdict\n\nif __name__ == '__main__':\n\tdataFileA = \"{0}\"\n\tdataFileB = \"{1}\"\n".format(dataNameA, dataNameB)
        readLinesPyA = "\t# Section A:\n\twith open(dataFileA) as fhA:\n\t\tpass\n\n"
        readLinesPyB = "\t# Section B:\n\twith open(dataFileA) as fhB:\n\t\tpass\n"
        pyData += readLinesPyA
        pyData += readLinesPyB
        with open("./" + pyName, 'w') as fh:
            fh.write(pyData)
        with open(dataNameA, 'w') as fh:
            pass
        with open(dataNameB, 'w') as fh:
            pass
