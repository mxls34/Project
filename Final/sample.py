def create_product(filename, product_id, name, price, quantity):
    with open(filename, 'a') as file:
        file.write(f"{product_id},{name},{price},{quantity}\n")
    print(f"เพิ่มสินค้า {name} เรียบร้อยแล้ว")

def read_products(filename):
    with open(filename, 'r') as file:
        products = file.readlines()
        if not products:
            print("ยังไม่มีสินค้าในระบบ")
        else:
            report_header()
            for product in products:
                report_product(product)

def report_header():
    # header = ["รหัสสินค้า", "ชื่อสินค้า", "ราคาสินค้า", "จำนวนสินค้า"]
    # header_row = "|".join(f"{col:^20}" for col in header)
    header_row = f"{'รหัสสินค้า':^11} | {'ชื่อสินค้า':^34} | {'ราคาสินค้า':^17} | {'จำนวนสินค้า':^17}"
    separator = "-" * 79

    # แสดงหัวข้อและเส้นคั่น
    print(f"{'รายงานสินค้า':^80}")
    print(separator)
    print(f"|{header_row}|")
    print(separator)

def report_product(product):
    row = product.strip().split(',')
    # ฟอร์แมตสินค้าแต่ละแถวให้ตรงกับความกว้างของคอลัมน์ในส่วนหัว
    row_str = f"{row[0]:^8} | {row[1]:^30} | {row[2]:^15} | {row[3]:^15}"
    print(f"|{row_str}|")
    separator = "-" * 79
    print(separator)


def update_product(filename, product_id, new_name=None, new_price=None, new_quantity=None):
    updated = False
    products = []
    with open(filename, 'r') as file:
      for line in file:
        product = line.strip().split(',')
        if product[0] == product_id:
          if new_name:
            product[1] = new_name
          if new_price:
            product[2] = new_price
          if new_quantity:
            product[3] = new_quantity
          updated = True
        products.append(product)
    if updated:
          with open(filename, 'w') as file:
              for product in products:
                  file.write(','.join(product) + '\n')
          print(f"อัพเดตสินค้ารหัส {product_id} เรียบร้อยแล้ว")
    else:
          print(f"ไม่พบสินค้ารหัส {product_id}")

def delete_product(filename, product_id):
    deleted = False
    products = []
    with open(filename, 'r') as file:
        for line in file:
            product = line.strip().split(',')
            if product[0] != product_id:
                products.append(product)
            else:
                deleted = True
    if deleted:
        with open(filename, 'w') as file:
            for product in products:
                file.write(','.join(product) + '\n')
        print(f"ลบสินค้ารหัส {product_id} เรียบร้อยแล้ว")
    else:
        print(f"ไม่พบสินค้ารหัส {product_id}")

def menu():
  filename = 'products.txt'
  while True:
        print()
        print('='*29)
        print(f'|' + 'ระบบจัดการร้านค้า'.center(30) + '|')
        print('='*29)
        print("1. เพิ่มสินค้า")
        print("2. แสดงสินค้าทั้งหมด")
        print("3. อัพเดตสินค้า")
        print("4. ลบสินค้า")
        print("5. ออกจากระบบ")
        choice = input("เลือกการทำงาน: ")

        if choice == '1':
          product_id = input("รหัสสินค้า: ")
          name = input("ชื่อสินค้า: ")
          price = float(input("ราคาสินค้า: "))
          quantity = int(input("จำนวนสินค้า: "))
          create_product(filename, product_id, name, price, quantity)
        elif choice == '2':
          read_products(filename)
        elif choice == '3':
          product_id = input("รหัสสินค้าที่ต้องการอัพเดต: ")
          new_name = input("ชื่อใหม่ (กด Enter หากไม่ต้องการเปลี่ยน): ")
          new_price = input("ราคาใหม่ (กด Enter หากไม่ต้องการเปลี่ยน): ")
          new_quantity = input("จำนวนใหม่ (กด Enter หากไม่ต้องการเปลี่ยน): ")
          update_product(filename, product_id, new_name, new_price, new_quantity)
        elif choice == '4':
          product_id = input("รหัสสินค้าที่ต้องการลบ: ")
          delete_product(filename, product_id)
        elif choice == '5':
          print("ออกจากระบบ")
          break
        else:
          print("กรุณาเลือกตัวเลือกที่ถูกต้อง")

if __name__ == '__main__':
    menu()