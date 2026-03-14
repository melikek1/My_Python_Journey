# A robust function to calculate discounts with strict Input Validation.
# Uses isinstance() to ensure data types are correct and implements 
# Early Exit (return) to prevent system crashes on invalid inputs.

def apply_discount(price, discount):
    # 1. Check if price is a number
    if not isinstance(price, (int, float)):
        return "The price should be a number"

    # 2. Check if discount is a number
    if not isinstance(discount, (int, float)):
        return "The discount should be a number"

    # 3. Check price bounds
    if price <= 0:
        return "The price should be greater than 0"

    # 4. Check discount bounds (0 is allowed)
    if discount < 0 or discount > 100:
        return "The discount should be between 0 and 100"

    # 5 & 6. Calculate and return final price
    discount_amount = price * (discount / 100)
    final_price = price - discount_amount
    
    return final_price
