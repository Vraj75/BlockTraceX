import axios from "axios";

const API = "http://127.0.0.1:8000";

export const detectFraud = (data) =>
  axios.post(`${API}/detect`, data);

export const getBalance = (address) =>
  axios.get(`${API}/balance/${address}`);