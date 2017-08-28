""" This script downloads the data for some of the "homework"
from the Online Brain Intensive Course. The data is stored
at Surfdrive (a data storage repository/drive from the
Dutch institute for IT in science/academia) and downloaded
using cURL, which should be cross-platform. """

from __future__ import print_function
import subprocess
import os
import zipfile
import os.path as op
import platform

cmd = "where" if platform.system() == "Windows" else "which"
with open(os.devnull, 'w') as devnull:
    res = subprocess.call([cmd, 'curl'], stdout=devnull)

    if res != 0:
        raise OSError("The program 'curl' was not found on your computer! "
                      "Either install it or download the data from surfdrive "
                      " (link on website)")

this_dir = op.dirname(op.realpath(__file__))
dst_dir = op.join(this_dir, 'data')

if not op.isdir(dst_dir):
    os.makedirs(dst_dir)

data_file = 'https://surfdrive.surf.nl/files/index.php/s/2iHbWhxFM8D3H8d/download'
dst_file = op.join(dst_dir, 'data.zip')

if not op.isdir(dst_dir):
    print("Downloading the data ...\n")
    cmd = "curl -o %s %s" % (dst_file, data_file)
    return_code = subprocess.call(cmd, shell=True)
    print("\nDone!")
    print("Unzipping ...", end='')
    zip_ref = zipfile.ZipFile(dst_file, 'r')
    zip_ref.extractall(dst_dir)
    zip_ref.close()
    print(" done!")
    os.remove(dst_file)
else:
    print("Data is already downloaded and located at %s/*" % dst_dir)
