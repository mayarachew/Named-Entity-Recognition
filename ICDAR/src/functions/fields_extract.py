"""Extract most important fields from the receipt text."""
import re
from typing import Tuple

def fields_extract(text: str) -> Tuple[str, str, str, str]:
    """Extract fields (company, address, total, date) from text
    Args:
        text (str): original text extracted from receipt image
    Returns:
        company (str): company name
        address (str): company address
        total (str): receipt total value
        date (str): receipt date
    """

    # Transform text to upper case
    text = text.upper()
    
    company = ""
    address = ""
    total = ""
    date = ""
    # get_total = False

    for row in text.split('\n'):
        # Get company name
        if ('BHD' in row or 'RESTAURANT' in row or 'HARDWARE' in row or 'ENTERPRISE' in row or 'RESTORAN' in row or 'S/B' in row or 'PHARMACY' in row) and not company:
            company = row

        # Get total value
        numerical_row = re.search('[\d][,|.]', row)
        # if '^([T][O][T][A][L])' in row and numerical_row:
        #     total = row
        #     get_total = True
        # if ('DUE' in row or 'BUE' in row) and numerical_row and not total and not get_total:
        #     total = row
        if ('TOTAL' in row or 'RM' in row or 'DUE' in row or 'BUE' in row) and numerical_row and not total:
            total = row

        # Get time value
        time_row = re.search('[\d][\d][\/|-][\w][\w][\w]*[\/|-][\d]*', row)
        if time_row:
            date = row
        time_row = re.search('[D][A|U][T][E]', row)
        if time_row and not date:
            date = row
        time_row = re.search('[\d][\d]\:[\d][\d]', row)
        if time_row and not date:
            date = row

    # If company not found, get the first line
    if not company:
        company = text.strip().split('\n')[0]

    # Get company address
    end_address_string = 'TEL' if 'TEL' in text else 'TAX' if 'TAX' in text else 'JAX'
    if end_address_string in text:
        if ')' in text:
            address = text[text.index(')')+len(')'):text.index(end_address_string)]
        if address == '' and company:
            address = text[text.index(company)+len(company):text.index(end_address_string)]
    else:
        address = ''

    return company, address, total, date