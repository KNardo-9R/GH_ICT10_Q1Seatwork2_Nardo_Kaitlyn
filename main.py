from pyscript import display

brand_name = 'SINGSONG EATERIES' # string
owner_name = 'Kaitlyn Nardo' # string
year_established= 2025 # integer 
has_delivery = True # boolean
popular_item_price = 200 # integer
product_names = ['Adobong Mani','Taho','Omelet','Sinigang','Sisig'] # list
business_hours_opening = 8 # integer
business_hours_closing = 12 # integer 
menu_prices = ['₱120','₱20','₱240','₱300','₱367'] # list 
common_allergens = ['Peanuts','Soybeans','Egg', 'Milk']  #   list 
tax_rate = 12.00 # float

display(f'{brand_name}', target='brand')
display(f'OWNER: {owner_name}', target='owner')
display(f'Operating Since {year_established}', target='year')
display(f'Popular Item Price: ₱{popular_item_price}', target='price')
display(f'Product Names: {product_names[0]}', target='product')
display(f'Menu Prices: {menu_prices[2]}', target='menu')
display(f'Common Allergens In Our Food: {common_allergens[0]}',target='allergens')
display(f'Our Tax Rate: {tax_rate}%', target='taxrate')
display(f'DELIVERY ACCEPTED: {has_delivery}', target='delivery')
display(f'OPENING & CLOSING TIMES: {business_hours_opening}AM-{business_hours_closing}PM', target='times')