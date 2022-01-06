const express = require('express');
const app = express();
const port = 7865;


app.use(express.json());

app.get('/', (req, res) => {
  res.send('Welcome to the payment system');
});

app.listen(port, () => {
  console.log('API available on localhost port 7865');
});

app.get('/cart/:id([0-9]+)', (req, res) => {
  const id = req.params.id;
  res.send(`Payment methods for cart ${id}`);
});

app.get('/available_payments', (req, res) => {
  const paymentData = {
    payment_methods: {
      credit_cards: true,
      paypal: false
    }
  };
  res.json(paymentData)
});

app.post('/login', (req, res) => {
  const username = req.body.userName;
  res.end(`Welcome ${username}`);
});
