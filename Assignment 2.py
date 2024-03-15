{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "a60c1ec3-c754-4ec1-af7d-2d8f2dc863e3",
   "metadata": {},
   "outputs": [],
   "source": [
    "#integer data type \n",
    "\n",
    "shoesize= 43"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "6bed53cf-14f7-43fa-985f-e8cce786b8f6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "shoesize: 43\n"
     ]
    }
   ],
   "source": [
    "print (\"shoesize:\" ,shoesize)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "5049b49c-0015-4e6c-8c14-3934c1858359",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "int"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(shoesize)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "5afa3025-e5ad-405d-8621-cc741fba87fc",
   "metadata": {},
   "outputs": [],
   "source": [
    "#float data type \n",
    "\n",
    "weight_kg= 60.6"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "d8244d55-d4d5-48bf-91b6-d397e05320c0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "weight in kg: 60.6\n"
     ]
    }
   ],
   "source": [
    "print(\"weight in kg:\", weight_kg)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "80ff74c6-2b84-4b65-bc17-bc605d58d50a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "float"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(weight_kg)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "a9d5d996-8a71-4694-8264-8a10a97abd4e",
   "metadata": {},
   "outputs": [],
   "source": [
    "#complex data type\n",
    "vector= 14 + 20j"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "796287c2-0f5f-4f54-a8c1-b11636532855",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "complex_number (14+20j)\n"
     ]
    }
   ],
   "source": [
    "print(\"complex_number\",  vector)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "181a558c-ad42-40bf-89f4-d7a590c8e524",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "complex"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(vector)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "8babe333-5928-45ab-9f50-b78e8ae8392b",
   "metadata": {},
   "outputs": [],
   "source": [
    "#string data type\n",
    "warning=\"caveat emptor!\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "4ebec1ce-862d-4f57-a906-ffcb65bed83f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "warning: caveat emptor!\n"
     ]
    }
   ],
   "source": [
    "print(\"warning:\" ,warning)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "9926066c-e2d2-47c6-bed4-535158e83ea4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "str"
      ]
     },
     "execution_count": 52,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(warning)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "1b8069b9-24d7-4a90-86e0-9bfcf0a03a78",
   "metadata": {},
   "outputs": [],
   "source": [
    "# boolean value\n",
    "\n",
    "is_an_employee=True"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "86ac3eba-716f-4f23-bdef-77d39116b5b1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Employee: True\n"
     ]
    }
   ],
   "source": [
    "print(\"Employee:\", is_an_employee)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "7429cb1a-91a3-4ae9-bfd1-49bbeaccfe44",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "bool"
      ]
     },
     "execution_count": 58,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(is_an_employee)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "id": "63eed9bb-4db1-4f41-926c-321bbd9073fd",
   "metadata": {},
   "outputs": [],
   "source": [
    "#tuple data type\n",
    "\n",
    "products =( \"beverages\", \"clothes\",\"shoes\",\"confectioneries\", \"stationaries\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "id": "85fa35e5-09e5-42e0-83e4-3d4ab3c407ec",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "tuple"
      ]
     },
     "execution_count": 68,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(products)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "id": "e5f4f7eb-0ed9-4786-ac55-961ecf434939",
   "metadata": {},
   "outputs": [],
   "source": [
    "#list data type\n",
    "African_countries= [\"mali\", \"togo\",\"benin\", \"madagascar\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "id": "feec0251-a389-443b-aad4-ef8ee2a7c721",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "list"
      ]
     },
     "execution_count": 78,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(African_countries)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "id": "cf82486e-466e-4c0f-a3ba-d95a12658dcf",
   "metadata": {},
   "outputs": [],
   "source": [
    "# set data type\n",
    "week_days= { \"mon\", \"tues\", \"wed\", \"thur\", \"fri\",\"sat\"}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "id": "f6eb062b-b34f-4e5e-b405-bc9dd9751ac1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "set"
      ]
     },
     "execution_count": 81,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(week_days)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "id": "ba484f34-40ee-453f-9e49-0461b799b5a3",
   "metadata": {},
   "outputs": [],
   "source": [
    "#frozen set\n",
    "vowels= frozenset ({'a','e','i','o','u'})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "id": "a9825b6f-384b-4d15-af7c-0c2b3e047967",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "frozenset"
      ]
     },
     "execution_count": 90,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(vowels)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 105,
   "id": "6ce463ec-9d5e-4a8b-94d5-e750511f53b2",
   "metadata": {},
   "outputs": [],
   "source": [
    "# dictionary\n",
    "\n",
    "employee_1={\"name\":\"John Davies\", \"age\":\"35\",\"state of origin\":\"Anambra\", \"is_employee\":True ,\"hobbies\": [\"bass\",\"poetry\",\"5D chess\"]}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 106,
   "id": "ba3230d9-0f66-4f90-9a44-b43b720c19b6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Employee Profile: {'name': 'John Davies', 'age': '35', 'state of origin': 'Anambra', 'is_employee': True, 'hobbies': ['bass', 'poetry', '5D chess']}\n"
     ]
    }
   ],
   "source": [
    "print(\"Employee Profile:\", employee_1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 107,
   "id": "fdfa38a4-8e67-4f98-b918-f5bbf5493e46",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dict"
      ]
     },
     "execution_count": 107,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(employee_1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 114,
   "id": "022cda27-92a5-48ab-9339-0ab5414905fc",
   "metadata": {},
   "outputs": [],
   "source": [
    "#range\n",
    "\n",
    "numbers = range(5,6,7)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 113,
   "id": "1330640c-6bbe-4604-b77b-904e553e60b3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "range"
      ]
     },
     "execution_count": 113,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(numbers)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7d229ae3-22a2-4d45-b447-1cb00b3091dd",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f9e06e48-18c5-42f4-9102-03ca5317cc9c",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
