class ShoppingCart:
    def __init__(self):
        self.items = {}

    # Fitur tambah barang ke keranjang
    def add_item(self, item_name, price, quantity):
        # Defect 1: Tidak ada validasi nilai minus
        if item_name in self.items:
            self.items[item_name]['quantity'] += quantity
        else:
            self.items[item_name] = {'price': price, 'quantity': quantity}

    # Fitur hapus barang
    def remove_item(self, item_name):
        # Defect 2: Tidak mengecek apakah barang ada di keranjang
        del self.items[item_name]

    # Fitur hitung total belanja dengan diskon
    def calculate_total(self, discount_percent):
        total = 0
        for item in self.items.values():
            total += item['price'] * item['quantity']
        
        # Defect 3: Rumus diskon salah (hanya mengurangi nominal, bukan persentase)
        final_total = total - discount_percent
        return final_total

# --- Kode Testing Simulasi ---
if __name__ == "__main__":
    cart = ShoppingCart()
    cart.add_item("Laptop", 15000000, 1)
    
    # Memicu Defect 1
    cart.add_item("Mouse", 150000, -2) 
    
    # Memicu Defect 3 (Diskon 10%, tapi malah dikurangi Rp 10)
    print("Total Belanja:", cart.calculate_total(10)) 
    
    # Memicu Defect 2 (Crash karena Keyboard tidak ada di keranjang)
    cart.remove_item("Keyboard")