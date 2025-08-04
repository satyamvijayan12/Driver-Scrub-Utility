import subprocess

def create_restore_point():
    subprocess.run([
        'powershell',
        'Checkpoint-Computer -Description "DriverScrub Restore Point" -RestorePointType "MODIFY_SETTINGS"'
    ])
