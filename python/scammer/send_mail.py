import os, shutil
from glob import glob

# Option Values
file_path = "D:\python_test"
new_file_path='D:\python_test\\test'
file_count_limit = 1

# Check if a variable is Int type or not
def is_int(var):
    try:
        int(var)
        return True
    except Exception:
        return False


# Go to files directory and read the file
os.chdir(file_path)
file_count = 0
for filename in glob('ER_802*.txt.bad'):
    # Delete empty files
    if os.path.getsize(filename) == 0:
        os.remove(filename)
        continue  # Skip to other file

    new_filename = os.path.join(new_file_path, os.path.basename(filename) + ".tmp")
    print filename
    fp = open(filename, 'r')
    nfp = open(new_filename, "w")

    # Read Line by line of file
    for line in fp.readlines():
        print line.strip()
        words = line.split(",")
        # print(words)
        turn_around_time_ms = processing_time_ms = response_time_ms = result_code = ""

        try:
            message = words[17].strip()
        except IndexError, e:
            raise Exception(filename + " Index Error : " + line)

        print 'Columns : %s' % (len(words))
        # Check the Word from 18th Position onwards i.e. 17th Index and merge it
        if (len(words) > 22):
            for i in range(18, words.__len__() - 3):
                message = message + "," + words[i].strip()

            # Assign the remaining fields if they exists in the file. If not then null
            try:
                turn_around_time_ms = words[i].strip()
                processing_time_ms = words[i + 1].strip() if (i + 1) <= words.__len__() else ""
                response_time_ms = words[i + 2].strip() if i + 2 <= words.__len__() - 1 else ""
                result_code = words[i + 3].strip() if i + 3 <= words.__len__() - 1 else ""
            except IndexError, e:
                raise "Error : " + line
        else:
            i = 18
            while (i < words.__len__()):
                if is_int(words[i]) or len(words[i].strip()) == 0:
                    break
                else:
                    message = message + "," + words[i].strip()
                i += 1

            # Assign the remaining fields if they exists in the file. If not then null
            try:
                turn_around_time_ms = words[i].strip() if i <= words.__len__() else ""
                processing_time_ms = words[i + 1].strip() if (i + 1) <= words.__len__() else ""
                response_time_ms = words[i + 2].strip() if i + 2 <= words.__len__() - 1 else ""
                result_code = words[i + 3].strip() if i + 3 <= words.__len__() - 1 else ""
            except:
                pass

        # Replace any double quote in the string
        message = message.replace('"', '')
        # print(line)
        new_line = "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,\"%s\",%s,%s,%s,%s\n" % (
            words[0], words[1], words[2], words[3], words[4], words[5], words[6], words[7], words[8], words[9],
            words[10], words[11], words[12], words[13], words[14], words[15], words[16], message, turn_around_time_ms,
            processing_time_ms, response_time_ms, result_code)
        print new_line

        # Open another file to write
        nfp.write(new_line)
        print ''

    fp.close()
    nfp.close()

    # Delete the original file and rename .tmp to the original one and move to build directory
    shutil.move(new_filename, os.path.join(new_file_path, filename))
    os.system("chmod 775 " + os.path.join(new_file_path, filename))
    # os.remove(filename)
    # os.system("rm -f " + filename) # Getting issues with python remove

    file_count += 1
    if file_count_limit == file_count:
        break
