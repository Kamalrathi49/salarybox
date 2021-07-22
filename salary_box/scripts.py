from myapp.models import Company
company_list = [
  {
    'name' : 'salarybox1',  
    'founder': 'piyush goyal',
    'headquator' : 'Gurugram',
    'fund_raise' : '2B',
    'working' : 'close' 
  },
    {
    'name' : 'TutorBin',
    'founder': 'parkash jha',
    'headquator' : 'Gurugram',
    'fund_raise' : '2B',
    'working' : 'close' 
  }

]
for item in company_list:
    print('->', item)
    c = Company.objects.create(
        name=item['name'],
        founder=item['founder'],
        headquator=item['headquator'],
        fund_raise=item['fund_raise'],
        working=item['working'],
    )
    c.save()


