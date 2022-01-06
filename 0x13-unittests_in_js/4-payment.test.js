const Utils = require('./utils')
const sinon = require('sinon');
const { expect }  = require('chai');
const sendPaymentRequestToApi = require('./3-payment');


describe('Utils Stubs', function () {
  it('Stubs output:', () => {
    const stubFunction = sinon.stub(Utils, 'calculateNumber');
    stubFunction.returns(10)
    const spyRes = sinon.spy(console, 'log');

    sendPaymentRequestToApi(100, 20);

    expect(stubFunction.calledOnceWithExactly('SUM', 100, 20)).to.equal(true);
    expect(spyRes.calledOnceWithExactly('The total is: 10')).to.equal(true);

    stubFunction.restore();
    spyRes.restore();
  });
});
