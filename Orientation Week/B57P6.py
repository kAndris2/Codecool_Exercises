kor = int(input("Add meg a korodat: \n"))
ret = int(input("Hány évesen akarsz nyugdíjba menni? \n"))

import datetime
c_Year = datetime.datetime.now()
ret_year = ret - kor + c_Year.year
print("Te majd '" + str(ret_year - c_Year.year) + "' év múlva mehetsz nyugdíjba. (" + str(ret_year) + ")")