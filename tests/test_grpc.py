import pytest
from helpers.grpc import client
from grpc._channel import _InactiveRpcError


def test_create_employee():
    res = client.create_employee(
        first_name='Bruce',
        second_name='Wayne',
        age=33
    )
    assert res.id != 0


def test_get_employee():
    first_name, second_name = 'James', 'Gordon'
    age = 51
    res_create = client.create_employee(
        first_name=first_name,
        second_name=second_name,
        age=age
    )

    employee = client.get_employee(res_create.id)
    assert employee.id == res_create.id
    assert employee.first_name == first_name
    assert employee.second_name == second_name
    assert employee.age == age


def test_get_employee_negative():
    with pytest.raises(_InactiveRpcError) as e:
        client.get_employee(-1)


def test_delete_employee():
    first_name, second_name = 'Rachel', 'Daves'
    age = 27
    res_create = client.create_employee(
        first_name=first_name,
        second_name=second_name,
        age=age
    )

    employee = client.delete_employee(res_create.id)
    assert employee.id == res_create.id


def test_delete_employee_negative():
    with pytest.raises(_InactiveRpcError) as e:
        client.delete_employee(-1)
