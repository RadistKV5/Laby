disk_capacity_mb = 1.44
pages = 100
strings = 50
digits = 25
bytes_per_digit = 4
bytes_per_book = bytes_per_digit * digits * strings * pages
kb_per_book = bytes_per_book / 1024
disk_capacity_kb = disk_capacity_mb * 1024
a = int(disk_capacity_kb/kb_per_book)
print("Количество книг, помещающихся на дискету:", a)
