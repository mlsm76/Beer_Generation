{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pickle\n",
    "import numpy as np\n",
    "from flask import Flask, request"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [],
   "source": [
    "#defines a global variable called \"model\" and populates it with the load_model function\n",
    "model = None\n",
    "\n",
    "def load_model():\n",
    "    global model\n",
    "    # model variable refers to the global variable\n",
    "    with open('knn_dbscan.pkl', 'rb') as f:\n",
    "        model = pickle.load(f)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [],
   "source": [
    "beer_app = Flask(__name__)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [],
   "source": [
    "@beer_app.route('/')\n",
    "def home_endpoint():\n",
    "    return 'Test'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [],
   "source": [
    "@beer_app.route('/predict', methods=['POST'])\n",
    "def get_prediction():\n",
    "    # Works only for a single sample\n",
    "    if request.method == 'POST':\n",
    "        data = request.get_json()  # Get data posted as a json\n",
    "        data = np.array(data)[np.newaxis, :]  # converts shape from (4,) to (1, 4)\n",
    "        prediction = model.predict(data)  # runs globally loaded model on the data\n",
    "    return str(prediction[0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app \"__main__\" (lazy loading)\n",
      " * Environment: production\n",
      "   WARNING: Do not use the development server in a production environment.\n",
      "   Use a production WSGI server instead.\n",
      " * Debug mode: off\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      " * Running on http://0.0.0.0:333/ (Press CTRL+C to quit)\n"
     ]
    }
   ],
   "source": [
    "if __name__ == '__main__':\n",
    "    load_model()  # load model at the beginning once only\n",
    "    beer_app.run(host='0.0.0.0', port=333)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
