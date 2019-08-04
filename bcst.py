#civil tools BBSAD
#sachin
#contact +918105190452
#bearing capacity of soil test calculator

print ""
print "\tBearing Capacity of Soil Test"
print ""
def help():
 help = '''

	Commands	usage
	========	=====
	set weight       example: 5kg,10kg
	set fh           (fall height) 150cm
	set tr		 trails of impression 4,5,6..n
	set fos          (factor of safty 2 to 3)default 2
	set area         (area of rerangle or circle)
	show options	 shows assigned values
	run		 final calculations
	
	others
	======
	calc               calculator (press enter to disable)
'''
 print help
w = 0
fh = 0
trail = 0
fose = 2
area = 0
def calc(w,fh,trail,fose,area):
 
 y = 0
 z=[]
 while y != trail:
	try:
	 y = y+1
	 var = input("Enter depth of impression trail "+str(y)+" : ")
	 z.append(var)
 	except SyntaxError:
	 print "something missed ....."
	 pass
 var2 = sum(z)
 avg = var2/trail

 R = (w*fh)/avg
 ua = R/area
 sa = R/(area*fose)
 print ""
 print "Ultimate bearing capacity   : ",R,"   Kg"
 print "Resistance of soil/unit area: ",ua," Kg/cm2"
 print "Safe bearing capacity       : ",sa," Kg/cm2"


while True:
       try:
	civ = raw_input("BCST ||> ")
	civil = civ.split()
	if not civil:
		print ">> Command invalid <<"
		continue
	elif civil[0] == "help":
		help()
	elif civil[0] == "exit":
		break
	elif civil[0] == "set":
		if civil[1] == "weight":
		 w = int(civil[2])
		elif civil[1] == "fh":
		 fh = int(civil[2])
		elif civil[1] == "tr":
		 trail = int(civil[2])
		elif civil[1] == "fos":
		 fose = int(civil[2])
		elif civil[1] == "area":
		 area = float(civil[2])
		else:
		 print ">> Command invalid <<"

	elif civil[0] == "show":
		if civil[1] == "options":
		 print ""
		 print "Weight of iron(cube or ball): ",w," Kg"
		 print "Fall Height                 : ",fh," cm"
		 print "Trail numbers of impression : ",trail
		 print "Area of rec (or) circle     : ",area," cm2"
		 print "Factor of safety            : ",fose
		 print ""
		else:
		 print ">> Command invalid <<"
		 pass
	elif civil[0] == "run":
		try:
	  	 calc(w,fh,trail,fose,area)
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