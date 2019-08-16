import os
import glob
import shutil


def pptx_copy(src_directory=".", dst_directory="."):
    counter = 0
    for src_file in glob.glob(src_directory + os.sep + '**/*.ppt*', recursive=True):
        dst_file = dst_directory + os.sep + os.path.basename(src_file)
        try:
            shutil.copyfile(src_file, dst_file)
            counter +=1
        except shutil.SameFileError:
            print("Source and Destination are same !!!")
            break
        except:
            print("Un known Error in copying!!!")
    print(f"{counter} file(s) copied.")
    return counter


if __name__ == "__main__":
    pptx_copy(r"/Users/vsiddaia/Downloads/", r"./CyberSecurity-Notes")
    #pptx_copy(r"/Users/vsiddaia/Downloads/", r"/Users/vsiddaia/Downloads/")
