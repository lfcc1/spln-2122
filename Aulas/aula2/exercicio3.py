from sys import argv
import subprocess

result = subprocess.run(f"cat {argv[1] if len(argv) > 1 else '-'} | nl | head -n 50 | tail -n 11", shell=True)
print(result)
