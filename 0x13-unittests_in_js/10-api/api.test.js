const { expect } = require('chai');
const request = require("request");

describe('Test API Integration', () => {
  describe('GET /', () => {
    let url = 'http://localhost:7865';

    it('return status 200', (done) => {
      request(url, function(error, res, body){
      expect(res.statusCode).to.equal(200);
      expect(body).to.equal('Welcome to the payment system');
      done();
      });
    });     
  });

  describe('GET/cart/7', () => {
    let url = 'http://localhost:7865/cart/7';

    it('return status 200 and id 7', (done) => {
      request(url,function(error, res, body){
        expect(res.statusCode).to.equal(200);
        expect(body).to.equal('Payment methods for cart 7');
        done();
      });
    });
  });

  describe('GET/cart/hello 404 for invalid Id number', () => {
    let url = 'http://localhost:7865/cart/hello';

    it('return status 404', (done) => {
      request(url,function(error, res, body){
        expect(res.statusCode).to.equal(404);
        done();
      });
    });
  });

  describe('POST method /login with valid username', () => {
    it('returns 200 and correct name Betty', (done) => {
      const login_index = {
        url: 'http://localhost:7865/login',
        method: 'POST',
        json: {
          userName: 'Betty',
        },
      };
      request(login_index, function (error, res, body) {
        expect(res.statusCode).to.equal(200);
        expect(body).to.equal('Welcome Betty');
        done();
      });
    });
  });
  
  describe('GET method /available_payments ', () => {
    it('return 200 with payment method string', (done) => {
      const payment_index = {
        url: 'http://localhost:7865/available_payments',
        method: 'GET',
      };
      request(payment_index, function (error, res, body) {
        expect(res.statusCode).to.equal(200);
        expect(body).to.equal(
          '{"payment_methods":{"credit_cards":true,"paypal":false}}'
        );
        done();
      });
    });
  });
});
