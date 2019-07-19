class Employee:

	emp_count = 0  # class attribute
	hike_ratio = 0.1

	def __init__(self, emp_id, emp_name, emp_salary):
		self.id = emp_id    # instance/object attribute
		self.name = emp_name
		self.salary = emp_salary
		self.status = 'Active'
		Employee.emp_count += 1

	def compute_hike(self):
		return self.salary * Employee.hike_ratio

	def change_status(self, new_status):
		if self.status == 'Active' and new_status in ['Inactive', 'Suspended', 'Terminated']:
			Employee.emp_count -= 1
		elif self.status in ['Inactive', 'Suspended', 'Terminated'] and new_status == 'Active':
			Employee.emp_count += 1

emp1 = Employee(1, 'ABC', 350000)  # object
emp2 = Employee(2, 'XYZ', 2000000)

print(emp2.compute_hike())  # Output: 200000

print(Employee.emp_count)  # Output: 2

emp1.change_status('Inactive')
print(Employee.emp_count)  # Output: 1