from pathlib import Path
import tkinter as tk
from tkinter import ttk, messagebox


def format_price(amount):
    """Format numbers cleanly without trailing zeros."""
    return f"{amount:.2f}".rstrip("0").rstrip(".")


class RestaurantOrderManagement:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurant Management App")
        self.root.geometry("800x600")
        self.root.resizable(False, False)

        self.menu_items = {
            "FRIES MEAL": 2,
            "LUNCH MEAL": 2,
            "BURGER MEAL": 3,
            "PIZZA MEAL": 4,
            "CHEESE BURGER": 2.5,
            "DRINKS": 1,
        }

        self.exchange_rate = 82

        self.setup_background(root)

        frame = ttk.Frame(root, padding=15)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        ttk.Label(
            frame,
            text="Restaurant Order Management",
            font=("Arial", 20, "bold"),
        ).grid(row=0, columnspan=3, padx=10, pady=10)

        self.menu_labels = {}
        self.menu_quantities = {}

        for i, (item, price) in enumerate(self.menu_items.items(), start=1):
            label = ttk.Label(
                frame,
                text=f"{item} (${format_price(price)}):",
                font=("Arial", 12),
            )
            label.grid(row=i, column=0, sticky=tk.W, padx=10, pady=5)
            self.menu_labels[item] = label

            quantity_entry = ttk.Entry(frame, width=6, justify=tk.CENTER)
            quantity_entry.grid(row=i, column=1, padx=10, pady=5)
            self.menu_quantities[item] = quantity_entry

        currency_row = len(self.menu_items) + 1
        self.currency_var = tk.StringVar()
        ttk.Label(
            frame,
            text="Currency:",
            font=("Arial", 12),
        ).grid(row=currency_row, column=0, sticky=tk.W, padx=10, pady=5)

        currency_dropdown = ttk.Combobox(
            frame,
            textvariable=self.currency_var,
            state="readonly",
            width=18,
            values=("USD", "INR"),
        )
        currency_dropdown.grid(row=currency_row, column=1, padx=10, pady=5)
        currency_dropdown.current(0)
        self.currency_var.trace_add("write", self.update_menu_prices)

        order_button = ttk.Button(
            frame,
            text="Place Order",
            command=self.place_order,
        )
        order_button.grid(
            row=currency_row + 1,
            columnspan=3,
            padx=10,
            pady=12,
        )

    def setup_background(self, root):
        bg_width, bg_height = 800, 600
        canvas = tk.Canvas(root, width=bg_width, height=bg_height, highlightthickness=0)
        canvas.pack(fill=tk.BOTH, expand=True)

        image_path = Path(__file__).resolve().parent / "foodphoto.jpg"
        if not image_path.exists():
            canvas.configure(bg="#2b2b2b")
            return

        original_image = tk.PhotoImage(file=str(image_path))
        x_factor = max(1, original_image.width() // bg_width)
        y_factor = max(1, original_image.height() // bg_height)
        background_image = original_image.subsample(x_factor, y_factor)

        canvas.create_image(0, 0, anchor=tk.NW, image=background_image)
        # Keep references to both images so neither is garbage-collected
        canvas.original_image = original_image
        canvas.image = background_image

    def get_currency_details(self):
        currency = self.currency_var.get()
        if currency == "INR":
            return "₹", self.exchange_rate
        return "$", 1

    def update_menu_prices(self, *args):
        symbol, rate = self.get_currency_details()
        for item, label in self.menu_labels.items():
            price = self.menu_items[item] * rate
            label.config(text=f"{item} ({symbol}{format_price(price)}):")

    def place_order(self):
        total_cost = 0
        order_lines = []
        symbol, rate = self.get_currency_details()

        for item, entry in self.menu_quantities.items():
            raw_qty = entry.get().strip()
            if not raw_qty:
                continue

            if not raw_qty.isdigit():
                messagebox.showwarning(
                    "Invalid Quantity",
                    f"Please enter a whole number for {item}.",
                )
                return

            quantity = int(raw_qty)
            if quantity > 0:
                price = self.menu_items[item] * rate
                cost = quantity * price
                total_cost += cost
                order_lines.append(
                    f"{item}: {quantity} x {symbol}{format_price(price)} = {symbol}{format_price(cost)}"
                )

        if total_cost > 0:
            summary = "Order Summary:\n" + "\n".join(order_lines)
            summary += f"\n\nTotal Cost: {symbol}{format_price(total_cost)}"
            messagebox.showinfo("Order Placed", summary)
        else:
            messagebox.showerror("Error", "Please order at least one item.")


if __name__ == "__main__":
    root = tk.Tk()
    app = RestaurantOrderManagement(root)
    root.mainloop()