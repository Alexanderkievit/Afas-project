"""**Module for individual functions needed by the generator.**"""

import random
from calendar import monthrange
from datetime import date, timedelta, datetime

import bsn


class Functions:
    """**This class contains the functions that can generate data or combine data.**"""

    @staticmethod
    def genereer_random_datum() -> str:
        """**Generates random date.**
        
        Based on the day when you call this function, the function creates a new date in the next
        month.

        Returns: 
            A date object in a string which contains a generated date.
            Example: '2020-12-01'       
        """
        date_format = "%Y-%m-%d"
        today = date.today()
        if today.month == 12:
            random_date = today.replace(year=today.year + 1, month=1, day=random.randint(1, 31))
        else:
            random_day = random.randint(1, monthrange(today.year, today.month + 1)[1])
            random_date = today.replace(month=today.month + 1, day=random_day)

        return random_date.strftime(date_format)

    @staticmethod
    def extra_dagen_optellen(original_date: str, extra_days: int) -> str:
        """**Adds days to a date.**
        
        By calling this function there will by an amount of days be added by a date. It pays attention that the result
        does not fall on weekend days. If that is the case there will be added some extra days.

        Args:
            original_date(str): A date object where extra days will be added.
            extra_days(int): A number of days that must by added on original_date. 

        Returns:
            A date object in a string which contains a new date.
            Example: '2020-12-21'
        """
        date_format = "%Y-%m-%d"
        expiration_date = datetime.strptime(original_date, date_format) + timedelta(days=extra_days)

        if expiration_date.weekday() == 5:
            expiration_date += timedelta(days=2)
        elif expiration_date.weekday() == 6:
            expiration_date += timedelta(days=1)

        return expiration_date.strftime(date_format)

    @staticmethod
    def genereer_random_waarde(min_value: int, max_value: int) -> int:
        """**Generates a random integer.**
        
        By calling this function there will be a random value generated between two values.
        
        Args:
            min_value(int): The lowest value that is possible to generate.
            max_value(int): The highest value that is possible to generate.

        Returns:
            An integer between the two given parameters. 
            Example: 15

        Raises:
            ValueError: An error occurred with the input values. That happens when the min_value is higher then the
            max_value.
        """
        if min_value < max_value:
            random_value = random.randint(min_value, max_value)
        else:
            raise ValueError

        return random_value

    @staticmethod
    def waardes_optellen(first_value: float, second_value: float) -> float or int:
        """**Sums up two values.**
        
        By calling this function the two values will be combined.
        If one of the values is a float, the result will have two decimals.

        Args:
            first_value(float): This value will be combined with the second_value. 
            second_value(float): This value will be combined with the first_value.
            
        Returns:
            A float or integer from the summation of the two values.
            Example: 4.15
        """
        if type(first_value) == float or type(second_value) == float:
            result = round(first_value + second_value, 2)
        else:
            result = round(first_value + second_value)

        return result

    @staticmethod
    def waardes_aftrekken(first_value: float, second_value: float) -> float or int:
        """**Subtracts two values from each other.**
        
        By calling this function the second_value will be subtracted from the first_value.
        If one of the values is a float, the result will have two decimals.

        Args:
            first_value(float): The second_value will be subtracted from this value.
            second_value(float): This value will be subtracted from the first_value.
        
        Returns:
            A float or integer from subtraction of the two values.
            Example: 5.15
        """
        if type(first_value) == float or type(second_value) == float:
            result = round(first_value - second_value, 2)
        else:
            result = round(first_value - second_value)

        return result

    @staticmethod
    def waardes_vermenigvuldigen(first_value: float, second_value: float) -> float or int:
        """**Multiplies one value by another value.**
        
        By calling this function the two values will be multiplied.
        If one of the values is a float, the result will have two decimals.

        Args:
            first_value(float): This value will be multiplied with the second_value.
            second_value(float): This value will be multiplied with the first_value.

        Returns:
            A float or integer from the multiply of the two values.
            Example: 5.25
        """
        if type(first_value) == float or type(second_value) == float:
            result = round(first_value * second_value, 2)
        else:
            result = round(first_value * second_value)

        return result

    @staticmethod
    def waardes_delen(first_value: float, second_value: float) -> float or int:
        """**Divide one value by another value.**
        
        By calling this function first_value will be divided divide by the second_value. 
        If one of the values is a float, the result will have 2 decimals.
        
        Args:
            first_value(float): An integer or float. 
            second_value(float): An integer or float.

        Returns:
            A float or integer of the divided values.
            Example: 4.54
        """
        if type(first_value) == float or type(second_value) == float:
            result = round(first_value / second_value, 2)
        else:
            result = round(first_value / second_value)

        return result

    @staticmethod
    def tekst_samenvoegen(first_value: any, second_value: any, third_value: any) -> str:
        """**Combine multiple values to a string**
        
        By calling this function you will add multiple values together as a string.

        Args:
            first_value(any): This is the first part of the new_string.
            second_value(any): This is the second part of the new_string.
            third_value(any): This is the last part of the new_string.

        Returns:
            A string combining all given values.
            Example: "This is a string"
        """
        new_string = f"{str(first_value)} {str(second_value)} {str(third_value)}"

        return new_string

    @staticmethod
    def random_bsn() -> str:
        """**Generate a random bsn**
        
        By calling this functions you will generate a random number. To verify if the number is a bsn,
        it goes through a elfproef. If the elfproef returns False, then the function runs until the elfproef
        returns True.

        Returns:
            A string containing the generated bsn.
            Example: "633064488"
        """
        valid_bsn = False

        while not valid_bsn:
            possible_bsn = random.randint(10000000, 999999999)
            bsn_check = bsn.bsn()
            valid_bsn = bsn_check.validate_bsn(possible_bsn)

        return str(possible_bsn)

    @staticmethod
    def handmatige_waarde(value: any) -> any:
        pass

    @staticmethod
    def bron_waarde(get_connector: str, get_connector_field: str) -> list:
        pass

    @staticmethod
    def veld_waarde(field_id: str) -> any:
        pass

    @classmethod
    def metainfo(cls) -> list:
        """**Gives all the information of the functions in the class Functions**

        Args:
            cls: The functions class containing the generator functions.

        Returns:
            A list of all the functions and parameters with their datatypes.
            Example: [{"label": "Extra dagen optellen", "parameters": {"original_date": "str", "extra_days": "int",
            "return": str"}}, ...]
        """

        function_list = [function for function in dir(cls) if not function.startswith(("_", "metainfo"))]
        functions_and_parameters_list = []

        for function in function_list:
            function_dict = {}

            annotations = eval(f"{cls.__name__}.{function}.__annotations__")
            params = {annotation: annotations[annotation].__name__ for annotation in annotations}

            function_dict["id"] = function
            function_dict["label"] = function.replace("_", " ").capitalize()
            function_dict["parameters"] = params
            functions_and_parameters_list.append(function_dict)

        return functions_and_parameters_list

