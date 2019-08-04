#civil tools BBSAD
#sachin
#contact +918105190452
#bearing plastering quantity 


print ""
print "\tPlastering Quantity"
print ""
fa=1500
ca=1500
cement = 1440
volume = 0.012
def help():
 help = '''

	Commands	   usage
	========	   =====
	use <1:4,1:5,1:6>  use ratio 1:6
	set dfa            density of sand(default 1500)kg/m3
	set dca            density of jelly(default 1500)kg/m3
	set volume         Example (default 1m3)
	show options	   shows assigned values
	run		   final calculations

	others
	======
	calc               calculator (press enter to disable)
'''
 print help

def calc(fa,cement,volume,m,ratio,s):
 dry_volume = 1.33*volume

#cement calculations############
# in cubic_meter , kg , cubic_meter 

 c_cubic_meter = (dry_volume*1)/m
 c_kg = c_cubic_meter*cement
 no_bags = c_kg/50
 c_cft = no_bags*1.226

#sand calculations##########
#in cubic_meter , kg , cubic_meter
 
 s_cubic_meter = (dry_volume*s)/m
 s_kg = s_cubic_meter*fa
 s_cft = s_cubic_meter*35.3147
 	 

 
 print ""
 print ratio +" of volume  "+ str(volume)+" m3"
 print ""
 print "::Cement:: calculations"
 print ""
 print "	CUM(cubic meter) :",c_cubic_meter," m3"
 print "	CFT(cubic feet)  :",c_cft," cft"
 print "	Kg               :",c_kg," kg"
 print "        Number of cement bags : ", no_bags
 print ""
 print "::Sand:: calucalitions"
 print ""
 print "	CUM(cubic meter) :",s_cubic_meter," m3"
 print "	CFT(cubic feet)  :",s_cft," cft"
 print "	Kg               :",s_kg," kg"
 

while True:
       try:
	civ = raw_input("PQ ||> ")
	civil = civ.split()
	if not civil:
		print ">> Command invalid <<"
		continue
	elif civil[0] == "help":
		help()
	elif civil[0] == "exit":
		break
	elif civil[0] == "set":
		if civil[1] == "dfa":
		 fa = int(civil[2])
		elif civil[1] == "dca":
		 ca = int(civil[2])
		elif civil[1] == "volume":
		 volume = float(civil[2])
		else:
		 print ">> Command invalid <<"
	
	elif civil[0] == "show":
		if civil[1] == "options":
		 print "Density of cement  : ",cement,"kg/m3"
		 print "Density of sand    : ",fa," kg/m3"
		# print "density of jelly   : ",ca," kg/m3"
		 print "Volume of concrete : ",volume," m3"
		else:
		 print ">> Command invalid <<"
		 pass
	elif civil[0] == "use":
		if civil[1] == "1:4":
		 m = 5
		 ratio = "1 : 4"
		 s = 4
		elif civil[1] == "1:5":
		 m = 6
		 ratio = "1 : 5"
		 s = 5
		elif civil[1] == "1:6":
		 m= 7
		 ratio = "1 : 6"
		 s = 6
		else:
		 print ">> Command invalid <<"
		 pass
	elif civil[0] == "run":
		try:
	  	 calc(fa,cement,volume,m,ratio,s)
		except NameError:
		 print "Please assign values" 
	
	elif civil[0] =="calc":
		 print ""
		 print "Calculator Enabled, Press enter to exit "
		 try:
		  while True:
		   san = input("Calculator : ")
		   print float(san)
	           
		 except SyntaxError:
		    print ""
		    pass
	else:
		print ">> Command invalid <<"
		continue
       except IndexError:
	print ">> Command invalid <<"
	pass