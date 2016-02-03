import os
import re

rootdir = '/home/ptbooks/dzs'

for subdir,dirs,files in os.walk(rootdir):
	for file in files:
		m = re.match('.*[.]md$',file)
		if m == None:
			continue
		fn = subdir + '/' + file;
		os.rename(fn,fn+'.orig')
		f=open(fn+'.orig','r')
		w=open(fn,'w')
		lines=f.readlines()
		pattern=re.compile(r'(https?[:][/][/][^\'\"<]*[.])md([\'\"])')
		for line in lines:
			newline=pattern.sub(r'\1.md\2',line)
			w.write(newline)
		f.close()
		w.close()

