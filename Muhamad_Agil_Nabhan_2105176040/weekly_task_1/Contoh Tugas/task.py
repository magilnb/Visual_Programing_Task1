class MyClass:
    def __init__(self, parameter1, parameter2, parameter3, parameter4, parameter5, parameter6):
        self.attribute1 = parameter1
        self.attribute2 = parameter2
        self.attribute3 = parameter3
        self.attribute4 = parameter4
        self.attribute5 = parameter5
        self.attribute6 = parameter6

objek1 = MyClass("Muhamad Agil Nab'han", "B 2021", "Pendidikan Komputer", "Fakultas Keguruan dan Ilmu Pendidikan", "Jalan Kedondong Dalam 5", "Kabupaten Paser")

print("Biodata Diri:")
print("Nama:", objek1.attribute1)
print("Kelas:", objek1.attribute2)
print("Prodi:", objek1.attribute3)
print("Fakultas:", objek1.attribute4)
print("Tempat Tinggal:", objek1.attribute5)
print("Asal:", objek1.attribute6)