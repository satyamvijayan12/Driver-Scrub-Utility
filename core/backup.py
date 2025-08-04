import shutil
import os

def backup_inf(inf_name):
    source = os.path.join("C:\\Windows\\INF", inf_name)
    target_dir = "backups"
    os.makedirs(target_dir, exist_ok=True)
    target = os.path.join(target_dir, inf_name)
    if os.path.exists(source):
        shutil.copyfile(source, target)
