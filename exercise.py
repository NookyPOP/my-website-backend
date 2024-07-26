import datetime
import dateutil

exp = "2024-07-27 15:02:34.968090+00:00"

print(int(dateutil.parser.isoparse(exp).timestamp() * 100000))
