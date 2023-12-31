income = 50000
single_person_tax_allowance = 25050
taxable_at_15_perecent = income - single_person_tax_allowance
taxable_at_30_perecent = income - taxable_at_15_perecent
percent_tax_15 = taxable_at_15_perecent * .1
percent_tax_30 = taxable_at_30_perecent * .3
total_tax = percent_tax_15 + percent_tax_30
print(total_tax)
