#====Simpe Retail Managment System=====

#===== A project of Dilanka-jay ===


from retailshop_functions import * #import all the functions from retailshop_function module	

#main part(display part)
def main():
	
	#create_table function exists inside of retailshop_function module
	create_table()

	if log_in():
		global conn
		global cur
		while True:
			print("\n==== Welcome To Retail Shop Managment System ====\n\n")
			print("----------- Main Menu ------------\n")
			print("Press 1 to add products")
			print("Press 2 to view all products")
			print("Press 3 to delete products")
			print("Press 4 to update products")
			print("Press 5 to search products")
			print("Press 6 to change admin settings")
			print("Press 7 to exit")
			
			#checking input options
			option = input("\nWhat is your choice: \n")
			
			#=====start add products option======
			if option == "1": 
				
				product_name = input("Enter the product name: ")
				product_price = int(input("Enter the product price: "))
				product_qty = int(input("Enter quantity: "))
				product_dis = int(input("Enter product discount: "))
				
				#store entered product details inside the database
				cur.execute("INSERT INTO products (name, price,quantity, discount) VALUES (?,?,?,?)",( product_name, product_price, product_qty, product_dis))
				conn.commit()
				print("\nNew record has been created!")
				userExit() 
				#=====end add products option======
				
			
			#=====start show products option======
			elif option == "2": 
				cur.execute("SELECT * FROM products")
				fetch = cur.fetchall()
				if fetch:
					for row in fetch:
						print("-"*40)
						print("Id = ", row[0])
						print("Name = ", row[1])
						print("Price = ", row[2])
						print("Quantity = ",row[3])
						print("Discount = ", row[4])
						print("-" * 40)
						
				else:
					print("No records in the database")
					
				userExit()
				#=====end show products option======
				
			#======start delete products option=======	
			elif option == "3": 
				del_product = input("What product do you want to delete: ")
				cur.execute("SELECT * FROM products WHERE name = '%s' "%(del_product))
				if cur.fetchone() is not None:
					cur.execute("DELETE FROM products WHERE name = '%s' "%(del_product))
					conn.commit()
					print("\nProduct has been deleted!")
					
				else:
					print("\nNo such product name in the datsbase!")
					userExit()
					
			#=====end delete products option======
				
				#=====start update products option======								
			elif option == "4":
				update_item = input("What product do you want to update?: ")
				
				cur.execute("SELECT * FROM products WHERE name = '%s' "%(update_item))
				data = cur.fetchall()
				if data is not None:
				
					for row in data:
						print("These are the exists data about "+update_item)
						
						print("Id: ",row[0])
						print("Name: ",row[1])
						print("Price: ",row[2])
						print("Quantity: ",row[3])
						print("Discount:",row[4])
						print("-"*30)
						
					
						new_price = int(input("Enter new price: "))
						new_qty = int(input("Enter new quantity: "))
						new_dis = int(input("Enter new discount: "))
						
						
						query = "UPDATE products SET price=?, quantity=?, discount=? WHERE name LIKE ?"
						cur.execute(query, (new_price, new_qty, new_dis, update_item))
						
						
						print("\nSuccessfully updated!")
						conn.commit()
						userExit()
				else:
					print("Not found!")
			
				#=====end update products option======
				
				
				
			#=====start search products option======		
			elif option == "5":
				search = input("What product do you want to search?: ")
				cur.execute("SELECT * FROM products WHERE name LIKE '%s' "%(search))
				
				data = cur.fetchall()
				if data is not None:
					for row in data :
						print("\nSearch result of "+search)
						print("id: ",row[0])
						print("name: ",row[1])
						print("price: ",row[2])
						print("quantity: ",row[3])
						print("discont: ",row[4])
					
						userExit()
				else:
						print("\nCoudn't find the name of "+search+" in the database!")
						#=====end search products option======
			
					#=====start change admin info  option======		
			elif option == "6":
				setting = input("Are you sure you want to change admin settings? (yes/no): ")
				if setting.lower() in ("yes","y"):
					old_name = input("Please enter previous user name: " )
					oldpass = input("Please enter previous password: ").encode()
					old_pass=hashlib.md5(oldpass).hexdigest()
					cur.execute("SELECT *  FROM admin")
					data = cur.fetchone()
		
					if old_name and old_pass in data:
						cur.execute("DELETE FROM admin WHERE username='%s' "%(old_name))
						new_name = input("Enter new admin name: ")
						new_pass = input("Enter new password: ").encode()
						new_hashed_pass=hashlib.md5(new_pass).hexdigest()
						
						cur.execute("INSERT INTO admin (username, password) VALUES (?,?)", (new_name,new_hashed_pass))
						conn.commit()
						userExit()
					
					else:
						print("Sorry you can not change admin settings!")
					#=====end change admin info  option======	
					
						
			elif option == "7": #exit option
					sys.exit()
			else:
				print("Choose a given option")

					
if __name__ == "__main__":						main()

