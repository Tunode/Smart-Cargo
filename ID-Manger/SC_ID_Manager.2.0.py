#IMPORT:
import json
import os.path
#Structure:
class ID_Manager():

	def Ask_ID(self): #Asks for Username and password and returns them in Dictionarty. With Keys: "Loggers_ID" and "Loggers_Pass"
		Logger = {
		"Loggers_ID": " ",
		"Loggers_Pass": " ",
		}
		User_ID = input("Username: ")
		Logger["Loggers_ID"] = User_ID
		User_Pass = input("Password: ")
		Logger["Loggers_Pass"] = User_Pass
		return Logger

	def Check_IF_IDList(self): #Check's if user id list exists.
		IS_File = os.path.exists("IDList.json")
		return IS_File
		
	def Gen_IDList(self): #Generate's user list with Admin's Default loggin information
		Admin = {
		"Admin": "Admin",
		"admin": "78999999512364"
		}
		IDList = json.dumps(Admin)
		with open("IDList.json", "w") as f:
			f.write(IDList)
			f.close()
		Output = "Generated"
		return Output
			
	def Bring_IDList(self):	#Bring's user data.
		IDList = json.load(open("IDList.json"))
		return IDList

	def Reset_IDList(self): #Clears user data and resets admin pass.
		os.remove("IDList.json")
		self.Gen_IDList()
		Output = "Reseted"
		return Output

	def Add_User(self): #Add's new user in user data.
		ID_In_use = True
		while ID_In_use == True: #This Part of code check is user id and pass all ready in use.
			New_User_Data = self.Ask_ID()
			New_User_ID = New_User_Data["Loggers_ID"]
			New_User_Pass = New_User_Data["Loggers_Pass"]	
			Listed_Data = self.Bring_IDList()	
			if New_User_ID in Listed_Data:
				print(" Username is allready in use, Please try again.")
				Inuse1 = True
			if New_User_Pass in Listed_Data:
				if Inuse1== False:
					print(" Username is allready in use, Please try again.")
				else:
					pass
			else:
				ID_In_use = False
				
		New_ID_Key = New_User_Data["Loggers_ID"]
		OLD_ID_Key = "Loggers_ID"
		New_User_Data[New_ID_Key] = New_User_Data.pop(OLD_ID_Key)
		Listed_Data.update(New_User_Data)
		Listed_Data[New_User_ID] = New_User_Pass
		del Listed_Data["Loggers_Pass"]
		with open("IDList.json", "w") as outfile:
			json.dump(Listed_Data, outfile)

	def Print_IDList(self):#Prints list of users in user data.
		User_List = self.Bring_IDList()
		index = 1
		#print(self.Bring_IDList())
		for key, value in User_List.items() :
			print(index, key)
			index += 1
 
	def Chance_Pass(self, logged_User_ID):#Need's Logged user name ass input to chahce password. for logged user.
		User_List = self.Bring_IDList()
		New_Pass = input("New Password: ")
		New_Pass_again = input("New Password again: ")
		if New_Pass == New_Pass_again:
			if logged_User_ID in User_List:
				User_List[logged_User_ID] = str(New_Pass)
				with open("IDList.json", "w") as outfile:
					json.dump(User_List, outfile)
				print('Password Updated.')
			else:
				print('ERROR 404 User not founded.')
		else:
			print("Both passwords need's to match.")	
		pass

	def Remove_User(self):#Removes named user from used data.
		User_List = self.Bring_IDList()
		User_To_Remove = input("Username: ")
		if User_To_Remove in User_List:
			del User_List[User_To_Remove]
			with open("IDList.json", "w") as outfile:
				json.dump(User_List, outfile)
			print('User removed.')
		else:
			print('Username not found.')	
		#print(User_List)

	def IS_ID_Trusted(self): # Check if Loggin data match's data found from user data.
		ID_Trusted = False
		while ID_Trusted == False:
			Logger_Data = self.Ask_ID()
			Loggers_ID =Logger_Data["Loggers_ID"]
			Loggers_Pass = Logger_Data["Loggers_Pass"]	
			Listed_Data = self.Bring_IDList()
				
			if Loggers_ID in Listed_Data:
				Listed_Pass_For_Logger = Listed_Data[Loggers_ID]
				if Listed_Pass_For_Logger == Loggers_Pass:
					ID_Trusted = True
					return ID_Trusted
				else:
					print("Username or password is wrong. Please try again")
			else:
				print("Username or password is wrong. Please try again.")



#-THE-CODE: (Test area:)

ID_Manager = ID_Manager()
#ID_Manager.Reset_IDList()
ID_Manager.Add_User()
#ID_Manager.Gen_IDList()
ID_Manager.IS_ID_Trusted()
ID_Manager.Print_IDList()
#ID_Manager.Remove_User()
logged_User_ID = "Admin"
#ID_Manager.Chance_Pass(logged_User_ID)


