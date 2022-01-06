const Utils = require('./utils')
const sinon = require('sinon');
const { expect }  = require('chai');
const sendPaymentRequestToApi = require('./3-payment');


describe('Utils Spies', function () {
  it('Spies output:', () => {
    const spyFunction = sinon.spy(Utils, 'calculateNumber');
    const spyRes = sinon.spy(console, 'log');

    sendPaymentRequestToApi(100, 20);

    expect(spyFunction.calledOnceWithExactly('SUM', 100, 20)).to.be.true;
    expect(spyRes.calledOnceWithExactly('The total is: 120')).to.be.true;

    spyFunction.restore();
    spyRes.restore();
  });
});
