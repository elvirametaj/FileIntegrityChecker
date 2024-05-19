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

