const Utils = require('./utils');
const sinon = require('sinon');
const { expect } = require('chai');
const sendPaymentRequestToApi = require('./5-payment');


describe('Hooks Output:', () => {
  let spyRes;
  beforeEach(() => {
    spyRes = sinon.spy(console, 'log');
  });

  afterEach(() => {
    spyRes.restore();
  });

  it('The total is: 120', () => {
    sendPaymentRequestToApi(100, 20);
    expect(spyRes.calledOnceWithExactly('The total is: 120')).to.equal(true);
    expect(spyRes.calledOnce).to.equal(true);
  });

  it('The total is: 20', () => {
    sendPaymentRequestToApi(10, 10);
    expect(spyRes.calledOnceWithExactly('The total is: 20')).to.equal(true);
    expect(spyRes.calledOnce).to.equal(true);
  });
});
