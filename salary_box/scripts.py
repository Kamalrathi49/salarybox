from myapp.models import Company

company_list = [{
  "name": "Edgeblab",
  "founder": "Blakeley Mildmott",
  "headquator": "Mazār-e Sharīf",
  "working": "working",
  "fund_raise": "$680550.66",
}, {
  "name": "Browseblab",
  "founder": "Vittoria Lunn",
  "headquator": "Mafang",
  "working": "close",
  "fund_raise": "$558921.37",
}, {
  "name": "Yakijo",
  "founder": "Alex Pothbury",
  "headquator": "Reno",
  "working": "working",
  "fund_raise": "$263526.55",
}, {
  "name": "Yodoo",
  "founder": "Christiano Bosket",
  "headquator": "Davyd-Haradok",
  "working": "working",
  "fund_raise": "$982123.78",
}, {
  "name": "Topdrive",
  "founder": "Grace Maidens",
  "headquator": "Xiaoguai",
  "working": "close",
  "fund_raise": "$596797.01",
}]

for item in company_list:
    company = Company.objects.create(
        name=item['name'],
        founder=item['description'],
        headquator=item['headquator'],
        fund_raise=item['fund_raise'],
        working=item['working'],
    )
    company.save()

