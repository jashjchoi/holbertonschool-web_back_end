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

  describe('GET/cart/hello', () => {
    let url = 'http://localhost:7865/cart/hello';

    it('return status 404', (done) => {
      request(url,function(error, res, body){
        expect(res.statusCode).to.equal(404);
        done();
      });
    });
  });
});
