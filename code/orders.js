import React, { useState, useEffect } from "react";

function Orders() {
  const [orders, setOrders] = useState([]);

  useEffect(() => {
    fetch("/api/orders")
      .then((res) => res.json())
      .then((data) => setOrders(data));
  }, []);

  return (
    <div>
      <h1>My Orders</h1>
      <ul>
        {orders.map((order) => (
          <li key={order.id}>
            <p>Order ID: {order.id}</p>
            <p>Order Date: {order.order_date}</p>
            <p>Total Amount: {order.total_amount}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Orders;