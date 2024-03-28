# grpc_tools is a C extension bundling both protoc and the gRPC Python protoc plugin together 
# so that the user doesn't have to deal with downloading protoc, downloading the gRPC Python code generator, 
# and getting the necessary configuration set up to make them work together properly

# --python_out indicates where the generated serialization/deserialization code should go
# --grpc_python_out is the flag registered by the gRPC Python code generator, indicating where 
# Python stub and server code should be placed on the filesystem

python3 -m grpc_tools.protoc -I . --python_out=. --grpc_python_out=. example.proto
