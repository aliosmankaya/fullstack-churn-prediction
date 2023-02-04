from ..services.counts import Counts


def columns_controller(col_type: str):
    result = Counts().columns(col_type=col_type)
    return result


def column_values_controller(column: str):
    result = Counts().column_values(column=column)

    if result:
        return {"values": [value[0] for value in result]}

    return


def user_counts_controller():
    result = Counts().user_counts()

    return {"Customer Count": result}


def categorical_distribution_controller(column: str):
    result = Counts().categorical_distribution(column=column)

    if result:
        return {key: value for key, value in result}

    return


def numerical_distribution_controller(column: str):
    result = Counts().numerical_distribution(column=column)

    if result:
        return {key: value for key, value in zip(["Count", "Sum", "Avg"], result)}

    return
