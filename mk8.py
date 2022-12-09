import platform
import os
os.system('termux-setup-storage')
os.system('rm -rf mk8')
os.system('git pull')
try:os.mkdir('/sdcard/OK')
except:pass
try:os.mkdir('/sdcard/CP')
except:pass
try:os.system('touch .proxy.txt')
except:pass
arc = str(platform.uname().machine)
if 'arm' in arc:
	__import__("latter")._site_view_()
elif 'aarch' in arc:
	__import__("mk8").linex()
else:
	exit(f' Unknow device machine {arc}')
