from nada_dsl import *

def nada_main():
    party1 = Party(name="Party1")
    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))

    # Perform various computations
    sum_result = my_int1 + my_int2
    product_result = my_int1 * my_int2
    difference_result = my_int1 - my_int2
    division_result = my_int1 / my_int2

    # Conditional operation to find the maximum value using a comparison
    is_greater = my_int1 > my_int2
    max_result = is_greater.if_else(my_int1, my_int2)

    # Nested operations
    nested_result = (sum_result * product_result) - (difference_result / division_result)

    return [
        Output(sum_result, "sum_output", party1),
        Output(product_result, "product_output", party1),
        Output(difference_result, "difference_output", party1),
        Output(division_result, "division_output", party1),
        Output(max_result, "max_output", party1),
        Output(nested_result, "nested_output", party1)
    ]
