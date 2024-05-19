import hashlib
import sys


def calculate_md5(file_path):

    md5_hash = hashlib.md5()

    try:
        with open(file_path, 'rb') as file:
            for chunk in iter(lambda: file.read(4096), b''):
                md5_hash.update(chunk)

        md5_digest = md5_hash.hexdigest()

        return md5_digest
    except FileNotFoundError:
        print(f"Error: Path-i për file-n '{file_path}' që keni shënuar nuk u gjet.")
        sys.exit(1)
    except PermissionError:
        print(f"Error: Nuk keni të drejtë për tu qasur në këtë file: '{file_path}'.")
        sys.exit(1)
    except:
        print("Kemi hasur probleme gjatë leximit të file-s")
        sys.exit(1)

def calculate_sha256(file_path):

    sha256_hash = hashlib.sha256()

    try:
        with open(file_path, 'rb') as file:
            for chunk in iter(lambda: file.read(4096), b''):
                sha256_hash.update(chunk)

        sha256_digest = sha256_hash.hexdigest()

        return sha256_digest
    except FileNotFoundError:
        print(f"Error: Path-i për file-n '{file_path}' që keni shënuar nuk u gjet.")
        sys.exit(1)
    except PermissionError:
        print(f"Error: Nuk keni të drejtë për tu qasur në këtë file: '{file_path}'.")
        sys.exit(1)
    except:
        print("Kemi hasur probleme gjatë leximit të file-s")
        sys.exit(1)

def print_banner(file_name):
    banner = f"""
====================================
File Integrity Checker
====================================
Kalkulimet për: {file_name}
====================================
"""
    print(banner)

def print_help():
    help_message = """
    
Përdorimi: python <path_1> <path_2>

Argumentet:
  path_1    Path-i për skriptin për të ekzekutuar.
  path_2    Path-i për file-n për të cilin do të llogariten shenjat MD5 dhe SHA-256.

Shembull:
  python ./.venv/FileIntegrityChecker.py ./.venv/file.txt
  
"""
    print(help_message)

