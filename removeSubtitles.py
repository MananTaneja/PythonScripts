import os

folderName = input("Enter the folder name to remove unnecessary subtitles (in downloads folder): ")

folderName.lstrip().rstrip()

path = os.path.join('/home/manantaneja/Downloads', folderName)

os.chdir(path)

for file_name in os.listdir():
    if(file_name.endswith('-es.srt')):
        os.unlink(file_name)
    if(file_name.endswith('-it.srt')):
        os.unlink(file_name)
    if(file_name.endswith('-ja.srt')):
        os.unlink(file_name)
    if(file_name.endswith('-pt.srt')):
        os.unlink(file_name)
    if(file_name.endswith('-tr.srt')):
        os.unlink(file_name)
        