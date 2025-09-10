def discount(price, disper):
    disamt = price * (disper / 100)
    return price - disamt

def gst(price, gstper=18):
    gstamt = price * (gstper / 100)
    return price + gstamt
def invoice(cart, disper=0, gstper=18):
    print(" INVOICE ")
    subtotal = 0
    for product, price in cart.items():
        print(f"{product:<15}: ₹{price}")
        subtotal += price
    print(f"Subtotal: ₹{subtotal}")

    discounted_total = discount(subtotal, disper)
    print(f"After {disper}% discount: ₹{discounted_total}")

    final_total = gst(discounted_total, gstper)
    print(f"After {gstper}% GST: ₹{round(final_total, 2)}")
    print("Thank you")
