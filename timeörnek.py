from datetime import datetime

pazarsayisi=0

for yil in range(1901,2022):
    for ay in range(1,13):
        if datetime(yil,ay,1).isoweekday()==7:
            pazarsayisi+=1

print(pazarsayisi)
