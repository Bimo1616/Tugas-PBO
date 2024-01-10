from matakuliah import matakuliah

# Update Data
a = matakuliah()
kodemk = '11100'
a.namamk = "trinil"
a.sks = "4"
a.updateBykodemk(kodemk)
b = a.getAllData()
print(b)
