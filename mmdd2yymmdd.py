'''
Created on Mar 6, 2019

  # Date Received (R)  Date in host (H)  Next Day in host (N)   RESULT  ACTION
  - -----------------  ----------------  --------------------   ------  ------
  1 (03)1230           031230             (03)1231              R<H     YY = YY of N
  2 (03)1231           031230             (03)1231              R=H     YY = YY of N
  3 (03)1230           031231             (04)0101              R>H     YY = YY of N - 1
  4 (03)1231           031231             (04)0101              R>H     YY = YY of N - 1
  5 (04)0101           031231             (04)0101              R=H     YY = YY of N
  6 (03)1231           040101             (04)0102              R>H     YY = YY of N - 1
  7 (04)0101           040101             (04)0102              R<H     YY = YY of N

@author: hwase0ng
'''
from datetime import date, datetime, timedelta


def getToday(fm="%Y%m%d"):
    return datetime.today().strftime(fm).replace("-", "")


def getNextDay(pdate):
    return getDayOffset(pdate, 1)


def getDayOffset(pdate, offset):
    pyyyy = int(pdate[:4])
    pmm = int(pdate[4:6])
    pdd = int(pdate[6:8])
    try:
        result = date(pyyyy, pmm, pdd) + timedelta(days=offset)
    except Exception, e:
        return str(e)
    result = str(result).replace("-", "")
    return result


def mmdd2yymmdd(mmddR, dateH=getToday()):
    dateN = getNextDay(dateH)
    yyN = dateN[:4]
    mmddN = dateN[4:]
    yyR = int(yyN) - 1 if mmddR > mmddN else int(yyN)
    yyR = "{:04d}".format(yyR)
    dateR = yyR[2:] + mmddR
    print(mmddR, dateH[2:], mmddN, dateR)
    return dateR


if __name__ == '__main__':
    yymmddR = mmdd2yymmdd("1230", "20031230")
    yymmddR = mmdd2yymmdd("1231", "20031230")
    yymmddR = mmdd2yymmdd("1230", "20031231")
    yymmddR = mmdd2yymmdd("1231", "20031231")
    yymmddR = mmdd2yymmdd("0101", "20031231")
    yymmddR = mmdd2yymmdd("1231", "20040101")
    yymmddR = mmdd2yymmdd("0101", "20040101")
