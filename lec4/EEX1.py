
print("---------------")
print("KPH\rMPH")
print("---------------")
for KPH in range(60,130,10):
   MPH = KPH*0.6214
print(KPH, "\t",format(MPH,".1f"))