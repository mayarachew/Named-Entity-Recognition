"""Adapt fields."""
import re

def define_data_values(key: str, value: str) -> str:
  data_value = value.strip()
    
  if value:
    # Date adapter output      
    if key == 'date':
      data_value = re.sub('[\d.]*[:][\d]*', '', data_value)
      data_value = re.sub('[Dd][Aa][Tt][Ee][:]*', '', data_value)
      if '/' in data_value or '-' in data_value:
        data_value = re.findall("[\d]*[\/-][\d]*[\/-]*[\d]*", data_value)[0]
      data_value = data_value.replace('PM', '').replace('AM', '')
    
    # Total adapter output 
    if key == 'total':
      if data_value:
        regex = re.search('[RM]*[ ]*[\\w]*([\\.|\\,]\\d\\d)', data_value)
        data_value = "" if regex is None else regex[0]
      else:
          data_value = ""
      data_value = data_value.replace('N', 'M').replace(' ', '')
      
    data_value = data_value.replace('\n',' ').strip()
  return data_value

def fields_adapt(company: str, address: str, total: str, date: str) -> dict:
    """Adapt fields to output dict
    Args:
        company (str): company name
        address (str): company address
        total (str): receipt total value
        date (str): receipt date
    Returns:
        data (dict): dictionary that contains all information
    """

    data = {}
    data['company'] = define_data_values('company', company)
    data['address'] = define_data_values('address', address)
    data['total'] = define_data_values('total', total)
    data['date'] = define_data_values('date', date)

    return data