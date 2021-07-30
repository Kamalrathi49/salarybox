from myapp.models import Company

company_list = [{
  "name": "Google",
  "founder": "Larry Page",
  "headquator": "Hong Kong",
  "working": "working",
  "fund_raise": "$6805504336",
},
{
  "name": "Apple",
  "founder": "Steve Jobs",
  "headquator": "California",
  "working": "working",
  "fund_raise": "$6805533066",
},
{
  "name": "Tesla",
  "founder": "Nicolas Tesla",
  "headquator": "New York",
  "working": "working",
  "fund_raise": "$6805340",
},
{
  "name": "Nokia",
  "founder": "Fredrek Idestam",
  "headquator": "London",
  "working": "working",
  "fund_raise": "$680325340",
},]

for item in company_list:
    company = Company.objects.create(
        name=item['name'],
        founder=item['founder'],
        headquator=item['headquator'],
        fund_raise=item['fund_raise'],
        working=item['working'],
    )
    company.save()

