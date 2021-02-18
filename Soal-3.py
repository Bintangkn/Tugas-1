teori=79
praktek=0
standar=70
if teori >= standar and praktek >= standar:
    print("Selamat, anda lulus!")
elif teori >= standar and standar > praktek:
    print("Anda harus mengulang ujian praktek.")
elif teori < standar and praktek >= standar:
    print("Anda harus mengulang ujian teori.")
elif teori < standar and praktek < standar:
    print("Anda harus mengulang ujian teori dan praktek.")