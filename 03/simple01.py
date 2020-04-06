import re

m = re.match('www','www.santostang.com');

print('match result:',m);

print('match start and end:',m.span());

print('match start position:',m.start());

print('match end position:',m.end());
