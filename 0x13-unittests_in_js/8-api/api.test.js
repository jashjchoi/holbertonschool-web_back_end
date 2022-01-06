const { expect } = require('chai');
const request = require("request");

describe('Test API Integration', () => {
  describe('GET /', () => {
    let url = 'http://localhost:7865';

    it('return status 200', (done) => {
      request(url, function(error, response, body){
      expect(response.statusCode).to.equal(200);
      expect(body).to.equal('Welcome to the payment system');
      done();
      });
    });     
  });
});
