<h1 align="center">🛡️ Fraud Detection System</h1>

<p align="center">
A machine learning project using <b>Neural Networks (MLP)</b> to detect fraudulent transactions based on historical data.<br>
The model preprocesses, encodes, and normalizes transaction details before making predictions.
</p>

---

<h2>📌 Features</h2>

<ul>
  <li>Preprocessing categorical and numerical data</li>
  <li>MLPClassifier with custom architecture <code>(10,8,10)</code></li>
  <li>Model training and evaluation with classification report</li>
  <li>Fraud probability prediction for new transactions</li>
</ul>

---

<h2>🛠️ Tech Stack</h2>

<ul>
  <li>Python 3.x</li>
  <li>Pandas</li>
  <li>Scikit-learn</li>
</ul>

---

<h2>📂 Dataset</h2>

<p>
Example dataset (<code>fraudes.csv</code>) should include:
</p>
<ul>
  <li><code>transaction_id</code>, <code>customer_id</code> <i>(removed during preprocessing)</i></li>
  <li><code>amount</code>, <code>time</code>, <code>location</code>, <code>is_fraud</code></li>
</ul>

---

<h2>🚀 How to Run</h2>

<pre>
# 1️⃣ Install dependencies
pip install pandas scikit-learn

# 2️⃣ Place 'fraudes.csv' in the project root

# 3️⃣ Run the script
python fraud_detection.py
</pre>

---

<h2>📊 Example Output</h2>

<table>
  <tr>
    <th>amount</th>
    <th>time</th>
    <th>location</th>
    <th>fraud_probability</th>
    <th>is_fraud_predicted</th>
  </tr>
  <tr>
    <td>1235.30</td>
    <td>10</td>
    <td>Loja Física</td>
    <td>0.78</td>
    <td>1</td>
  </tr>
  <tr>
    <td>12.53</td>
    <td>13</td>
    <td>Online</td>
    <td>0.02</td>
    <td>0</td>
  </tr>
</table>

---

<h2>📄 License</h2>
<p>MIT License</p>
