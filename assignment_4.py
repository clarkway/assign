{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "print (\"if you want to quit, press '0' \")\n",
    "while True:\n",
    "    go_on=True\n",
    "    given=input(\"Please enter an integer number: \")\n",
    "    if not given.isdecimal():\n",
    "      print(\"This is not an integer number, enter an integer number!\")\n",
    "      go_on=False\n",
    "    \n",
    "    if go_on!=False:\n",
    "      num=int(given)\n",
    "      prime=[2,3,5,7]\n",
    "      if num in prime:\n",
    "        print (num, \"is a prime number\")\n",
    "      elif num%2!=0 and num%3!=0 and num%5!=0 and num%7!=0 and num>1:\n",
    "        print (num, \"is a prime number\")\n",
    "      elif num==0:\n",
    "        break\n",
    "      else:\n",
    "        print (num, \"is NOT a prime number\")"
   ]
  }
 ],
 "metadata": {
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
   "version": 3
  },
  "orig_nbformat": 2
 },
 "nbformat": 4,
 "nbformat_minor": 2
}