
 class Point()

  	blanck = Point()  # by creating a new class, we create a new type - this case Point; the members of the class are of Point type; 

  	# creating new members = instances/objects of that class - we call this process instantiation
  	# to instantiate a new Point object, we call the function Point ==> the variable "blanck" is assigned a reference to a new POint object
  	# a function like Point() that instantiate a new object is called a constructor

  	blanck.x = 3.0
  	blanck.y = 4.0 		# we add new data to an instance by using "Attributes" - using "." notation

print blanck