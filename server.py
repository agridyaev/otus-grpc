import grpc
from grpc_reflection.v1alpha import reflection
import example_pb2
import example_pb2_grpc

from concurrent import futures


class EmployeeServicer(example_pb2_grpc.EmployeesAPIServicer):
    employees = dict()
    count = 1

    def CreateEmployee(self, request, context):
        e = {'first_name': request.first_name,
             'second_name': request.second_name,
             'age': request.age}
        print(f'Add employee: "{e}"')

        e['id'] = EmployeeServicer.count
        EmployeeServicer.count += 1

        EmployeeServicer.employees[e['id']] = e
        return example_pb2.CreateEmployeeResponse(id=e['id'])

    def GetEmployee(self, request, context):
        print(f'Get employee: id - "{request.id}"')
        if request.id not in EmployeeServicer.employees:
            raise grpc.RpcError(f'Employee with id "{request.id}" not exists')

        e = EmployeeServicer.employees[request.id]
        return example_pb2.GetEmployeeResponse(
            id=e['id'], first_name=e['first_name'], second_name=e['second_name'], age=e['age'])

    def DeleteEmployee(self, request, context):
        print(f'Remove employee: id - "{request.id}"')
        if request.id not in EmployeeServicer.employees:
            raise grpc.RpcError(f'Employee with id "{request.id}" not exists')

        e = EmployeeServicer.employees.pop(request.id)
        EmployeeServicer.count -= 1
        return example_pb2.DeleteEmployeeResponse(id=e['id'])


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    example_pb2_grpc.add_EmployeesAPIServicer_to_server(EmployeeServicer(), server)
    service_names = (
        example_pb2.DESCRIPTOR.services_by_name['EmployeesAPI'].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(service_names, server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server listening on :50051")
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
