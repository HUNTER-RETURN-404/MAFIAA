# Compiled By Mr Mafia | Muhammad Muzammil
# Github :  https://github.com/Muzammil-404

import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("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"))))
