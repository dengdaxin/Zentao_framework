import os
import zipfile

def zip(zip_file_name,file_name):
    with zipfile.ZipFile(zip_file_name,mode= 'w',compression=zipfile.ZIP_DEFLATED) as zf:
        for i in file_name:
            parent_path,name = os.path.split(i)
            zf.write(i,arcname=name)

zip_name = '../report/report.zip'