from datetime import datetime
from pathlib import Path
import os
import zipfile
import posixpath


def backup_wizard(disk, user):
    
    unit = disk
    folder = ":\My_Backups"
    backup_directory  = unit + folder
    backup_directory.replace(os.sep, posixpath.sep)

    user_name = user
    path_to_backup = "C:\\User\\" + user_name + "\\Desktop\\Backups"
    path_to_backup.replace(os.sep, posixpath.sep)

    max_backup_amount = 3

    object_to_backup_path = Path(path_to_backup)
    backup_directory_path = Path(backup_directory)

    backup_directory_path.mkdir(parents = True, exist_ok = True)

    existing_backups = [
        i for i in backup_directory_path.iterdir()
        if i.is_file() and i.suffix == ".zip" and i.name.startswith('backup-')
    ]

    oldest_to_newest_backup_by_name = list(sorted(existing_backups, key=lambda f: f.name))
    while len(oldest_to_newest_backup_by_name) >= max_backup_amount:
        backup_to_delete = oldest_to_newest_backup_by_name.pop(0)
        backup_to_delete.unlink()


    backup_file_name = f'backup-{datetime.now().strftime("%Y%m%d%H%M%S")}-{object_to_backup_path.name}.zip'
    zip_file = zipfile.ZipFile(str(backup_directory_path / backup_file_name), mode='w')
    if object_to_backup_path.is_file():
        zip_file.write(
            object_to_backup_path.absolute(),
            arcname = object_to_backup_path.name,
            compress_type = zipfile.ZIP_DEFLATED
        )
    elif object_to_backup_path.is_dir():
        for file in object_to_backup_path.glob('**/*'):
            if file.is_file():
                zip_file.write(
                    file.absolute(),
                    arcname = str(file.relative_to(object_to_backup_path)),
                    compress_type = zipfile.ZIP_DEFLATED
                )

    zip_file.close()