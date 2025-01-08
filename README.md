# Project Bank Apps

![PyPi](https://img.shields.io/pypi/v/Bank_apps?style=plastic) 
![license](https://img.shields.io/github/license/Collin_Farell/Bank_apps)
![Twitch](https://img.shields.io/twitch/status/lo_loler)

**Bank_apps**

## This is a banking application for conducting banking transactions.

## Installation

1. Clone repozitory:
```git clone
https://github.com/AlexisKr/Bank_apps.git
```

2. install dependencies:
```python
pip install -r requirements.txt
```

## Ussage

1.Open the application in your web browser
2.Enter your data and get answers

```python
def get_mask_account(number_of_bill: str) -> str:
    """принимает на вход номер счета в виде числа
    и возвращает маску номера по правилу **XXXX
    """

    str_bill_number = str(number_of_bill)  # вернет строку

    return "*" * len(str_bill_number[:-14]) + str_bill_number[-4:]
```

## Documentation

For more information, please contact us by email

## Installation 
Please download the repozitory on your computer and install the necessary dependencies

## Launching the application
To run the application, you need to run the main.py file in the python <name>.py - from the root of the project repository
python <_path_>name.py - from another folder
<_path_> - path to the file <name>.py of the Homework10 project

## License

The project is distributed under the [MIT license](LICENSE)
