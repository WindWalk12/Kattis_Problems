megabytes = int(input())
months = int(input())
megabytesBack = megabytes

for i in range(months):
    a = int(input())
    megabytesBack -= a
    megabytesBack += megabytes

print(megabytesBack)