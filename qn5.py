# Customize a coffee order: "Small", "Medium", or "Large" with an option for "Extra shot" of espresso.

order_size = input('Enter the size of coffee: ')
extra_shot = True

if extra_shot:
    order_size = order_size + " Coffee with an extra shot"
else:
    order_size = order_size + " Coffee"

print(f'Your order is {order_size}')