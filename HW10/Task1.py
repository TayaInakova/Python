{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 130,
   "id": "3f9e827a",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 131,
   "id": "947e4d2f",
   "metadata": {},
   "outputs": [],
   "source": [
    "arr1 = np.random.random(12)\n",
    "arr2 = np.linspace(1, 30, 12, dtype=int)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 132,
   "id": "ee00e428",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([0.32372503, 0.62718856, 0.03497399, 0.97572812, 0.92963241,\n",
       "       0.12547121, 0.82117273, 0.33261652, 0.1118611 , 0.89574636,\n",
       "       0.04894013, 0.93149251])"
      ]
     },
     "execution_count": 132,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 133,
   "id": "45e3f2f1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 1,  3,  6,  8, 11, 14, 16, 19, 22, 24, 27, 30])"
      ]
     },
     "execution_count": 133,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 134,
   "id": "29147527",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 1.32372503,  3.62718856,  6.03497399,  8.97572812, 11.92963241,\n",
       "       14.12547121, 16.82117273, 19.33261652, 22.1118611 , 24.89574636,\n",
       "       27.04894013, 30.93149251])"
      ]
     },
     "execution_count": 134,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr3 = arr1 + arr2\n",
    "arr3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 135,
   "id": "10a69af6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 0.32372503,  1.88156568,  0.20984391,  7.80582493, 10.22595651,\n",
       "        1.75659697, 13.13876362,  6.31971392,  2.46094417, 21.49791253,\n",
       "        1.32138339, 27.94477531])"
      ]
     },
     "execution_count": 135,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr4 = arr1 * arr2\n",
    "arr4"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 136,
   "id": "a96dba96",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([0.32372503, 0.20906285, 0.005829  , 0.12196601, 0.08451204,\n",
       "       0.00896223, 0.0513233 , 0.01750613, 0.0050846 , 0.03732276,\n",
       "       0.0018126 , 0.03104975])"
      ]
     },
     "execution_count": 136,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr5 = arr1 / arr2\n",
    "arr5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 137,
   "id": "2a7ebe28",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[0.32372503, 0.62718856, 0.03497399, 0.97572812],\n",
       "       [0.92963241, 0.12547121, 0.82117273, 0.33261652],\n",
       "       [0.1118611 , 0.89574636, 0.04894013, 0.93149251]])"
      ]
     },
     "execution_count": 137,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr6 = arr1.reshape(3, 4)\n",
    "arr6"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 138,
   "id": "2ed7faa3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([0.97572812, 0.92963241, 0.93149251])"
      ]
     },
     "execution_count": 138,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr6.max(axis=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 139,
   "id": "d07a233a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([0.92963241, 0.89574636, 0.82117273, 0.97572812])"
      ]
     },
     "execution_count": 139,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr6.max(axis=0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 140,
   "id": "d103734e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.9757281164137986"
      ]
     },
     "execution_count": 140,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr1.max()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 141,
   "id": "ca84473a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "30"
      ]
     },
     "execution_count": 141,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr2.max()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 142,
   "id": "cbdeb52d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[0.32372503, 0.62718856, 0.03497399],\n",
       "       [0.97572812, 0.92963241, 0.12547121],\n",
       "       [0.82117273, 0.33261652, 0.1118611 ],\n",
       "       [0.89574636, 0.04894013, 0.93149251]])"
      ]
     },
     "execution_count": 142,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr1.reshape(4, 3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 143,
   "id": "22155981",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 1,  3],\n",
       "       [ 6,  8],\n",
       "       [11, 14],\n",
       "       [16, 19],\n",
       "       [22, 24],\n",
       "       [27, 30]])"
      ]
     },
     "execution_count": 143,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr2.reshape(-1, 2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c9f6396d",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "96ab41f5",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c47e214f",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "aa94ea74",
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
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
