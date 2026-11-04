
# Shopping Cart System
# Python 3

# Product catalogue
products = {
    "Pen": 10,
    "Notebook": 50,
    "Bag": 500
}

# Shopping cart
cart = {}


def view_products():
    print("\n--- Available Products ---")
    for name, price in products.items():
        print(f"{name}: Rs.{price}")


def add_to_cart():
    view_products()

    name = input("\nEnter product name: ").strip().title()

    if name not in products:
        print("Invalid product.")
        return

    try:
        quantity = int(input("Enter quantity: "))

        if quantity < 1:
            print("Quantity must be at least 1.")
            return

    except ValueError:
        print("Please enter a valid integer quantity.")
        return

    cart[name] = cart.get(name, 0) + quantity

    print(f"{name} x{quantity} added to cart.")
    print(f"Cart subtotal: Rs.{get_subtotal()}")


def remove_from_cart():
    if not cart:
        print("Cart is empty.")
        return

    view_cart()

    name = input("\nEnter product name to remove: ").strip().title()

    if name not in cart:
        print("Product not found in cart.")
        return

    del cart[name]
    print(f"{name} removed from cart.")


def get_subtotal():
    return sum(
        products[name] * quantity
        for name, quantity in cart.items()
    )


def view_cart():
    print("\n--- Shopping Cart ---")

    if not cart:
        print("Cart is empty.")
        return

    for name, quantity in cart.items():
        amount = products[name] * quantity
        print(f"{name} x{quantity} = Rs.{amount}")

    print(f"Subtotal: Rs.{get_subtotal()}")


def checkout():
    if not cart:
        print("Cart is empty.")
        return

    subtotal = get_subtotal()

    discount = subtotal * 0.10 if subtotal > 500 else 0
    taxable_amount = subtotal - discount
    gst = taxable_amount * 0.18
    grand_total = taxable_amount + gst

    print("\n--- Final Bill ---")
    view_cart()
    print(f"Discount: Rs.{discount:.2f}")
    print(f"GST (18%): Rs.{gst:.2f}")
    print(f"Grand Total: Rs.{grand_total:.2f}")


def main():
    while True:
        print("\n===== SHOPPING CART SYSTEM =====")
        print("1. View Products")
        print("2. Add to Cart")
        print("3. Remove from Cart")
        print("4. View Cart")
        print("5. Checkout")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_products()
        elif choice == "2":
            add_to_cart()
        elif choice == "3":
            remove_from_cart()
        elif choice == "4":
            view_cart()
        elif choice == "5":
            checkout()
        elif choice == "6":
            print("Thank you for shopping!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
