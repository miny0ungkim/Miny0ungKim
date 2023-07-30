import requests
from bs4 import BeautifulSoup
import csv


fd=open("fin.csv","w", encoding="utf-8-sig", newline="") 
writer = csv.writer(fd)
field_header = "N	종목명	현재가	전일비	등락률	액면가	거래량	상장주식수	시가총액	외국인비율	PER	ROE	토론실".split("\t")
writer.writerow(field_header)


for i in range(1,10+1):
  url = f"https://finance.naver.com/sise/field_submit.naver?menu=market_sum&returnUrl=http%3A%2F%2Ffinance.naver.com%2Fsise%2Fsise_market_sum.naver%3F%26page%3D{i}&fieldIds=quant&fieldIds=market_sum&fieldIds=per&fieldIds=roe&fieldIds=frgn_rate&fieldIds=listed_stock_cnt"
  res = requests.get(url)
  soup = BeautifulSoup(res.text, "lxml")
  items = soup.find_all("tr", attrs={"onmouseover":"mouseOver(this)"})
  for item in items:
    cols = item.find_all("td")
    col_list = []
    for col in cols:
      col_list.append(col.get_text().strip()) #탭
    writer.writerow(col_list)



import uvicorn
#파싱

app= FastAPI() #생성
@app.get("\") 
def read_root():
  url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%ED%99%8D%EC%A7%80%EB%8F%99+%EB%82%A0%EC%94%A8&oquery=%EB%84%A4%EC%9D%B4%EB%B2%84+%EB%82%A0%EC%94%A8&tqi=i6%2Brldp0YiRssTdiMgdssssssew-034124"
  res = requests.get(url)
  soup = BeautifulSoup(res.text)
  dong = soup.find("div", attrs = {"class":""}).find("h2")
  tmp = soup.find("div", attrs = {"class":""}.get_text()
  min_max = soup.find("span", attrs = {"class":"temerature_inner"}).get_text()
  print(dong)
  print(tmp)
  print(min)
  return dong, tmp, min)max

if __name__ == '__main__':
         uvicorn.run(app)