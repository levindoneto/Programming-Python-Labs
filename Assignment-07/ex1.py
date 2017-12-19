s = ['live','long','and','prosper']
t = ['may','the','force','be','with','you']
u = 'They call it a Royale with cheese'.split()
s[1]
print('Line 04:\nType: ', type(s[1]),'\nValue: ', s[1],'\n----------------\n')
t[2:4]
print('Line 05:\nType: ', type(t[2:4]),'\nValue: ', t[2:4],'\n----------------\n')
len(s+t) == len(s) + len(t)
print('Line 06:\nType: ', type(len(s+t) == len(s) + len(t)),'\nValue: ', len(s+t) == len(s) + len(t),'\n----------------\n')
len(u)
print('Line 07:\nType: ', type(len(u)),'\nValue: ', len(u),'\n----------------\n')
s+t[3:8]
print('Line 08:\nType: ', type(s+t[3:8]),'\nValue: ', s+t[3:8],'\n----------------\n')
(s+u)[3:8]
print('Line 09:\nType: ', type((s+u)[3:8]),'\nValue: ', (s+u)[3:8],'\n----------------\n')
len(' '.join(s))
print('Line 10:\nType: ', type(len(' '.join(s))),'\nValue: ', len(' '.join(s)),'\n----------------\n')
len(' '.join(s))
print('Line 11:\nType: ', type(len(' '.join(s))),'\nValue: ', len(' '.join(s)),'\n----------------\n')
'the force' in ' '.join(t)
print('Line 12:\nType: ', type('the force' in ' '.join(t)),'\nValue: ', 'the force' in ' '.join(t),'\n----------------\n')
'the force' in ' '.join(t)
print('Line 13:\nType: ', type('the force' in ' '.join(t)),'\nValue: ', 'the force' in ' '.join(t),'\n----------------\n')
' '.join(s)[:7] + ' '.join(s)[17:]
print('Line 14:\nType: ', type(' '.join(s)[:7] + ' '.join(s)[17:]),'\nValue: ', ' '.join(s)[:7] + ' '.join(s)[17:],'\n----------------\n')
