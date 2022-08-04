import shutil
import os

import exceptions

def sort_by_gender(fromDir:str,toDir:str) -> None:
    """
    Sort the images by gender

    :param fromDir: The origin directory (No trailing /)
    :type fromDir: str
    :param toDir: The receiving directory (No trailing /)
    :type toDir: str
    :raise exceptions.SortError: If the data file is invalid
    :return: No return
    :rtype: None
    """
    for file in os.listdir(fromDir):
        if file.endswith(".txt"):
            with open(f"{fromDir}/{file}", "r") as f:
                data = f.readlines()
                gender = data[6]
            if "Male" in gender:
                shutil.move(f"{fromDir}/{file.replace('.txt','.jpg')}", f"{toDir}/{file.replace('.txt','.jpg')}")
            elif "Female" in gender:
                shutil.move(f"{fromDir}/{file.replace('.txt','.jpg')}", f"{toDir}/{file.replace('.txt','.jpg')}")
            else:
                raise exceptions.SortError("Invalid data file")

def sort_to_data(fromDir:str,toDir:str) -> None:
    """
    Sort the images by to the data folder with the percentage of: train 80%, test 10%, val 10%

    :param fromDir: The origin directory (No trailing /)
    :type fromDir: str
    :param toDir: The receiving directory (No trailing /)
    :type toDir: str
    :return: No return
    :rtype: None
    """
    files_f_train = os.listdir(f"{fromDir}/female")
    files_m_train = os.listdir(f"{fromDir}/male")
    for file in files_f_train[:round((len(files_f_train) * 8) / 100)]:
        shutil.move(f"{fromDir}/female/{file}",f"{toDir}/train/female/{file}")
    for file in files_m_train[:round((len(files_m_train) * 8) / 100)]:
        shutil.move(f"{fromDir}/male/{file}",f"{toDir}/train/male/{file}")

    files_f_test = os.listdir(f"{fromDir}/female")
    files_m_test = os.listdir(f"{fromDir}/male")
    for file in files_f_test[:round(len(files_f_test) / 2)]:
        shutil.move(f"{fromDir}/female/{file}",f"{toDir}/test/female/{file}")
    for file in files_m_test[:round(len(files_m_test) / 2)]:
        shutil.move(f"{fromDir}/male/{file}",f"{toDir}/test/male/{file}")
    
    files_f_val = os.listdir(f"{fromDir}/female")
    files_m_val = os.listdir(f"{fromDir}/male")
    for file in files_f_val[:len(files_f_val)]:
        shutil.move(f"{fromDir}/female/{file}",f"{toDir}/val/female/{file}")
    for file in files_m_val[:len(files_m_val)]:
        shutil.move(f"{fromDir}/male/{file}",f"{toDir}/val/male/{file}")
