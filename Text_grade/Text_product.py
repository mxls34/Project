def create_product(filename, product_id, name, price, quantity):
    with open(filename, 'a') as file:
        file.write(f"{product_id},{name},{price},{quantity}\n")
   
def product_vat(filename):
    with open(filename, 'r') as file:
        products = file.readlines()
        for i in products:
            row = i.strip().split(',')
            price = int(row[2])
            vat = (price*7)/100
            totals = price+vat
    return vat,totals,price

def main():
    filename = 'product.txt'
    while True:
        spc = '-' * 29
        print(spc)
        print(f'|' + 'ระบบจัดการร้านค้า'.center(30) + '|')
        print(spc)
        print("1. เพิ่มสินค้า")
        print("2. หาค่าVatของสินค้า")
        print("3. ยอดรวม")
        print("4. ")
        print("5. ออกจากระบบ")
        choice = input("เลือกการทำงาน: ")
        vat = []

        if choice == '1':
            name = input('ชื่อสินค้า :')
            product_id = input("รหัสสินค้า: ")
            price = int(input("ราคาสินค้า: "))
            quantity = int(input("จำนวนสินค้า: "))
            create_product(filename,product_id, name, price, quantity)
        if choice == '2':
            vat,totals,price = product_vat(filename)
            print('ราคา :' , price) 
            print('ค่าvat :',vat)
            print('ยอดรวม :',totals)
        # if choice == '3':

            

if __name__ == '__main__':
    main()