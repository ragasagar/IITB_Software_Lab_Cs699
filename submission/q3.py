import glob
import os
import shutil
import sys


def function_q3(inp_file_path, out_folder_path):
    """
    Function function_q3 searches in a directory for text files , it compares every pair of files and if a pair is found where lines of one file are reversed as compared to other file than it moves both the files in output directory.

    :param inp_file_path: input_path is the relative path of input folder containing various text files
    :type inp_file_path: str
    :param out_folder_path: output_path is the raltive path of output folder where all the pairs are moved to which have line reversed compared to each other 
    :type out_folder_path: str
    """
    if os.path.isdir(out_folder_path):
        os.rename(out_folder_path, "test")
        shutil.rmtree("test")

    os.mkdir(out_folder_path)
    files = glob.glob(os.path.join(inp_file_path, '*.txt'))
    filestemp = files

    for file1 in filestemp:
        for file3 in filestemp:
            if(file1 == file3):
                continue
            tempfile1 = open(file3, "r")
            tempfile2 = open(file1, "r")
            k = tempfile1.readlines()
            t = reversed(k)
            q = tempfile2.readlines()
            list1 =[x.rstrip().lstrip().strip('\n')  for x in t]
            list2 = [x.rstrip().lstrip().strip('\n') for x in q]
            tempfile1.close()
            tempfile2.close()
            if(list1 == list2):
                shutil.move(file1, out_folder_path)
                shutil.move(file3, out_folder_path)
                filestemp.remove(file1)
                filestemp.remove(file3)

                break


if __name__ == '__main__':
    ''''''
    # inp_file_path = "./testcases/q3/input/"
    # out_folder_path = "./testcases/q3/output/"
    # inp_file_path = sys.argv[1]
    # out_folder_path = sys.argv[2]
    # function_q3(inp_file_path, out_folder_path)
