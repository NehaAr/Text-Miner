#Change the path of input file and open it using the follwing lines of code in python

with open('','r') as input_file:
  input_data = json.load(input_file)
  input_file.close()
  input_data1=json.dumps(input_data , indent=6)
  input_data_self=json.dumps(input_data)
