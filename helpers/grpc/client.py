import grpc
from example_pb2_grpc import EmployeesAPIStub
import example_pb2


channel = grpc.insecure_channel('localhost:50051')
stub = EmployeesAPIStub(channel)


def create_employee(first_name, second_name, age):
    request = example_pb2.CreateEmployeeRequest(
        first_name=first_name, second_name=second_name, age=age)
    return stub.CreateEmployee(request)


def get_employee(id_):
    request = example_pb2.GetEmployeeRequest(id=id_)
    return stub.GetEmployee(request)


def delete_employee(id_):
    request = example_pb2.DeleteEmployeeRequest(id=id_)
    return stub.DeleteEmployee(request)
