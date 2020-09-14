install:
	[ -d /usr/local/bin ] && cp csv2json.py /usr/local/bin/csv2json || cp csv2json.py /usr/bin/csv2json

uninstall:
	[ ! -z `which csv2json` ] && rm `which csv2json`