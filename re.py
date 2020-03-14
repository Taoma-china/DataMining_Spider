import re

pattern = re.compile('\d+\.+\d')


src = "3.14 124.123 212 213 421"

result=pattern.findall(src)
print result
