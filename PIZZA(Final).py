import tkinter as tk
from tkinter import messagebox
PIZZA_PRICES = {"Small": 8, "Medium": 10, "Large": 12}
TOPPING_PRICE = 1.5
class HotAndReadyApp:
    """Main application class for Hot and Ready Pizza Ordering.""" 
    def __init__(self, root):
        self.root = root
        self.root.title("Hot and Ready")
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack()
        self.address_entry = None
        self.size_var = None
        self.toppings = None
        self.quantity_var = None
        self.create_welcome_screen()
    def create_welcome_screen(self):
        """Create the welcome screen with navigation buttons."""
        self.clear_screen()
        tk.Label(self.main_frame, text="Welcome to Hot and Ready!", font=("Arial", 16)).pack(pady=10)    
        tk.Button(self.main_frame, text="Start Order", command=self.create_order_screen, width=15).pack(pady=5)
        tk.Button(self.main_frame, text="Exit", command=self.root.quit, width=15).pack(pady=5)
    def create_order_screen(self):
        """Create the order screen where users can select pizza details."""
        self.clear_screen()
        tk.Label(self.main_frame, text="Enter Delivery Address:", font=("Arial", 12)).pack()
        self.address_entry = tk.Entry(self.main_frame, width=30)
        self.address_entry.pack(pady=5)
        tk.Label(self.main_frame, text="Choose Pizza Size:", font=("Arial", 12)).pack()
        self.size_var = tk.StringVar(value="Medium")  
        for size in PIZZA_PRICES.keys():
            tk.Radiobutton(self.main_frame, text=size, variable=self.size_var, value=size).pack()
        tk.Label(self.main_frame, text="Select Toppings:", font=("Arial", 12)).pack()
        self.toppings = {"Pepperoni": tk.BooleanVar(), "Mushrooms": tk.BooleanVar()}
        for topping in self.toppings:
            tk.Checkbutton(self.main_frame, text=topping, variable=self.toppings[topping]).pack()
        tk.Label(self.main_frame, text="How Many Pizzas?", font=("Arial", 12)).pack()
        self.quantity_var = tk.StringVar(value="1")
        self.quantity_spinbox = tk.Spinbox(self.main_frame, from_=1, to=10, textvariable=self.quantity_var, width=5)
        self.quantity_spinbox.pack(pady=5)
        tk.Button(self.main_frame, text="Next", command=self.create_summary_screen, width=10).pack(pady=5)
        tk.Button(self.main_frame, text="Back", command=self.create_welcome_screen, width=10).pack(pady=5)
    def create_summary_screen(self):
        """Create the summary screen displaying order details and total cost."""
        if not self.address_entry.get().strip():
            messagebox.showerror("Input Error", "Delivery address cannot be empty!")
            return
        self.clear_screen()
        address = self.address_entry.get
        size = self.size_var.get()
        toppings_selected = [t for t, var in self.toppings.items() if var.get()]
        quantity = int(self.quantity_var.get())
        base_price = PIZZA_PRICES[size]
        topping_cost = len(toppings_selected) * TOPPING_PRICE
        total_cost = (base_price + topping_cost) * quantity
        
        order_details = f"Address: {address}\nSize: {size}\nToppings: {', '.join(toppings_selected) if toppings_selected else 'None'}\nQuantity: {quantity}\nTotal: ${total_cost:.2f}"
        tk.Label(self.main_frame, text="Order Summary", font=("Arial", 16)).pack(pady=5)
        tk.Label(self.main_frame, text=order_details, font=("Arial", 12), justify="left").pack(pady=5)
        tk.Button(self.main_frame, text="Confirm Order", command=self.create_confirmation_screen, width=15).pack(pady=5)
        tk.Button(self.main_frame, text="Back", command=self.create_order_screen, width=15).pack(pady=5)
    def create_confirmation_screen(self):
        """Display the confirmation screen with the order details."""
        self.clear_screen()
        tk.Label(self.main_frame, text="Order Confirmed!", font=("Arial", 16), fg="green").pack(pady=10)
        tk.Label(self.main_frame, text="Your pizza is on the way!", font=("Arial", 12)).pack(pady=5)
        tk.Button(self.main_frame, text="Place Another Order", command=self.create_order_screen, width=20).pack(pady=5)
        tk.Button(self.main_frame, text="Exit", command=self.root.quit, width=20).pack(pady=5)
    def clear_screen(self):
        """Clear all widgets in the current screen."""
        for widget in self.main_frame.winfo_children():
            widget.destroy()
# Run  Application
if __name__ == "__main__":
    root = tk.Tk()
    app = HotAndReadyApp(root)
    root.mainloop()
