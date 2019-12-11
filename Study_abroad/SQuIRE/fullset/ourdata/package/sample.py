from __future__ import print_function,division
import sys
import os
import errno
import re
import argparse #module that passes command-line arguments into script
from datetime import datetime
import operator #for doing operations on tuple
from operator import itemgetter
import subprocess as sp
from subprocess import Popen, PIPE,STDOUT
import io
import tempfile
#for creating interval from start
from collections import defaultdict #for dictionary
import glob
import re
from six import itervalues
import shutil
tab="'"+'\t'+"'"
print(tab)
joincommand_list = ["join", "-t",tab,"-j", "12", "-o", "1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,1.10,2.1,2.2,2.3,2.4,2.5,2.6,2.7,2.8,2.9,2.10", "/mnt/squire_count/Clean3latF_Fullset_paired_ulabeled_1.tmpBrcR1N_newread_v1", "/mnt/squire_count/Clean3latF_Fullset_paired_ulabeled_2.tmpv10ntO_newread_v1", ">" , "/mnt/squire_count/Clean3latF_Fullset_paired_matched.tmpcn49vH_10k_v1"]
#print(joincommand_list)
joincommand=" ".join(joincommand_list)
sp.check_call(["/bin/sh","-c",joincommand])
print(joincommand)
