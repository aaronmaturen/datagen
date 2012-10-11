#!/usr/bin/python
#lan12-49:datagen atmature$ python data.py 
#Data Generator, v0.1.0a
#Aaron T. Maturen <atmature@svsu.edu>
#type 'help' for help info, 'end' to end program


#lan12-49:datagen atmature$ python data.py
#Data Generator, v0.1.0a
#Aaron T. Maturen <atmature@svsu.edu>
#type 'help' for help info, 'end' to end program
#>>> ADD COLUMN index "[0-9]{4}" s                             
#>>> ADD COLUMN password "[0-9a-zA-Z]{4,10}"
#>>> ADD COLUMN first_name "<file|datastores/firstnames.txt>"
#>>> ADD COLUMN last_name "<file|datastores/lastnames.txt>"
#>>> ADD COLUMN gender "(male|female)"
#>>> ADD COLUMN active "active"
#>>> ADD COLUMN salary "\$<float|13.5,22.6,.05>"
#>>> ADD COLUMN age "<int|16,80,1>"
#>>> SHOW COLUMNS
#+ ---------------------------------- + -------- + ------------- + --------- + --------- + ----------- +
#|  regex                             |     pkey |          name |    source |    unique |        type | 
#+ ---------------------------------- + -------- + ------------- + --------- + --------- + ----------- +
#|  \$<float|13.5,22.6,.05>           |    False |        salary |         r |     False |    char(45) | 
#|  [0-9]{4}                          |    False |         index |         s |     False |    char(45) | 
#|  <file|datastores/firstnames.txt>  |    False |    first_name |         r |     False |    char(45) | 
#|  <file|datastores/lastnames.txt>   |    False |     last_name |         r |     False |    char(45) | 
#|  (male|female)                     |    False |        gender |         r |     False |    char(45) | 
#|  <int|16,80,1>                     |    False |           age |         r |     False |    char(45) | 
#|  active                            |    False |        active |         r |     False |    char(45) | 
#|  [0-9a-zA-Z]{4,10}                 |    False |      password |         r |     False |    char(45) | 
#+ ---------------------------------- + -------- + ------------- + --------- + --------- + ----------- +
#>>> GENERATE FILE 10
#>>> SHOW FILE
#+ -------- + -------- + ------------- + ------------- + --------- + ------ + --------- + ------------ +
#|  salary  |    index |    first_name |     last_name |    gender |    age |    active |     password | 
#+ -------- + -------- + ------------- + ------------- + --------- + ------ + --------- + ------------ +
#|  $18.2   |     0000 |        REAGAN |         MANHA |      male |     72 |    active |     iFBT0y8T | 
#|  $17.05  |     0001 |       MARDELL |    KNACKSTEDT |      male |     65 |    active |        3tuIg | 
#|  $17.9   |     0002 |        MARLIN |     PURFEERST |    female |     80 |    active |     kgX29wR7 | 
#|  $13.8   |     0003 |          PURA |       WHOOLEY |      male |     20 |    active |    ZbfxLo4lO | 
#|  $19.95  |     0004 |        IVETTE |        SLENTZ |    female |     38 |    active |      MNPvLOO | 
#|  $18.35  |     0005 |        HALINA |      BELINSKY |    female |     56 |    active |     XRCXkoWr | 
#|  $22.5   |     0006 |        WINONA |         GERST |    female |     46 |    active |         4pY9 | 
#|  $19.7   |     0007 |         WILEY |          BURO |    female |     42 |    active |         eF5U | 
#|  $14.55  |     0008 |     WILLODEAN |        ACKINS |      male |     74 |    active |    T30YimWmu | 
#|  $14.4   |     0009 |        COLENE |        BOHREN |      male |     23 |    active |      zNEIPiD | 
#+ -------- + -------- + ------------- + ------------- + --------- + ------ + --------- + ------------ +
#>>> SAVE FILE randomData.tsv
#[saved file]
#>>> 



help = "Datagen v0.1.0a created by Aaron T. Maturen <atmature@svsu.edu>\n\
	    Commands:\n\
	      ADD COLUMN name \"regex\" source\n\
	         name = word (without quotes)\n\
	         regex = regular expression (needs quotes)\n\
	         source = r or s for random and sequential records, optional,\n\
	                  defaults to random, sequential is extreamly slow \n\n\
	      SHOW COLUMNS\n\
	         displays all configured columns\n\
	      SHOW FILE\n\
	         displays all generated data for a file\n\
	      SAVE FILE filename\n\
	         saves file relative to the pwd\n\
	      GENERATE FILE count\n\
	         generates test data for the table\n\n\
	   Regular Expressions:\n\
             <file|filename> uses a range from a textfile, one value per line\n\
             <int|start,stop,step> uses a range of integers\n\
             <float|start,stop,step,[precision]> uses a range of floats\n\
             (this|that) this or that\n\
             [a-zA-Z0-9]{min,max} creates a random string using characters from \n\
		                          the alphanumeric set with a length between min and max\n\
		  text - static text\
		"
import re
import string
import random

#Program Configuration
inputPrompt = ">>> "


def floatRange(start, stop, step, precision=5):
	start = float(start)
	stop = float(stop)
	step = float(step)
	precision = int(precision)
	import math
	start += 0.0
	count = int(math.ceil((stop - start) / step))
	rtn = [None,] * count
	rtn[0] = start
	for i in xrange(1,count):
		rtn[i] = round(rtn[i-1] + step,precision)
	return rtn
	
def intRange(start,stop,step=1):
	start = int(start)
	stop =  int(stop)
	step = int(step)
	rtn = []
	while start <= stop:
		rtn.append(start)
		start += step
	#print rtn
	return rtn
	
# mm/dd/yyyy
def dateRange(start,stop,step=1):
	import datetime
	rtn = []
	start = re.split('/',start)
	startDate = datetime.date(int(start[2]),int(start[0]),int(start[1]))
	stop = re.split('/',stop)
	stopDate = datetime.date(int(stop[2]),int(stop[0]),int(stop[1]))
	step = int(step)
	while startDate <= stopDate:
		rtn.append(str(startDate))
		startDate += datetime.timedelta(days=step)
		
	return rtn

def charRange(startchar, stopchar):
	return [chr(i) for i in range(ord(startchar),ord(stopchar)+1)]

def columnRange(name):
	global virtual_file
	return virtual_file.select_column(name)
	
def cartesian_product(*args):
	import itertools
	return_set = []
	for element in itertools.product(*args):
		element_str = ''
		for item in element:
			element_str = element_str + (str(item))
		return_set.append(re.sub('\\\\','',element_str))
	return return_set
	
#print cartesian_product((1, 2), (3, 'cat'),(5,6))

#print charRange('a','d')

def get_max_width(table, index):
	return max([len(str(row[index])) for row in table])

def pprint_table(table):
	import sys
	col_paddings = []
	def print_break():
		print >> sys.stdout, '+',str('-').rjust(col_paddings[0]+2,'-'),
		for i in col_paddings[1:]:
			print >> sys.stdout, '+',str('-').rjust(i+3,'-'),
		print >> sys.stdout,'+'

	for i in range(len(table[0])):
		col_paddings.append(get_max_width(table, i))
	print_break()

	# left col
	print >> sys.stdout, '| ',str(table[0][0]).ljust(col_paddings[0] + 1),'| ',
	# rest of the cols
	for i in range(1, len(table[0])):
		col = str(table[0][i]).rjust(col_paddings[i] + 2)
		print >> sys.stdout,col,'| ',
	print >> sys.stdout

	print_break()

	for row in table[1:]:
		# left col
		print >> sys.stdout, '| ',str(row[0]).ljust(col_paddings[0] + 1),'| ',
		# rest of the cols
		for i in range(1, len(row)):
			col = str(row[i]).rjust(col_paddings[i] + 2)
			print >> sys.stdout,col,'| ',
		print >> sys.stdout
	
	print_break()
	
def regexClasses(regex):
	return re.findall('(.+)',''.join(regex))
	
#requires regex like [a-z]{6,7}[A-Z]{0,1}
def randomCharacters(regex):
	rtnstr = []
	matchsets = re.split("(\[[^\[\]\{\}]*\]\{\d*,?\d*\}|\([^\[\]\{\}\(\)]*\)|\<[^\[\]\{\}\(\)\<\>]*\>)",regex)
	#print matchsets;
	for atomicset in matchsets:
		if atomicset != None:
			if len(atomicset) > 0:
				#check to see if atomic regex is supposed to be random characters
				if atomicset == ''.join(re.findall("(\[[^\[\]\{\}]*\]\{\d*,?\d*\})",atomicset)):
					setrange = ''.join(re.findall('['+''.join((re.findall("\[.*\]",atomicset)))[1:-1]+']*', string.printable))
					numbers = sorted(re.findall('\d*',''.join(re.findall("\{\d*,?\d*\}",atomicset))))
					#print numbers		
					if len(numbers) == 1:
						numbers.append('')
					else:
						if sorted(numbers)[-2] != '':
							rtnstr.append(''.join(random.choice(setrange) for z in range(random.randrange(int(sorted(numbers)[-1]), int(sorted(numbers)[-2])))))
						elif sorted(numbers)[-1] != '':
							rtnstr.append(''.join(random.choice(setrange) for z in range(int(sorted(numbers)[-1]))))
				elif atomicset[0] == '(' and atomicset[-1] == ')' and len(re.split('\|',atomicset)) > 1 and atomicset[-2] != '\\':
					rtnstr.append(''.join(random.choice(re.split('[|]',atomicset[1:-1]))))
				elif atomicset[0] == '<' and atomicset[-1] == '>':
					classset = re.split('\|',atomicset[1:-1])
					if classset[0].lower() == 'file':
						f = open(classset[1])
						lines = []
						for line in f:
							lines.append(str(re.sub('\n','',line)))
						f.close()
						rtnstr.append(random.choice(lines))
					elif classset[0].lower() == 'int':
						rtnstr.append(str(random.choice(intRange(*re.split(',',classset[1])))))
					elif classset[0].lower() == 'float':
						rtnstr.append(str(random.choice(floatRange(*re.split(',',classset[1])))))
					elif classset[0].lower() == 'date':
						rtnstr.append(str(random.choice(dateRange(*re.split(',',classset[1])))))
				else:
					rtnstr.append(''.join(regexClasses(atomicset)))
	#print rtnstr
	return re.sub('\\\\','',''.join(rtnstr))

def printRange(regex):
	def break_list(somelists):
		for z in range(len(somelists)):
			yield (somelists[z])
			
	rtnstr = []
	lists = []
	matchsets = re.split("(\[[^\[\]\{\}]*\]\{\d*,?\d*\}|\([^\[\]\{\}\(\)]*\)|\<[^\[\]\{\}\(\)\<\>]*\>)",regex)
	#print matchsets;
	for atomicset in matchsets:
		#print atomicset
		if atomicset != None and atomicset:
			if len(atomicset) > 0:
				#check to see if atomic regex is supposed to be a set of characters
				if atomicset == ''.join(re.findall("(\[[^\[\]\{\}]*\]\{\d*,?\d*,?\d*\})",atomicset)):
					setrange = ''.join(re.findall('['+''.join((re.findall("\[.*\]",atomicset)))[1:-1]+']*', string.printable))
					numbers = sorted(re.findall('\d*',''.join(re.findall("\{\d*,?\d*\}",atomicset))))
					#print numbers		
					if len(numbers) == 1:
						numbers.append('')
					else:
						if sorted(numbers)[-2] != '':
							for z in range(0,int(sorted(numbers)[-2])):
								lists.append(tuple(re.findall('.',setrange)))
							for z in range(int(sorted(numbers)[-2]),int(sorted(numbers)[-1])):
								lists.append(tuple(re.findall('.',setrange + "\\")))
							#print lists
						elif sorted(numbers)[-1] != '':
							for z in range(0,int(sorted(numbers)[-1])):
								lists.append(tuple(re.findall('.',setrange)))
				elif atomicset[0] == '(' and atomicset[-1] == ')' and len(re.split('\|',atomicset)) > 1 and atomicset[-2] != '\\':
					lists.append(re.split('[|]',atomicset[1:-1]))
				elif atomicset[0] == '<' and atomicset[-1] == '>':
					classset = re.split('\|',atomicset[1:-1])
					if classset[0].lower() == 'file':
						f = open(classset[1])
						lines = []
						for line in f:
							lines.append(str(re.sub('\n','',line)))
						f.close()
						lists.append(lines)
					elif classset[0].lower() == 'int':
						lists.append(intRange(*re.split(',',classset[1])))
					elif classset[0].lower() == 'float':
						lists.append(floatRange(*re.split(',',classset[1])))
					elif classset[0].lower() == 'date':
						lists.append(dateRange(*re.split(',',classset[1])))
					elif classset[0].lower() == 'column':
						print 'column'
						lists.append(columnRange(*re.split(',',classset[1])))
				else:
					lists.append(regexClasses(atomicset))
				#print cartesian_product(*lists)
			#print lists
	return cartesian_product(*lists)

#classes 
class Records():
	#if unique we need to make this a dictionary
	def __init__(self,unique=False):
		self.unique = unique
		self.values = []
		
	def add(self,value):
		if self.unique and value not in self.values:
			self.values.append(value)

	def get(self, value):
		return self.values[value]
		
	def list(self):
		return self.values
		
class Column():
	def __init__(self):
		self._column_type = 'char(45)'
		self._pkey = False
		self._unique = False
		self._source = 'r'
		self._mask = ''
		self._name = 'index'
		self._size = 15
		self._records = Records(self._unique)
		self._regex = ""
		
	def rename(self,newname):
		self._name = newname
	def describe(self):
		return {'name':self._name,'type':self._column_type, 'pkey':self._pkey,'unique':self._unique,'source':self._source,'regex':self._regex}
	def add_record(self,value):
		self._records = value[0:self._size]
	def list_methods(self):
		methods = []
		for method in dir(self):
			if method[0:1] != '_':
				methods.append(method)
		return methods
	def fill(self):
		#phone numbers: "\(989\) (799|791|607)-[0-9]{4}"
		if self._source == 's':
			self._records = printRange(self._regex)[0:self._size]
		elif self._source == 'r':
			rtn = []
			for i in range(self._size):
				rtn.append(randomCharacters(self._regex))
			self._records = rtn
		#for x in range(self._size):
		#	self.add_record(randomCharacters(self._regex))
		#	#self.add_record(randomCharacters('[X]{3,3}[-]{1,1}[X]{2,2}[-]{1,1}[0-9]{4,4}'))
	def list_records(self):
		return self._records
	def list_attr(self):
		attr = []
		for attr in dir(self):
			print attr[0:-1]
	def set_source(self, value):
		self._source = value
	def size(self, value=15):
		self._size = value
		return value
		
#Functions
#print column.list_records()

class File:
	global column
	columns = dict()
	
	def __init__(self):
		self._size = 15
		self._records = []
		
	def add_column(self,attr):
		name = attr[0]
		regex = attr[1][1:-1]
		try:
			source = attr[2]
		except IndexError:
			source = 'r'
		column = Column()
		column._regex = regex
		column._name = name
		column._source = source
		self.columns[name] = column
		return self.columns[name].describe()
	def remove_column():
		pass
	def rename():
		pass
		
	def generate(self,size=100):
		self.set_size(int(size[-1]))
		row = []
		rtn = []
		for c in self.columns:
			row.append(c)
			self.columns[c].size(self.get_size())
			self.columns[c].fill()
			#print self.columns[c].list_records()
		rtn.append(row)
		for i in range(self.get_size()):
			row = []
			for c in self.columns:
				try:
					row.append(self.columns[c]._records[i])
				except IndexError:
					row.append('')
			rtn.append(row)
		self._records = rtn
		return self._records
			
	def describe():
		pass
	def select_column(self,name):
		for column in self.columns.keys():
			if column._name == name:
				return column.list_records()
		return ''
				
	def show_columns(self, attr):
		if len(self.columns)!=0:
			printed_header = False
			values = []
			for column in self.columns.keys():
				if printed_header == False:
					values.append(self.columns[column].describe().keys())
					printed_header = True
				
				values.append(self.columns[column].describe().values())
			pprint_table(values)
		else:
			print "There are no columns."
	def get_size(self):
		return self._size
	def set_size(self, value):
		self._size = value
	def pprint(self,attr):
		pprint_table(self._records)
	def dump(self,attr):
		filename = attr[0]
		o = open(filename+'.txt','w')
		for row in self._records:
			o.write('\t'.join(row) + "\r\n")
		o.close()
		print "[saved " + filename + ".txt ]"
		
	def dump_structure(self, attr):
		if len(self.columns)!=0:
			printed_header = False
			values = []
			for column in self.columns.keys():
				if printed_header == False:
					values.append(self.columns[column].describe().keys())
					printed_header = True
				values.append(self.columns[column].describe().values())
			#print values
			filename = attr[0]
			o = open(filename+'.rpt','w')
			for row in values:
				joiner = []
				for item in row:
					joiner.append(str(item))
				o.write('\t'.join(joiner) + "\r\n")
			o.close()
			print "[saved " + filename + ".rpt ]"
		else:
			print "There are no columns."

		
#Beginning help information
print "Data Generator, v0.1.0a"
print "Aaron T. Maturen <atmature@svsu.edu>"
print "type 'help' for help info, 'end' to end program"

virtual_file = File()
#virtual_file.add_column(('birthday',"\"<date|05/29/1990,06/29/1990>\""))
#virtual_file.add_column(('name',"\"<file|datastores/firstnames.txt>\""))
#virtual_file.columns['birthday'].size(50)
#virtual_file.columns['birthday'].fill()
#print virtual_file.columns['birthday'].list_records()


#print printRange("[a-c]{2,4}[q-t]{3}")
#print printRange("(a|b)<date|05/29/1988,05/29/1990>")
#print printRange("<column|birthday>")
#print randomCharacters("<file|datastores/firstnames.txt>'s birthday is <date|5/29/2011,6/15/2011>")


commands = ({'ADD':{'FILE':1,'COLUMN':'add_column','SOURCE':3},
			 'DELETE':{'FILE':4,'COLUMN':5,'SOURCE':6},
			 'GENERATE':{'FILE':'generate','COLUMN':8},
			 'SHOW':{'COLUMNS':'show_columns','FILE':'pprint'},
			 'SAVE':{'FILE':'dump','COLUMNS':'dump_structure'}})
	
def processInput(input):
	global commands
	global virtual_file
	#column = Column()
	#column.fill()
	inputSplit = re.findall('(\w+|".*")',input)
	if inputSplit[0].upper() in commands.keys():
		if inputSplit[1].upper() in commands[inputSplit[0].upper()].keys():
			return getattr(virtual_file,commands[inputSplit[0].upper()][inputSplit[1].upper()])(inputSplit[2:])
			#return getattr(column,commands[inputSplit[0]][inputSplit[1]])()
			#return True #commands[inputSplit[0]][inputSplit[1]]
	else:
		return inputSplit[0]
		
#main loop
input = []
input.append(raw_input(inputPrompt))
#input.append('end')
while (input[-1]!="end" and input[-1]!="exit"):
	if input[-1]=='help':
		print help
	processInput(input[-1])
		
	#update input to continue loop
	input.append(raw_input(inputPrompt))
	#input.append('end')
