def process_payment(amount, currency):
    assert isinstance(amount, (int, float)), "Amount must be numeric"
    assert amount > 0, "Amount must be positive"
    assert currency in ("USD", "BRL", "EUR"), "Invalid currency"

    print(f"Processing {amount} {currency}")


process_payment(100, "USD")   
process_payment(-50, "USD")    
process_payment("100", "USD")  