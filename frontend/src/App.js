import React, { useState } from "react";
import { detectFraud, getBalance } from "./api";

function App() {
  const [address, setAddress] = useState("");
  const [balance, setBalance] = useState("");
  const [result, setResult] = useState("");

  const handleBalance = async () => {
    try {
      const res = await getBalance(address);
      setBalance(res.data.balance);
    } catch (err) {
      console.error(err);
      alert("Error fetching balance");
    }
  };

  const handleDetect = async () => {
    try {
      const res = await detectFraud({
        value: 20,
        gas: 50000,
        tx_count: 10,
      });
      setResult(res.data.result);
    } catch (err) {
      console.error(err);
      alert("Detection failed");
    }
  };

  return (
    <div style={{ padding: "30px" }}>
      <h1>🔗 BlockTraceX Dashboard</h1>

      <h2>Wallet Balance</h2>
      <input
        placeholder="Enter wallet address"
        onChange={(e) => setAddress(e.target.value)}
        style={{ width: "400px" }}
      />
      <button onClick={handleBalance}>Get Balance</button>

      <p><b>Balance:</b> {balance}</p>

      <hr />

      <h2>Fraud Detection</h2>
      <button onClick={handleDetect}>Check Transaction</button>

      <p><b>Result:</b> {result}</p>
    </div>
  );
}

export default App;