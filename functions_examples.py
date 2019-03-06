#   play with this some more later
#
company_rates = {
    'google': 400,
    'amazon': 380,
    'facebook': 350
}
hours_worked = {
    'google': 6,
    'amazon': 10,
    'facebook': 4
}
total_pay = 0
for company_name in company_rates.keys():
    hourly_rate = company_rates[company_name]
    hours = hours_worked[company_name]
    company_total_pay = hourly_rate * hours
    print(f)
# ----------
#     