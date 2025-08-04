import subprocess

def safe_remove_driver(inf_name):
    subprocess.run(["pnputil", "/delete-driver", inf_name, "/uninstall", "/force"], shell=True)
