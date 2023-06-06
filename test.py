try:
    import subprocess
except ImportError:
    print("\n  installing subprocess!...\n")
    os.system("pip install subprocess")


test = subprocess.check_output('getprop ro.product.cpu.abilist',shell=True).decode('utf-8').replace('\n','')

print(test)
