const sinon = require('sinon');
const { expect }  = require('chai');
const sendPaymentRequestToApi = require('./3-payment');
const utils = require('./utils')


describe('Spies', function () {
  it('Is the same math', () => {
    const spyFunction = sinon.spy(utils, 'calculateNumber');
    const spyConsole = sinon.spy(console, 'log');
    const apiRequest = sendPaymentRequestToApi(100, 20);


    expect(spyFunction.calledOnceWithExactly('SUM', 100, 20)).to.be.true;
    expect(spyConsole.calledOnceWithExactly('The total is: 120')).to.be.true;
    expect(utils.calculateNumber('SUM', 100, 20)).to.equal(apiRequest);

    spyFunction.restore();
    spyConsole.restore();
  });
});
