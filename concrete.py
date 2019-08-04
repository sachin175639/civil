#civil tools BBSAD
#sachin
#contact +918105190452
#bearing concrete quantity 

print ""
print "\tConcrete Quantity"
print ""
fa=1500
ca=1500
cement = 1440
volume = 1
def help():
 help = '''

	Commands	   usage
	========	   =====
	use (m15,m20,m25)  mix 
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

def calc(fa,ca,cement,volume,mix,mix_ratio,s,a,m):
 dry_volume = 1.54*volume

#cement calculations############
# in cubic_meter , kg , cubic_meter 

 c_cubic_meter = (dry_volume*1)/mix
 c_kg = c_cubic_meter*cement
 no_bags = c_kg/50
 c_cft = no_bags*1.226

#sand calculations##########
#in cubic_meter , kg , cubic_meter
 
 s_cubic_meter = (dry_volume*s)/mix
 s_kg = s_cubic_meter*fa
 s_cft = s_cubic_meter*35.3147
 	 

#sand course aggrigate calculation##########
#in cubic_meter , kg , cubic_meter
 
 a_cubic_meter = (dry_volume*a)/mix
 a_kg = a_cubic_meter*fa
 a_cft = a_cubic_meter*35.3147
 
 print ""
 print " "+m +"  "+mix_ratio+" of volume "+str(volume)+" m3"
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
 
 print ""
 print "::Agrigate:: calucalitions"
 print ""
 print "	CUM(cubic meter) :",a_cubic_meter," m3"
 print "	CFT(cubic feet)  :",a_cft," cft"
 print "	Kg               :",a_kg," kg"
 print ""


 	 
while True:
       try:
	civ = raw_input("CQ ||> ")
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
	elif civil[0] == "use":
		if civil[1] == "m15":
		 m = "M15"
		 mix = 7
		 mix_ratio = "1 : 2 : 4"
		 s = 2
		 a = 4
		
		elif civil[1] == "m20":
		 m = "M20"
		 mix = 5.5
		 mix_ratio = "1 : 1.5 : 3"
		 s = 1.5
		 a = 3

		elif civil[1] == "m25":
		 m= "M25"
		 mix = 4
		 mix_ratio = "1 : 1 : 2"
		 s = 1
		 a = 2

		else:
		 print ">> Command invalid <<"
	elif civil[0] == "show":
		if civil[1] == "options":
		 print "Density of cement  : ",cement,"kg/m3"
		 print "Density of sand    : ",fa," kg/m3"
		 print "density of jelly   : ",ca," kg/m3"
		 print "Volume of concrete : ",volume," m3"
		else:
		 print ">> Command invalid <<"
		 pass
	elif civil[0] == "run":
		try:
	  	 calc(fa,ca,cement,volume,mix,mix_ratio,s,a,m)
		except NameError:
		 print "Please assign values" 
	
	elif civil[0] =="calc":
		 print ""
		 print "Calculator Enabled, Press enter to exit "
		 try:
		  while True:
		   san = input("Calculator : ")
		   print san
	           
		 except SyntaxError:
		    print ""
		    pass
	else:
		print ">> Command invalid <<"
		continue
       except IndexError:
	print ">> Command invalid <<"
	pass