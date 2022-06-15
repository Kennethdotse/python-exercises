ostr = 'X-DSPAM-Confidence:0.8475'
idx = ostr.find(":")
a = ostr[19:]
num = float(a)
print(num)
