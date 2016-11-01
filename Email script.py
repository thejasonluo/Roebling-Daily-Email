#imports
import smtplib
import quandl
import time
quandl.ApiConfig.api_key = 'G9vB9WQEttApnxDw6Dx2'


#INDEXES
sp = quandl.get("YAHOO/INDEX_GSPC")
sp_latest = "{:,.2f}".format(sp['Adjusted Close'].iloc[-1])
nasdaq = quandl.get("NASDAQOMX/COMP")
nasdaq_latest = "{:,.2f}".format(nasdaq['Dividend Market Value'].iloc[-1])
dow = quandl.get("BCB/UDJIAD1")
dow_latest = "{:,.2f}".format(dow['Value'].iloc[-1])
nikkei = quandl.get("nikkei/ALL_STOCK")
nikkei_latest = "{:,.2f}".format(nikkei['Close'].iloc[-1])

#COMMODITIES
wti = quandl.get("CHRIS/CME_CL1")
wti_latest = "{:,.2f}".format(wti['Settle'].iloc[-1])
brent = quandl.get("CHRIS/ICE_B1")
brent_latest = "{:,.2f}".format(brent['Settle'].iloc[-1])
gold = quandl.get("LBMA/gold")
gold_latest = "{:,.2f}".format(gold['USD (AM)'].iloc[-1])
silver = quandl.get("LBMA/silver")
silver_latest = "{:,.2f}".format(silver['USD'].iloc[-1])

#SECTORS
effective_rate = quandl.get("FRED/DFF")
effective_rate_latest = "{:,.2f}".format(effective_rate['VALUE'].iloc[-1])

#CURRENCIES
usd_eur = quandl.get("CURRFX/usdeur")
usd_eur_latest = "{:,.2f}".format(usd_eur['Rate'].iloc[-1])
jpy_usd = quandl.get("CURRFX/usdjpy")
jpy_usd_latest = "{:,.2f}".format(jpy_usd['Rate'].iloc[-1])
usd_GBP = quandl.get("CURRFX/usdGBP")
usd_GBP_latest = "{:,.2f}".format(usd_GBP['Rate'].iloc[-1])

#INTEREST RATES
effective_rate = quandl.get("FRED/DFF")
effective_rate_latest = "{:,.2f}".format(effective_rate['VALUE'].iloc[-1])

#DATE
date = time.strftime("%b %d, %Y")

from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

#replace with email
fromaddr ="roeblingquants@gmail.com"
toaddr = "thejasonluo@gmail.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "[Roebling Group] Daily Update [%s]" % (date)

html = """\
<html>
   <div><span style="text-decoration: underline;"><strong>Indexes</strong></span></div>
   <div>S&P 500: {sp_latest} </div>
   <div>NASDAQ: {nasdaq_latest} </div>
   <div>Dow Jones Industrial Average: {dow_latest}</div>
   <div>Nikkei 225: {nikkei_latest}</div>
   <div> </div>
   <br> </br>
   <div><span style="text-decoration: underline;"><strong>Currencies</strong></span></div>
   <div>EURO/USD: {usd_eur_latest}</div>
   <div>GBP/USD: {usd_GBP_latest}</div>
   <div>USD/JPY: {jpy_usd_latest}</div>
   <div> </div>
   <br> </br>
   <div><span style="text-decoration: underline;"><strong>Commodities</strong></span></div>
   <div>WTI: {wti_latest}</div>
   <div>Brent: {brent_latest}</div>
   <div>Gold: {gold_latest}</div>
   <div>Silver: {silver_latest}</div>
   <div> </div>
   <br> </br>
   <div><span style="text-decoration: underline;"><strong>Interest Rates</strong></span></div>
   <div>Effective: {effective_rate_latest} </div>
</html>
""".format(**locals())

msg.attach(MIMEText(html, 'html'))

#replace "" with password in server.login(fromaddr, "")
server  = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "thequantgroup")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit
