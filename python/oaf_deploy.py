"""
This script will automate the deployment of the OAF components to the Server.
Once Files have been migrated to the server the script can be used for below purpose
Compile Java files
Import Pages and Regions
Bounce Server
"""
import os, sys

# Configuration variables
OAF_CUST_TOP = "xxexpd/oracle/apps"
HOST = ""
APPS_PASS = ""
PORT = ""
SID = ""


def show_usage():
    print "Below are the command usage\n"
    print "oaf_deploy.py bounce|module_path java|page filename|bounce <bounce>"

    print "\tBounce server"
    print "\toaf_deploy.py bounce"

    print "\tCompile all Java files, no bounce"
    print "\toaf_deploy.py module_path java"

    print "\tCompile a single Java file, no bounce"
    print "\toaf_deploy.py module_path java myfile.java"

    print "\tCompile all Java files and bounce"
    print "\toaf_deploy.py module_path java bounce"

    print "\tCompile a single Java file and bounce"
    print "\toaf_deploy.py module_path java myfile.java bounce"

    print "\tImport all Page/Region, no bounce"
    print "\toaf_deploy.py module_path page"

    print "\tCompile a single Page/Region file, no bounce"
    print "\toaf_deploy.py module_path page mypage.xml"

    print "\tCompile all Page/Region files and bounce"
    print "\toaf_deploy.py module_path page bounce"

    print "\tCompile a single Java file and bounce"
    print "\toaf_deploy.py module_path page mypage.xml bounce"

    exit(0)


# Return all the files from Subdirectories of given pattern
def find_files(path, file_extn):
    for dirpath, dirnames, filenames in os.walk(path):
        return [os.path.join(dirpath, file) for file in filenames if file.endswith(file_extn)]

# Method to compile Java File(s)
def compile_java(file):
    cmd = ""
    if len(file) <> 0:
        print "Compiling File " + file
        cmd = 'find ./ -type f -name "{:1}" -exec javac {} \;'.format(file)
    else:
        print "Compiling all Java Files"
        cmd = 'find ./ -type f -name "*.java" -exec javac {} \;'
    # Execute the command
    os.system(cmd)


# Method to import Page/Region(s)
def import_page(file):
    cmd = ""

    if len(file) <> 0:
        print "Importing page " + file
    else:
        print "Importing all page of Modules"


# Check if any parameters are passed
if len(sys.argv) < 1:
    show_usage()
